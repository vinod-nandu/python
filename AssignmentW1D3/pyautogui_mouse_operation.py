import pyautogui


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


def mouse_operations() -> None:
	"""Demonstrate common mouse operations with PyAutoGUI."""
	screen_width, screen_height = pyautogui.size()
	center_x = screen_width // 2
	center_y = screen_height // 2

	# Move, click, double-click, and use the secondary mouse button.
	pyautogui.moveTo(center_x, center_y, duration=0.5)
	pyautogui.click()
	pyautogui.doubleClick()
	pyautogui.rightClick()

	# Drag from the current position and scroll the wheel.
	pyautogui.dragTo(center_x + 100, center_y, duration=0.5, button="left")
	pyautogui.scroll(3)

	# Read the mouse position after the operations.
	print("Mouse position:", pyautogui.position())


if __name__ == "__main__":
	mouse_operations()
