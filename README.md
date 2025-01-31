<h0 align="center">Scrap Bot</h0>

![Python 3](https://img.shields.io/badge/python-3-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

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

## Contributions

Contributions are welcome. To contribute to the project, please fork the repository, create a branch for your changes, and submit a pull request.

## License

This project is distributed under the MIT License. See the LICENSE file for more information.

Happy trading with Scrap Bot!

## Contact

For any inquiries, please email 4kiro2kiro@gmail.com
