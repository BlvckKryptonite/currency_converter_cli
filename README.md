# 💱 Currency Exchange CLI Application

Welcome to the Currency Exchange CLI — a Python-based terminal application that enables users to check exchange rates, convert currencies, and explore supported currency codes using real-time data via the Fawaz Ahmed Currency API.

![App Screenshot](docs/demo-screenshot.png) 

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Flowchart](#flowchart)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [Deployment](#deployment)
- [Testing](#testing)
- [Known Issues](#known-issues)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

---

## Overview

This CLI project is designed for users who want quick and reliable access to currency conversion tools directly from the terminal. The application:
- Supports real-time currency exchange rates
- Performs conversions
- Validates inputs
- Is fully optimized for a terminal width of 80x24 (Code Institute standard)

This project aligns with my long-term fintech goals and showcases clean, maintainable, and functional Python development in a real-world context.

---

## Features

- **Currency Conversion** – Convert between any two valid currencies.
- **Exchange Rate Check** – View real-time exchange rates between two currencies.
- **Supported Currencies** – View a list of available and supported currency codes.
- **User-friendly Menu** – Clear menu navigation and prompt validation.
- **Input Validation** – Regex checks for currency codes and float validation for amounts.
- **Loading Animation** – Simulated loading for API calls to enhance UX.
- **Deployed on Heroku** – Easily accessible for demo and testing.

---

## User Stories 🧑‍💻 

- As a user, I want to convert money between currencies easily.
- As a user, I want to view exchange rates without needing to use Google or external tools.
- As a user, I want to see a list of supported currencies if I’m unsure of valid inputs.
- As a user, I want clear feedback for invalid entries.
- As a user, I want the tool to work reliably without needing technical setup.

---

## Flowchart

To better understand the app’s logic and UX journey, see the flowchart diagram below:

![Currency Exchange Flowchart](docs/currency_exchange_flowchart.png)


---

## 🛠 Technologies Used

### Core Languages
- [Python 3.12.8](https://www.python.org/)

### Libraries
- `requests` – For HTTP API requests
- `json` – To handle API response parsing
- `re` – For regular expression validation
- `sys` – For exiting the application
- `time` – To simulate loading
- `typing` – For optional type hinting

### External API

- [Fawaz Ahmed Currency API](https://github.com/fawazahmed0/currency-api)
  - No API key required
  - CDN-delivered JSON exchange data
  - Over 200 currencies supported including crypto

---

## How to Run Locally

### 1. Clone the Repository

git clone https://github.com/BlvckKryptonite/currency_converter_cli.git
cd currency_converter_cli

### 2. Create a Virtual Environment

- As guided by Code Institute's "Getting hand's on with venv":
   - In the command palette, type: create environment and select Python: Create Environment…
   - Choose Venv from the dropdown list.
   - Choose the Python version
   - A .venv folder appear in the file explorer pane to show that the virtual environment has been created.
 
### 3. Install Dependencies

- pip install -r requirements.txt

### 4. Run the application

- python3 run.py

---

##  Deployment

The application is deployed using [Heroku](https://heroku.com), which provides a cloud platform with terminal support for Python apps.

### Live Site
[Currency Exchange CLI on Heroku 🔗](https://currency-converter-cli-fad75cd3b79c.herokuapp.com/)


### Deployment Steps

This project was deployed using Code Institue's mock terminal for Heroku:

- Steps for deployment:

  - Fork or clone this repository
  - Create a new Heroku app
  - Set buildpacks to Python and NodeJS in that specific order
  - Link the Heroku app to the repository
  - Click **Deploy**

---

## Testing

### Manual Testing

| Feature                    | Test Description                                      | Result  |
|---------------------------|--------------------------------------------------------|---------|
| Exchange Rate Viewing     | Tested with valid and invalid currency codes          | Passed  |
| Currency Conversion       | Tested with valid inputs, small/large numbers         | Passed  |
| View Supported Currencies | Verified list from API                                | Passed  |
| Currency Code Validation  | Checked with lowercase, empty, and incorrect formats  | Passed  |
| Amount Validation         | Tested negative, zero, non-numeric inputs             | Passed  |
| Menu Navigation           | Entered invalid choices to trigger validation         | Passed  |
| CLI Layout                | Verified readability on 80x24 terminal                | Passed  |

### Validators Used
- [PEP8 Online Validator](http://pep8online.com/)
- `pylint` in VS Code
- CI Python Essentials Linter Test Tool

---

## Issues Worth Noting

- The Heroku-hosted app may have a short delay when waking from sleep (common on the free tier).
- The API (Fawaz Ahmed's CDN) may temporarily lag due to high usage or CDN refresh intervals.
- ⚠️ Heads-up: This CLI application is optimized for desktop terminal use and performs best in environments with standard terminal dimensions (80x24). While it can technically be run on mobile browsers, some users may experience input delays, slower animations, or minor formatting issues due to limitations in mobile terminal emulation

---

## Potential Future Enhancements

- Add historical exchange rate checking
- Save session history of conversions
- Enhance visuals with `colorama` or terminal tables
- Add offline caching of currency data
- **Add Graphical User Interface (GUI):** Convert the app into a GUI or web-based version using frameworks such as Flask or Django (with a REST API backend) for smoother cross-device compatibility.
- **Responsive Web Terminal:** Implement a lightweight responsive terminal emulator for better mobile performance.
- **Historical Exchange Rates:** Add a feature to view past exchange rates based on date selection.
- **Currency Trends Dashboard:** Graph monthly or weekly currency trends using APIs like exchangerate.host or Fawaz API with charting libraries.
- **Multi-Language Support:** Offer localization for global users.

---

## Credits

- **API Provider**: [Fawaz Ahmed Currency API](https://github.com/fawazahmed0/currency-api)
- **Template**: [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)



