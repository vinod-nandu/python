import json
import random
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
from openpyxl import load_workbook
from playwright.sync_api import sync_playwright


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

CONTACT_FILE = "contacts.xlsx"
REPORT_DIR = Path("reports")
SCREENSHOT_DIR = REPORT_DIR / "screenshots"

REPORT_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# Read contact from Excel
# ---------------------------------------------------------

def read_contact():
    df = pd.read_excel(CONTACT_FILE)

    if df.empty:
        raise ValueError("contacts.xlsx is empty.")

    contact = df.iloc[0]

    return {
        "name": str(contact["name"]).strip(),
        "phone": str(contact["phone"]).strip(),
        "message_template": str(contact["message"]).strip()
    }


# ---------------------------------------------------------
# Extract last 3 received messages
# ---------------------------------------------------------

def extract_last_messages(page):
    messages = []

    # WhatsApp Web changes its DOM frequently.
    # This selector is intentionally simple and may need
    # adjustment if WhatsApp changes its interface.

    message_elements = page.locator(
        'div.message-in'
    )

    count = message_elements.count()

    start = max(0, count - 3)

    for i in range(start, count):
        try:
            message = message_elements.nth(i)

            text = message.locator(
                'span.selectable-text'
            ).last.inner_text(timeout=2000)

            timestamp = message.locator(
                'span[data-pre-plain-text]'
            ).get_attribute(
                "data-pre-plain-text"
            )

            messages.append({
                "message": text,
                "timestamp": timestamp
            })

        except Exception:
            continue

    return messages


# ---------------------------------------------------------
# Main automation
# ---------------------------------------------------------

def main():

    contact = read_contact()

    name = contact["name"]
    phone = contact["phone"]

    # Personalize message
    message = contact["message_template"].replace(
        "{name}",
        name
    )

    timestamp = datetime.now()

    screenshot_file = (
        SCREENSHOT_DIR /
        f"{timestamp.strftime('%Y%m%d_%H%M%S')}_{name}.png"
    )

    result = {
        "name": name,
        "phone": phone,
        "message": message,
        "sent": False,
        "screenshot": "",
        "messages": [],
        "error": ""
    }

    with sync_playwright() as p:

        # Persistent browser profile keeps WhatsApp login session.
        browser = p.chromium.launch_persistent_context(
            "whatsapp_profile",
            headless=False,
            channel="chrome"
        )

        page = browser.pages[0] if browser.pages else browser.new_page()

        try:

            # -------------------------------------------------
            # 1. Open WhatsApp Web
            # -------------------------------------------------

            page.goto(
                "https://web.whatsapp.com",
                wait_until="domcontentloaded"
            )

            print("Waiting for WhatsApp Web...")

            # The search field appears only after the profile is authenticated.
            search_selector = (
                'div[contenteditable="true"][data-tab="3"], '
                '[aria-label*="Search"]'
            )
            qr_code = page.locator('canvas').first

            if qr_code.is_visible(timeout=5000):
                print(
                    "Scan the WhatsApp QR code in Chrome to continue..."
                )

            page.wait_for_selector(
                search_selector,
                state="visible",
                timeout=120000
            )

            print("WhatsApp Web is ready.")

            # -------------------------------------------------
            # 2. Search contact
            # -------------------------------------------------

            search_box = page.locator(
                search_selector
            ).first

            search_box.fill(phone)

            time.sleep(2)

            # -------------------------------------------------
            # 3. Open matching contact
            # -------------------------------------------------

            contact_result = page.locator(
                f'span[title*="{phone}"], '
                '[role="gridcell"], '
                'div[data-testid="cell-frame-container"], '
                '[role="option"]'
            ).first

            contact_result.wait_for(
                state="visible",
                timeout=15000
            )

            contact_result.click()

            time.sleep(2)

            print(f"Opened chat: {name}")

            # -------------------------------------------------
            # 4. Locate message box
            # -------------------------------------------------

            message_box = page.locator(
                'div[contenteditable="true"]'
            ).last

            message_box.wait_for(
                state="visible",
                timeout=10000
            )

            # -------------------------------------------------
            # 5. Type personalized message
            # -------------------------------------------------

            message_box.fill(message)

            print("Message typed.")

            # -------------------------------------------------
            # 6. Human-like delay
            # -------------------------------------------------

            delay = random.uniform(2, 5)

            print(
                f"Waiting {delay:.1f} seconds before sending..."
            )

            time.sleep(delay)

            # -------------------------------------------------
            # 7. Send message
            # -------------------------------------------------

            message_box.press("Enter")

            time.sleep(2)

            # -------------------------------------------------
            # 8. Confirm message appears
            # -------------------------------------------------

            sent_message = page.locator(
                'span.selectable-text'
            ).filter(
                has_text=message
            ).last

            sent_message.wait_for(
                state="visible",
                timeout=10000
            )

            result["sent"] = True

            print("Message sent successfully.")

            # -------------------------------------------------
            # 9. Take screenshot
            # -------------------------------------------------

            page.screenshot(
                path=str(screenshot_file),
                full_page=False
            )

            result["screenshot"] = str(
                screenshot_file
            )

            print(
                f"Screenshot saved: {screenshot_file}"
            )

            # -------------------------------------------------
            # 10. Extract last 3 messages
            # -------------------------------------------------

            result["messages"] = extract_last_messages(page)

            print("Last 3 messages extracted.")

        except Exception as e:

            result["error"] = str(e)

            print(
                f"Automation failed: {e}"
            )

        finally:

            # -------------------------------------------------
            # 11. Store result
            # -------------------------------------------------

            browser.close()

    # ---------------------------------------------------------
    # 12. Generate dated reports
    # ---------------------------------------------------------

    report_date = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    json_file = (
        REPORT_DIR /
        f"whatsapp_report_{report_date}.json"
    )

    excel_file = (
        REPORT_DIR /
        f"whatsapp_report_{report_date}.xlsx"
    )

    # JSON report
    with open(
        json_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    # Excel report
    excel_data = {
        "Name": [result["name"]],
        "Phone": [result["phone"]],
        "Message": [result["message"]],
        "Sent": [result["sent"]],
        "Screenshot": [result["screenshot"]],
        "Extracted Messages": [
            json.dumps(
                result["messages"],
                ensure_ascii=False
            )
        ],
        "Error": [result["error"]]
    }

    report_df = pd.DataFrame(excel_data)

    report_df.to_excel(
        excel_file,
        index=False
    )

    print("\n--------------------------------")
    print("Automation completed")
    print("--------------------------------")
    print(f"JSON report : {json_file}")
    print(f"Excel report: {excel_file}")


# ---------------------------------------------------------
# Program entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
