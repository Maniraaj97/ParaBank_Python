import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
