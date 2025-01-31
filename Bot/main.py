from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from scrapping_dex import scrape_dex
import time
import os

# Constants
DEX_URL = "https://dexscreener.com/?rankBy=trendingScoreH6&order=desc&minLiq=1000&minAge=1&min6HVol=50&min1HVol=10"
USER_PROFILE_DIR = os.path.expanduser("~/.config/google-chrome")  # Update if necessary

if __name__ == "__main__":
    driver = None
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument(f"--user-data-dir={USER_PROFILE_DIR}")  # Use existing user profile

        # Path to ChromeDriver
        chrome_driver_path = "/usr/bin/chromedriver"  # Update this path as needed
        chrome_options.binary_location = "/usr/bin/google-chrome"

        # Create the driver
        service = ChromeService(executable_path=chrome_driver_path)
        driver = Chrome(service=service, options=chrome_options)

        driver.get(DEX_URL)
        print("Please solve the CAPTCHA if prompted.")
        input("Press Enter once the CAPTCHA is solved...")  # Wait for user to solve CAPTCHA

        while True:
            scrape_dex(driver)
            time.sleep(180)  # Wait before next scrape
    finally:
        if driver:
            driver.quit()
