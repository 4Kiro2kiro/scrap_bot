<h1 align="center">Scrap Bot</h1>

![Python 3](https://img.shields.io/badge/python-3-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## Description
Scrap Bot is an automated bot designed to engage with Solana meme cryptocurrency to generate profits. This bot utilizes automated trading strategies to buy and sell cryptocurrency under optimal market conditions.

## Features
- **Market Analysis**: Scans the cryptocurrency market to detect price trends of Solana.
- **Automated Trading**: Executes buy and sell orders based on predefined algorithms and trading signals.
- **Risk Management**: Limits potential losses with an integrated risk management system.
- **Reports and Notifications**: Provides real-time updates through notifications about performed actions and portfolio status.

## Technologies Used
- Python 3.11: The main programming language.
- CCXT: A library used to connect the bot to cryptocurrency exchanges.
- Pandas & NumPy: For data processing and mathematical calculations.

## Installation
To install Scrap Bot, follow the instructions below:

```bash
git clone https://github.com/4Kiro2Kiro/scrap_bot.git
cd scrap_bot
```

## Configuration

Before running the bot, you need to set up parameters for google driver :

### Setting Up Selenium WebDriver with Google Chrome

- 1-**Install Google Chrome**:
   Download and install Google Chrome from [the official site](https://www.google.com/chrome/).

- 2-**Download Chromedriver**:
   Get the appropriate version of Chromedriver from [the official page](https://sites.google.com/chromium.org/driver/).

- 3-**Install Chromedriver**:
   Unzip and place Chromedriver in a directory included in your system's PATH.

- 4-**Configure Your Script to Use Chromedriver**:
   Ensure the path to `chromedriver` is used in your Python script or that it's included in your PATH.

- 5-**Verify Installation**:
   Test Chromedriver by running a Python script that opens Google Chrome and loads a page.

These streamlined steps guide you through the necessary setup to use Selenium WebDriver with Google Chrome.

## Usage

To start the bot, if you are on **linux**, run:

```bash
source venv_environment/bin/activate/
```

If you are on **windows**, run:

```bash
pip install -r requirements.txt
```

And after:

```bash
python main.py
```

## ⚠️ Important ⚠️

If the *cloudflare* captcha doesn't **work**, first launch google manually and go to the dex website [here](https://dexscreener.com/new-pairs), re-solder the captcha and then relaunch the bot !

## How Does It Work?

Scrap Bot operates by automating interactions with cryptocurrency markets using the Selenium WebDriver. Here is an overview of the key steps:

1. **Initialization**:
   - The bot starts by initializing its settings directly within the code, setting up API keys, trading preferences, and browser configurations manually.

2. **Market Connection**:
   - Using Selenium, the bot opens a session in Google Chrome and connects to the trading platform where it will execute transactions. This includes navigating to specific pages and authenticating if necessary.

3. **Market Monitoring**:
   - The bot monitors cryptocurrency prices in real-time and applies trend detection algorithms to identify potential trading opportunities.

4. **Executing Transactions**:
   - When a trading opportunity meets the defined criteria, the bot automatically executes buy or sell orders based on trading signals. This step is crucial and requires a rapid response to market changes.

5. **Risk Management**:
   - To minimize risks, the bot employs predefined risk management strategies such as stop-loss and take-profit orders to protect the invested capital.

6. **Reporting**:
   - At the end of each trading session, the bot generates a performance report detailing executed trades, profits and losses, and other relevant statistics. All this information is stored in a `data.txt` file for record-keeping and further analysis.

7. **Shutdown**:
   - After the trading session, the bot closes all active connections and terminates cleanly, ensuring all resources are released.

This automated process allows Scrap Bot to operate 24/7, thus maximizing trading opportunities without the need for constant human intervention.

## Contributions

Contributions are welcome. To contribute to the project, please fork the repository, create a branch for your changes, and submit a pull request.

## License

This project is distributed under the MIT License. See the LICENSE file for more information.

Happy trading with Scrap Bot!

## Contact

For any inquiries, please email 4kiro2kiro@gmail.com
