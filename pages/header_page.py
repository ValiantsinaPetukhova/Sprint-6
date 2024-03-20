import allure

from locators.base_page_locators import BasePageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Проверяем, что по клику на логотип самоката переходит на главную страницу')
    def switch_to_main_page(self):
        self.click_to_element_with_wait(HeaderPageLocators.ORDER_BUTTON_TOP)
        self.click_to_element_with_wait(HeaderPageLocators.SCOOTER_LOGO)

    def check_main_page_is_visible(self):
        return self.check_visibility_of_element(MainPageLocators.HOME_PAGE_LOCATOR)

    def click_to_yandex_logo(self):
        self.click_to_element_with_wait(HeaderPageLocators.YANDEX_LOGO)

    def check_dzen_page_is_open(self):
        return self.check_visibility_of_element(BasePageLocators.DZEN_HEADER_LOCATOR)



