# Selenium UI Automation – SauceDemo (Firefox + Pytest)

This project contains automated UI test cases for the SauceDemo website using Selenium WebDriver, pytest, and Firefox with webdriver_manager.

Project Structure:
Atlas-Guild/
├── conftest.py             - Reusable Firefox WebDriver fixture
├── tests/
│   ├── test_login.py       - Test: valid login
│   ├── test_add_to_cart.py - Test: add product to cart
│   └── test_checkout.py    - Test: checkout flow
└── README.md               - Setup + run instructions

Setup Instructions:

1. Clone the repository:
   git clone https://github.com/your-username/Atlas-Guild.git
   cd Atlas-Guild

2. (Optional) Create a virtual environment:
   python -m venv venv
   On Windows:
   venv\Scripts\activate
   On macOS/Linux:
   source venv/bin/activate

3. Install the dependencies:
   pip install -r requirements.txt
   (or manually: pip install selenium pytest webdriver_manager)

4. Prerequisites:
   - Python 3.10+
   - Firefox browser installed (https://www.mozilla.org/firefox/)

Running Tests:

To run all tests:
   pytest

To run a specific test:
   pytest tests/test_login.py

Tests Covered:
- Login with valid credentials
- Add product to cart
- Complete checkout flow

Tech Stack:
- Python
- Selenium WebDriver
- Pytest
- Firefox
- webdriver_manager

Author:
Shubhangi Ringasia
Email: your.email@example.com
GitHub: https://github.com/your-username
LinkedIn: https://www.linkedin.com/in/your-profile
