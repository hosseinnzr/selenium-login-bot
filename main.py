import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import LOGIN_URL, TARGET_URL, USERNAME, PASSWORD, CLASS_NAMES


def login(driver, username, password):
    """
    Automates the login process using the provided credentials.
    """
    try:
        driver.get(LOGIN_URL)
        time.sleep(2)

        # Locate input fields and enter user credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the submit button
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        time.sleep(4)
        print("Login process finished.")
        return True
    except Exception as e:
        print(f"An error occurred during login: {e}")
        return False


def hide_elements(driver, class_names):
    """
    Finds elements matching the given CSS class names and hides them using JavaScript.
    """
    try:
        for class_name in class_names:
            elements_to_hide = driver.find_elements(By.CLASS_NAME, class_name)
            for element in elements_to_hide:
                driver.execute_script("arguments[0].style.display = 'none';", element)
        print("Elements have been successfully hidden.")
    except Exception as e:
        print(f"An error occurred while hiding elements: {e}")


def main():
    # Initialize the Edge WebDriver instance
    driver = webdriver.Edge()

    # Initial login attempt
    if login(driver, USERNAME, PASSWORD):
        driver.get(TARGET_URL)
        hide_elements(driver, CLASS_NAMES)

    # Continuous session monitoring loop
    while True:
        try:
            current_url = driver.current_url

            # Re-authenticate if redirected to the login page
            if "account/login" in current_url:
                print("Session expired or logged out. Attempting to log in again...")
                if login(driver, USERNAME, PASSWORD):
                    driver.get(TARGET_URL)
                    hide_elements(driver, CLASS_NAMES)
            else:
                print("Session is active. Monitoring...")

            # Wait 10 seconds before checking session status again
            time.sleep(10)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    driver.quit()


if __name__ == "__main__":
    main()