import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Проверяем, что по клику на логотип самоката переходит на главную страницу')
    def switch_to_main_page(self, locator_order, locator_scooter):
        self.click_to_element_with_wait(locator_order)
        self.click_to_element_with_wait(locator_scooter)



