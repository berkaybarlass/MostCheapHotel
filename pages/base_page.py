from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def element_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "background-color: aquamarine; border: 2px solid black;",
        )
        element.click()

    def enter_text(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "background-color: aquamarine; border: 2px solid black;",
        )
        element.send_keys(text)

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        assert web_element.text == element_text