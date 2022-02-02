import pytest
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope='session')
def driver():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = Firefox(options=opts)
    yield driver
    driver.quit()
