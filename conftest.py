import pytest
from selenium.webdriver import Firefox


@pytest.fixture(scope='session')
def driver():
    driver = Firefox('/home/darya/virtualenvs/selenium/lib/python3.7/site-packages/selenium/webdriver/firefox')
    yield driver
    driver.quit()
