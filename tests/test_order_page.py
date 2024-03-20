import allure

from data import TestData
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка создания заказа через кнопку "Заказать" вверху страницы')
    def test_order_scooter_from_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_to_the_order_top_button()
        order_page = OrderPage(driver)
        order_page.set_order(TestData.NAME_1, TestData.LAST_NAME_1, TestData.ADDRESS_1,
                             OrderPageLocators.METRO_STATION_ONE_LOCATOR, TestData.PHONE_1,
                             OrderPageLocators.RENT_NEXT_DATE_LOCATOR,
                             OrderPageLocators.RENTAL_PERIOD_DAY_LOCATOR,
                             OrderPageLocators.COLOUR_GREY_LOCATOR, TestData.COMMENT_1)
        assert 'Заказ оформлен' in order_page.check_order()

    @allure.title('Проверка создания заказа через кнопку "Заказать" в середине страницы')
    def test_order_scooter_from_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_to_the_middle_of_the_page()
        main_page.click_to_the_middle_order_button()
        order_page = OrderPage(driver)
        order_page.set_order(TestData.NAME_2, TestData.LAST_NAME_2, TestData.ADDRESS_2,
                              OrderPageLocators.METRO_STATION_TWO_LOCATOR, TestData.PHONE_2,
                              OrderPageLocators.RENT_DAY_AFTER_TOMORROW_LOCATOR,
                              OrderPageLocators.RENTAL_PERIOD_THREE_DAYS_LOCATOR,
                              OrderPageLocators.COLOUR_BLACK_LOCATOR, TestData.COMMENT_2)
        assert 'Заказ оформлен' in order_page.check_order()

