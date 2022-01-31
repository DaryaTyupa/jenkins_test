from selenium.webdriver.common.by import By


def test_panda(driver):
    driver.get('https://plugins.jenkins.io/shiningpanda')
    title_element = driver.find_element(By.XPATH, "//*[@class='title']")
    assert title_element.text == 'ShiningPanda'

