# PyAutoGUI Automations

This repository contains Python scripts for automating repetitive tasks using the `pyautogui` library. The scripts are designed to work on **macOS** and can be easily adapted for other platforms.

## Scripts Included

### 1. **Instahyre Auto-Apply Script**
Automates the process of clicking the "Apply" button on the Instahyre platform.

#### Features:
- Opens Google Chrome using Spotlight.
- Clicks the "Apply" button at specified screen coordinates.
- Configurable click interval and typing speed.
- Failsafe mechanism to abort the script by moving the mouse to the top-left corner.

#### Usage:
1. Open Instahyre in Google Chrome and navigate to the page with the "Apply" button.
2. Run the script:
   ```bash
   python3 instahyre_autoapply.py
   ```
3. Quickly switch to your desktop. The script will:
   - Open Chrome (if not already open).
   - Start clicking the "Apply" button at the specified coordinates every 1 second.

#### Configuration:
- Modify `APPLY_BUTTON_X`, `APPLY_BUTTON_Y` for the button's coordinates.
- Adjust `CLICK_INTERVAL` for the delay between clicks.
- Use `pyautogui.position()` to find the exact coordinates of the "Apply" button.

---

### 2. **Other Automations**
(Add descriptions of other scripts in your repository here as you expand the project.)

---

## Prerequisites
- Python 3.x
- `pyautogui` library
- Google Chrome installed on macOS

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/G-Sudarshan/pyautogui-automations.git
   cd pyautogui-automations
   ```

2. Install the required library:
   ```bash
   pip install pyautogui
   ```

## Usage
1. Navigate to the script you want to run:
   ```bash
   cd scripts
   ```

2. Run the desired script:
   ```bash
   python3 script_name.py
   ```

3. Follow the on-screen instructions or switch to the application you want to automate.

---

## Failsafe
To stop any script at any time, move the mouse cursor to the **top-left corner** of the screen.

## Notes
- Ensure the target application (e.g., Chrome) is visible and maximized.
- Adjust `time.sleep()` durations if the script runs too fast or too slow for your system.

## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

