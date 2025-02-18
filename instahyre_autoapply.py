import pyautogui
import time

# Configuration
TYPE_INTERVAL = 0.1  # Typing speed (adjust if needed)
APPLY_BUTTON_X = 782  # X-coordinate of the "Apply" button
APPLY_BUTTON_Y = 831  # Y-coordinate of the "Apply" button
CLICK_INTERVAL = 1  # 1-second delay between clicks

# Enable failsafe: Move mouse to top-left corner to abort
pyautogui.FAILSAFE = True

def activate_chrome():
    """Open Chrome using Spotlight (macOS)."""
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    time.sleep(1)  # Wait for Spotlight to open
    pyautogui.write('chrome', interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for Chrome to launch

def move_n_click(x, y):
    """Move the mouse to (x, y) and click."""
    pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement
    pyautogui.click()

def main():
    # Activate Chrome and ensure Instahyre is open
    activate_chrome()
    
    # Wait for Instahyre to load (adjust time as needed)
    time.sleep(3)
    
    try:
        while True:
            # Click the "Apply" button
            move_n_click(APPLY_BUTTON_X, APPLY_BUTTON_Y)
            print("Clicked Apply button!")
            time.sleep(CLICK_INTERVAL)  # Wait 1 second
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

if __name__ == "__main__":
    main()
