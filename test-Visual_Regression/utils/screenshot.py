# utils/screenshot.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import SCREENSHOTS_DIR

def capture_screenshot(browser_name, url, save_path):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.set_window_size(1920, 1080)
    driver.get(url)
    # Inject a fake visual change (for testing only)
    driver.execute_script("document.body.style.border = '10px solid red';")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    driver.save_screenshot(save_path)
    driver.quit()