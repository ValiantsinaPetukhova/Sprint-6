import allure
import pytest
from data import TestData
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка создания заказа через кнопку "Заказать" вверху страницы и в середине страницы')
    @pytest.mark.parametrize("test_data", [
        (HeaderPageLocators.ORDER_BUTTON_TOP, TestData.NAME_1, TestData.LAST_NAME_1, TestData.ADDRESS_1,
         OrderPageLocators.METRO_STATION_ONE_LOCATOR, TestData.PHONE_1,
         OrderPageLocators.RENT_NEXT_DATE_LOCATOR, OrderPageLocators.RENTAL_PERIOD_DAY_LOCATOR,
         OrderPageLocators.COLOUR_GREY_LOCATOR, TestData.COMMENT_1),
        (MainPageLocators.ORDER_BUTTON_MIDDLE, TestData.NAME_2, TestData.LAST_NAME_2, TestData.ADDRESS_2,
         OrderPageLocators.METRO_STATION_TWO_LOCATOR, TestData.PHONE_2,
         OrderPageLocators.RENT_DAY_AFTER_TOMORROW_LOCATOR,
         OrderPageLocators.RENTAL_PERIOD_THREE_DAYS_LOCATOR,
         OrderPageLocators.COLOUR_BLACK_LOCATOR, TestData.COMMENT_2)
    ]
                             )
    def test_order_success_scenario(self, driver, test_data):
        main_page = MainPage(driver)
        main_page.acception_cookies()
        order_page = OrderPage(driver)
        order_page.set_order(*test_data)
        assert 'Заказ оформлен' in order_page.check_order()
