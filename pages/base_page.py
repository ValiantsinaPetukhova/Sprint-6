import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся с куками')
    def accept_cookies(self, locator):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator)))
            cookie_button.click()
        except:
            pass

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_text_to_the_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def format_locators(self, locator_raw, num):
        method, locator = locator_raw
        locator = locator.format(num)
        return (method, locator)

    def go_to_the_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Проверяем видимость элемента')
    def check_visibility_of_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
