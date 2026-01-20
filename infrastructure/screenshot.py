"""
Screenshot Manager
------------------
Captures screenshots for documentation and presentation.
"""

import os
import datetime
try:
    import pyautogui
except ImportError:
    pyautogui = None

import logging

logger = logging.getLogger("AtlasTech.Screenshot")

class ScreenshotManager:
    def __init__(self, output_dir="screenshots"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def capture(self, step_name):
        """Captures the entire screen."""
        if not pyautogui:
            logger.warning("pyautogui not installed. Skipping screenshot.")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{step_name}_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            logger.info(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None
