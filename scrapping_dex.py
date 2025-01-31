from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import re

# Constants
DATA_LOG_FILE = "data.txt"
BASE_URL = "https://dexscreener.com"

# Helper function to extract data with safety checks
def safe_extract(element, selectors, attr="text"):
    """Try multiple selectors to extract an element's text or attribute."""
    for selector in selectors:
        try:
            target_element = element.find_element(By.CSS_SELECTOR, selector)
            if attr == "text":
                return target_element.text
            return target_element.get_attribute(attr)
        except Exception:
            continue
    return None

# Function to extract price with special handling for cases
def extract_price(row):
    try:
        # Case 1: Price in span with title attribute
        complex_price = safe_extract(row, [".chakra-text.custom-0"], attr="title")
        if complex_price:
            return complex_price.replace("$", "").strip()

        # Case 2: Normal price in div
        normal_price = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-price"])
        if normal_price:
            return normal_price.strip("$")

        # If no price found
        return None
    except Exception:
        return None

# Function to extract link directly from HTML
def extract_link(row):
    try:
        # Get the HTML content of the row
        row_html = row.get_attribute("outerHTML")
        start_index = row_html.find("href=")
        if start_index != -1:
            start_index += 6  # Move past 'href="'
            end_index = row_html.find('"', start_index)
            link = row_html[start_index:end_index]
            return link
        return None
    except Exception as e:
        return None

# Function to extract ChakraLink using updated method
def extract_chakra_link(driver):
    try:
        # Method 1: Look for a span with a title attribute
        chakra_spans = driver.find_elements(By.XPATH, "//div[contains(@class, 'chakra-stack') and contains(@class, 'custom-133gp9')]//span[@class='chakra-text custom-72rvq0']")
        for span in chakra_spans:
            chakra_link = span.get_attribute("title")
            if chakra_link:
                print(f"Extracted ChakraLink from title: {chakra_link}")
                return chakra_link

        # Method 2: Look for a style element containing the link
        style_elements = driver.find_elements(By.XPATH, "//style")
        for style in style_elements:
            style_content = style.get_attribute("innerHTML")
            match = re.search(r"tokens/solana/([\w]+)", style_content)
            if match:
                chakra_link = match.group(1)
                print(f"Extracted ChakraLink from style: {chakra_link}")
                return chakra_link

        print("No valid ChakraLink found.")
        return None
    except Exception as e:
        print(f"Error extracting ChakraLink: {e}")
        return None

# Function to scrape additional data from individual crypto pages
def scrape_crypto_page(driver, crypto):
    url = f"{BASE_URL}{crypto['Link']}"
    print(f"Navigating to {url}")
    driver.get(url)

    try:
        # Wait for the page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chakra-stack"))
        )

        # Extract ChakraLink using the updated function
        chakra_link = extract_chakra_link(driver)
        crypto["ChakraLink"] = chakra_link

        print(f"Updated crypto data: {crypto}")

        return crypto

    except Exception as e:
        print(f"Error scraping crypto page: {e}")
        return crypto

# Scrape Dex Screener for data
def scrape_dex(driver):
    print("Starting Dex Screener scraper...")
    try:
        driver.refresh()  # Refresh the page
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ds-dex-table"))
        )

        # Locate all rows
        rows = driver.find_elements(By.CLASS_NAME, "ds-dex-table-row")
        print(f"Found {len(rows)} rows to scrape.")  # Log the number of rows
        scraped_data = []

        for index, row in enumerate(rows):
            try:
                # Extract required data
                link = extract_link(row)  # Special function to handle link extraction
                token_name = safe_extract(
                    row,
                    [".chakra-text.ds-dex-table-row-base-token-symbol", ".ds-dex-table-row-base-token-symbol"]
                )
                token_pair = safe_extract(row, [".ds-dex-table-row-quote-token-symbol"])
                price = extract_price(row)  # Special function to handle price extraction

                # Log progress in a minimalistic and clear way
                print(f"Row {index + 1}/{len(rows)}: Token={token_name}, Pair={token_pair}, Price={price}, Link={link}")

                age = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-pair-age span"])
                buys = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-buys"])
                sells = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-sells"])
                volume = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-volume"])
                makers = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-makers"])
                change_5m = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-price-change-m5 span"])
                change_1h = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-price-change-h1 span"])
                change_6h = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-price-change-h6 span"])
                change_24h = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-price-change-h24 span"])
                liquidity = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-liquidity"])
                market_cap = safe_extract(row, [".ds-table-data-cell.ds-dex-table-row-col-market-cap"])

                # Add data as a dictionary
                scraped_data.append({
                    "Link": link,
                    "Token": token_name,
                    "Pair": token_pair,
                    "Price": price,
                    "Age": age,
                    "Buys": buys,
                    "Sells": sells,
                    "Volume": volume,
                    "Makers": makers,
                    "5m": change_5m,
                    "1h": change_1h,
                    "6h": change_6h,
                    "24h": change_24h,
                    "Liquidity": liquidity,
                    "MarketCap": market_cap,
                })
            except Exception as e:
                print(f"Error extracting data from row {index + 1}: {e}")

        # Write initial data to file
        with open(DATA_LOG_FILE, "w") as f:
            for data in scraped_data:
                f.write(str(data) + "\n")

        print(f"Initial data saved to {DATA_LOG_FILE}")

        # Process top 2 cryptos
        additional_data = []
        for i in range(2):
            if i < len(scraped_data):
                updated_crypto = scrape_crypto_page(driver, scraped_data[i])
                additional_data.append(updated_crypto)

        # Append additional data to file, separated by a line break
        with open(DATA_LOG_FILE, "a") as f:
            f.write("\n# Detailed Data\n")
            for data in additional_data:
                f.write(str(data) + "\n")

        print(f"Detailed data appended to {DATA_LOG_FILE}")
        return scraped_data

    except Exception as e:
        print(f"Error during scraping: {e}")
        with open(DATA_LOG_FILE, "a") as f:
            f.write(f"Error during scraping at {datetime.now().isoformat()}: {str(e)}\n")
        return []
