import allure

from locators.base_page_locators import BasePageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.header_page import HeaderPage


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу по клику на логотип самоката')
    def test_switching_to_main_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.accept_cookies(BasePageLocators.COOKIES_BUTTON)
        header_page.switch_to_main_page(HeaderPageLocators.ORDER_BUTTON_TOP, HeaderPageLocators.SCOOTER_LOGO)
        assert header_page.check_visibility_of_element(MainPageLocators.HOME_PAGE_LOCATOR)

    @allure.title('Проверка перехода на страницу Яндекс Дзена по клику на логотип Яндекса')
    def test_switch_to_dzen_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.accept_cookies(BasePageLocators.COOKIES_BUTTON)
        header_page.click_to_element_with_wait(HeaderPageLocators.YANDEX_LOGO)
        header_page.go_to_the_new_window()
        assert header_page.check_visibility_of_element(BasePageLocators.DZEN_HEADER_LOCATOR)