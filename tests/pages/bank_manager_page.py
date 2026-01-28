from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.models.customer import Customer


class BankManagerPage:
    """Page Object for Bank Manager actions in the banking app."""

    def __init__(self, driver):
        """Initialise the page with a Selenium WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def login_manager(self):
        """Log in as Bank Manager from the home page."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[ng-click='manager()']")
            )
        ).click()

    def add_customer(self, customer: Customer):
        """
        Add a new customer using the Bank Manager Add Customer form.

        :param customer: Customer object containing test data
        """
        # Open Add Customer tab
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[ng-click='addCust()']")
            )
        ).click()

        # Wait for form to be visible
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[ng-model='fName']")
            )
        )

        # Fill form
        self.driver.find_element(
            By.CSS_SELECTOR, "input[ng-model='fName']"
        ).send_keys(customer.first_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[ng-model='lName']"
        ).send_keys(customer.last_name)

        self.driver.find_element(
            By.CSS_SELECTOR, "input[ng-model='postCd']"
        ).send_keys(customer.postcode)

        # Submit form
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Accept confirmation alert
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def open_customers(self):
        """Navigate to the Customers list view."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[ng-click='showCust()']")
            )
        ).click()

    def customer_exists(self, customer: Customer) -> bool:
        """
        Check if a customer exists in the Customers table.

        :param customer: Customer object to search for
        :return: True if customer is present, otherwise False
        """
        def customer_row_present(driver):
            rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            return any(
                customer.first_name in row.text and
                customer.last_name in row.text
                for row in rows
            )

        try:
            self.wait.until(customer_row_present)
            return True
        except:
            return False

    def delete_customer(self, customer: Customer):
        """
        Delete a customer from the Customers table.

        :param customer: Customer object to be deleted
        """
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            if customer.first_name in row.text:
                delete_button = row.find_element(
                    By.CSS_SELECTOR, "button[ng-click='deleteCust(cust)']"
                )
                delete_button.click()
                break