
---

# 🧪 Python Selenium Practice Framework

A lightweight, modular automation testing framework built using **Python**, **Selenium**, and **Pytest**.
This project demonstrates professional-grade test design, page object modeling, CI/CD integration, and HTML reporting — aligned with expectations for a **Senior QA Automation Engineer II** role.

---

## 🚀 What This Repo Is About

This repository serves as a **practice framework** for UI test automation.
It automates user workflows on [SauceDemo](https://www.saucedemo.com/) — a demo e-commerce site for practicing Selenium automation.

The project is structured using **Page Object Model (POM)**, includes reusable fixtures, and supports scalable test execution via **Pytest**.

---

## 🧩 What We’re Testing

Key user flows on SauceDemo:

* Login (valid, invalid, locked-out, empty fields)
* Inventory validation (product count)
* Cart functionality (add to cart)
* Sorting dropdown behavior

---

## 🧪 List of Test Cases

| Test File                    | Description                                |
| ---------------------------- | ------------------------------------------ |
| `test_login_success.py`      | Valid login verification                   |
| `test_login_negative.py`     | Invalid password scenario                  |
| `test_login_edge_cases.py`   | Locked-out and empty-field validations     |
| `test_login_parametrized.py` | Parametrized version of all negative cases |
| `test_inventory_page.py`     | Verifies total product count post-login    |
| `test_add_to_cart.py`        | Validates adding item(s) to cart           |
| `test_sorting_dropdown.py`   | Validates sorting dropdown functionality   |

---

## ⚙️ Framework Features

* **Python + Selenium + Pytest**
* **Page Object Model (POM)** for maintainability
* **Fixtures** for setup/teardown (`conftest.py`)
* **Parametrized testing** for reusability
* **Webdriver Manager** (no manual driver setup)
* **Headless execution** for CI
* **HTML reporting** via `pytest-html`

---

## 🔧 Tools & Technologies

* **Python 3.14**
* **Selenium 4.x**
* **Pytest 8.x**
* **Webdriver Manager**
* **pytest-html**
* **GitHub Actions** for CI/CD

---

## 🧱 CI/CD Integration

Automated test execution runs via **GitHub Actions** on every push or pull request:

* Installs dependencies
* Runs Pytest suite in headless mode
* Generates HTML reports under `reports/report.html`

---

## 📊 Test Reporting

Run locally with:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

View your detailed report by opening `reports/report.html` in a browser.

---

## 🧠 Value-Added Highlights

* Modular design (pages, config, utils, tests)
* Readable, extensible structure for real projects
* Ready for CI/CD integration
* Demonstrates senior-level test design thinking

---

## 🧰 How to Run

```bash
# 1. Clone repo
git clone https://github.com/rohitkodate247/python-selenium-practice.git
cd python-selenium-practice

# 2. Create and activate virtual env
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest -v
```
