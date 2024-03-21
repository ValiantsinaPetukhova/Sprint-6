import allure
from pages.header_page import HeaderPage


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу по клику на логотип самоката')
    def test_switching_to_main_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.acception_cookies()
        header_page.switch_to_main_page()
        assert header_page.check_main_page_is_visible()

    @allure.title('Проверка перехода на страницу Яндекс Дзена по клику на логотип Яндекса')
    def test_switch_to_dzen_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.acception_cookies()
        header_page.click_to_yandex_logo()
        header_page.go_to_the_new_window()
        assert header_page.check_dzen_page_is_open()