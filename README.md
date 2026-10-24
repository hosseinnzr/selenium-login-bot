# Selenium Web Automation & Session Monitor

This project is a browser automation script built with **Selenium** in Python. It handles automated login, session management, dynamic JavaScript-based element hiding, and continuous session monitoring.

## Features
- **Automated Login:** Automatically fills in username and password fields and submits the form.
- **Session Management:** Continuously monitors the active URL and re-authenticates if the session expires or redirects to the login page.
- **Element Hiding:** Hides specific webpage elements dynamically using JavaScript based on CSS class names.
- **Continuous Monitoring:** Periodically checks the session status in a background loop.

---

## Prerequisites

Before running the script, make sure you have the following installed:
- **Python** (v3.8 or higher)
- **Microsoft Edge** browser

---

## Installation & Setup

1. Clone or download the project files into your working directory.

2. Create a `requirements.txt` file in the project root directory with the following content:
```text
selenium>=4.0.0
webdriver-manager>=4.0.0