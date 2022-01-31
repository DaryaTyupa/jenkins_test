import pytest
from selenium.webdriver import Firefox


@pytest.fixture(scope='session')
def driver():
    driver = Firefox()
    yield driver
    driver.quit()
