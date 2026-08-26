import argparse
import re
import shutil
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup


DEFAULT_URL = "https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671"
DEFAULT_OUTPUT = "chennai_hourly_weather.txt"


def fetch_html(url: str) -> str:
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/126.0.0.0 Safari/537.36"
		),
		"Accept-Language": "en-US,en;q=0.9",
	}
	response = requests.get(url, headers=headers, timeout=30)
	response.raise_for_status()
	return response.text


def fetch_html_with_edge(
	url: str,
	headless: bool = True,
	wait_seconds: int = 8,
	driver_path: Optional[str] = None,
) -> str:
	try:
		from selenium import webdriver
		from selenium.webdriver.edge.options import Options
		from selenium.webdriver.edge.service import Service
	except ImportError as exc:
		raise RuntimeError(
			"Selenium is not installed. Install it with: python -m pip install selenium"
		) from exc

	options = Options()
	if headless:
		options.add_argument("--headless=new")
	options.add_argument("--disable-gpu")
	options.add_argument("--no-sandbox")
	options.add_argument("--window-size=1920,1080")

	service = None
	resolved_driver_path = driver_path or shutil.which("msedgedriver")
	if resolved_driver_path:
		service = Service(executable_path=resolved_driver_path)

	try:
		driver = webdriver.Edge(service=service, options=options)
	except Exception as exc:
		raise RuntimeError(
			"Unable to start Microsoft Edge WebDriver. Download msedgedriver for your Edge "
			"version and pass it with --driver-path, or add msedgedriver.exe to PATH."
		) from exc

	try:
		driver.get(url)
		time.sleep(wait_seconds)
		return driver.page_source
	finally:
		driver.quit()


def fetch_html_with_edge_playwright(
	url: str,
	headless: bool = True,
	wait_seconds: int = 8,
) -> str:
	try:
		from playwright.sync_api import sync_playwright
	except ImportError as exc:
		raise RuntimeError(
			"Playwright is not installed. Install it with: python -m pip install playwright"
		) from exc

	with sync_playwright() as p:
		browser = p.chromium.launch(channel="msedge", headless=headless)
		try:
			page = browser.new_page()
			page.goto(url, wait_until="domcontentloaded", timeout=60000)
			page.wait_for_timeout(wait_seconds * 1000)
			return page.content()
		finally:
			browser.close()


def _extract_entry(text: str) -> Optional[Dict[str, str]]:
	text = re.sub(r"\s+", " ", text).strip()
	if not text:
		return None

	time_match = re.search(r"\b(\d{1,2}\s?(?:AM|PM))\b", text, flags=re.IGNORECASE)
	if not time_match:
		return None

	temp_match = re.search(r"\b(-?\d+)\s*°", text)
	realfeel_match = re.search(r"RealFeel(?:®)?\s*(-?\d+)\s*°", text, flags=re.IGNORECASE)
	precip_match = re.search(r"(\d+)\s*%", text)

	condition = ""
	condition_match = re.search(
		r"%\s*([^%]+?)(?:Heat Index|Wind|Air Quality|Humidity|Dew Point|Cloud Cover|Visibility|$)",
		text,
		flags=re.IGNORECASE,
	)
	if condition_match:
		condition = condition_match.group(1).strip(" .,-")

	return {
		"time": time_match.group(1).upper(),
		"temperature_c": temp_match.group(1) if temp_match else "N/A",
		"realfeel_c": realfeel_match.group(1) if realfeel_match else "N/A",
		"precipitation_percent": precip_match.group(1) if precip_match else "N/A",
		"condition": condition or "N/A",
		"raw": text,
	}


def parse_hourly_weather(html: str) -> List[Dict[str, str]]:
	soup = BeautifulSoup(html, "html.parser")
	entries = []
	seen_times = set()

	cards = soup.select(
		"div[class*='hourly-card'], li[class*='hourly-card'], a[class*='hourly-card']"
	)

	for card in cards:
		text = " ".join(card.stripped_strings)
		entry = _extract_entry(text)
		if not entry:
			continue
		if entry["time"] in seen_times:
			continue
		seen_times.add(entry["time"])
		entries.append(entry)

	if entries:
		return entries

	full_text = soup.get_text(" ", strip=True)
	chunks = re.findall(
		r"(\b\d{1,2}\s?(?:AM|PM)\b.*?)(?=\b\d{1,2}\s?(?:AM|PM)\b|HOURLY WEATHER FORECAST FOR|$)",
		full_text,
		flags=re.IGNORECASE,
	)

	for chunk in chunks[:48]:
		entry = _extract_entry(chunk)
		if not entry:
			continue
		if entry["time"] in seen_times:
			continue
		seen_times.add(entry["time"])
		entries.append(entry)

	return entries


def save_to_text_file(entries: List[Dict[str, str]], output_path: str, source_url: str) -> None:
	with open(output_path, "w", encoding="utf-8") as file:
		file.write("Chennai Hourly Weather (AccuWeather)\n")
		file.write(f"Source: {source_url}\n")
		file.write(f"Fetched at: {datetime.now().isoformat(sep=' ', timespec='seconds')}\n")
		file.write("=" * 70 + "\n\n")

		if not entries:
			file.write("No hourly entries were parsed from the page.\n")
			return

		for idx, entry in enumerate(entries, start=1):
			file.write(f"{idx}. Time: {entry['time']}\n")
			file.write(f"   Temperature: {entry['temperature_c']} C\n")
			file.write(f"   RealFeel: {entry['realfeel_c']} C\n")
			file.write(f"   Precipitation Chance: {entry['precipitation_percent']}%\n")
			file.write(f"   Condition: {entry['condition']}\n")
			file.write("\n")


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Scrape Chennai hourly weather from AccuWeather and save to a text file."
	)
	parser.add_argument("--url", default=DEFAULT_URL, help="Hourly weather page URL")
	parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output text file path")
	parser.add_argument(
		"--source",
		choices=["edge", "edge-playwright", "requests"],
		default="edge",
		help="How to fetch the page: edge (selenium then playwright fallback), edge-playwright, or direct requests.",
	)
	parser.add_argument(
		"--show-browser",
		action="store_true",
		help="Show the Edge browser window while loading the page.",
	)
	parser.add_argument(
		"--driver-path",
		default=None,
		help="Path to msedgedriver.exe (optional if already in PATH).",
	)
	args = parser.parse_args()

	try:
		if args.source == "edge":
			try:
				html = fetch_html_with_edge(
					args.url,
					headless=not args.show_browser,
					driver_path=args.driver_path,
				)
			except Exception:
				html = fetch_html_with_edge_playwright(
					args.url,
					headless=not args.show_browser,
				)
		elif args.source == "edge-playwright":
			html = fetch_html_with_edge_playwright(
				args.url,
				headless=not args.show_browser,
			)
		else:
			html = fetch_html(args.url)
		entries = parse_hourly_weather(html)
		save_to_text_file(entries, args.output, args.url)
		print(f"Saved {len(entries)} hourly entries to {args.output}")
	except Exception as exc:
		print(f"Failed to scrape weather data: {exc}")


if __name__ == "__main__":
	main()
