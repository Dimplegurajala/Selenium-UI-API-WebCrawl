# UI Automation Framework (SauceDemo)

This project is part of a **Multi-Domain Repository**. This branch (**branch-1**) contains the UI Automation suite.

##  Repository Map
- **branch-1 (Current)**: Selenium UI Automation (SauceDemo).
- **branch-2**: REST API Contract & Functional Testing.
- **branch-3**: TenForce Data Scraping Utility.

##  Branch-1 Features
- **Page Object Model**: Granular pages for Login, Products, Cart, and Checkout.
- **BasePage Engine**: Centralized waits and Shadow DOM fallback.
- **Data-Driven**: CSV-based PT/AT scenarios.
- **CI/CD**: GitHub Actions pipeline (headless execution).
- **Visual Evidence**: Base64 screenshots embedded in HTML reports on failure.

##  Local Setup
1. `pip install -r requirements.txt`.
2. `pytest --html=report.html --self-contained-html`.