from behave import given, when, then
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from tests.pages.bank_manager_page import BankManagerPage
from tests.models.customer import Customer

@given("I am on the banking application home page")
def step_open_home(context):
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    context.driver = Chrome(service=service, options=options)
    context.driver.get(
        "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    )
    context.page = BankManagerPage(context.driver)


@when("I log in as bank manager")
def step_login(context):
    context.page.login_manager()


@when("I add a new customer")
def step_add_customer(context):
    context.customer = Customer(
        first_name="Robert",
        last_name="Connolly",
        postcode="07014"
    )

    context.page.add_customer(context.customer)


@then("the customer should appear in the customer list")
def step_verify_added(context):
    context.page.open_customers()

    assert context.page.customer_exists(
        context.customer
    ), "Customer was not found in customer list"


@when("I delete the customer")
def step_delete_customer(context):
    context.page.delete_customer(context.customer)


@then("the customer should be removed successfully")
def step_verify_deleted(context):
    assert not context.page.customer_exists(
        context.customer
    ), "Customer was not deleted successfully"
