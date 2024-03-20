import allure

from data import TestData
from locators.base_page_locators import BasePageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка создания заказа через кнопку "Заказать" вверху страницы')
    def test_order_scooter_from_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies(BasePageLocators.COOKIES_BUTTON)
        main_page.click_to_element_with_wait(HeaderPageLocators.ORDER_BUTTON_TOP)
        order_page = OrderPage(driver)
        order_page.set_order(OrderPageLocators.ORDER_PAGE_PERSONAL_DATA_LOCATOR,
                             OrderPageLocators.NAME_INPUT_LOCATOR, TestData.NAME_1,
                             OrderPageLocators.LAST_NAME_INPUT_LOCATOR, TestData.LAST_NAME_1,
                             OrderPageLocators.ADDRESS_INPUT_LOCATOR, TestData.ADDRESS_1,
                             OrderPageLocators.METRO_STATION_LOCATOR, OrderPageLocators.METRO_STATION_ONE_LOCATOR,
                             OrderPageLocators.PHONE_NUMBER_LOCATOR, TestData.PHONE_1,
                             OrderPageLocators.NEXT_BUTTON_LOCATOR,
                             OrderPageLocators.ORDER_PAGE_RENT_INFO_LOCATOR,
                             OrderPageLocators.RENT_DATE_LOCATOR, OrderPageLocators.RENT_NEXT_DATE_LOCATOR,
                             OrderPageLocators.RENTAL_PERIOD_LOCATOR, OrderPageLocators.RENTAL_PERIOD_DAY_LOCATOR,
                             OrderPageLocators.COLOUR_GREY_LOCATOR,
                             OrderPageLocators.COMMENT_INPUT_LOCATOR, TestData.COMMENT_1,
                             OrderPageLocators.ORDER_BUTTON_FINAL_LOCATOR, OrderPageLocators.CONFIRMATION_FORM_LOCATOR,
                             OrderPageLocators.CONFIRMATION_BUTTON_LOCATOR)
        assert 'Заказ оформлен' in order_page.check_order(OrderPageLocators.ORDER_PLACED_LOCATOR)

    @allure.title('Проверка создания заказа через кнопку "Заказать" в середине страницы')
    def test_order_scooter_from_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies(BasePageLocators.COOKIES_BUTTON)
        main_page.scroll_to_the_element(MainPageLocators.THIRD_PARD_OF_PAGE_LOCATOR)
        main_page.click_to_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)
        order_page = OrderPage(driver)
        order_page.set_order(OrderPageLocators.ORDER_PAGE_PERSONAL_DATA_LOCATOR,
                             OrderPageLocators.NAME_INPUT_LOCATOR, TestData.NAME_2,
                             OrderPageLocators.LAST_NAME_INPUT_LOCATOR, TestData.LAST_NAME_2,
                             OrderPageLocators.ADDRESS_INPUT_LOCATOR, TestData.ADDRESS_2,
                             OrderPageLocators.METRO_STATION_LOCATOR, OrderPageLocators.METRO_STATION_TWO_LOCATOR,
                             OrderPageLocators.PHONE_NUMBER_LOCATOR, TestData.PHONE_2,
                             OrderPageLocators.NEXT_BUTTON_LOCATOR,
                             OrderPageLocators.ORDER_PAGE_RENT_INFO_LOCATOR,
                             OrderPageLocators.RENT_DATE_LOCATOR, OrderPageLocators.RENT_DAY_AFTER_TOMORROW_LOCATOR,
                             OrderPageLocators.RENTAL_PERIOD_LOCATOR, OrderPageLocators.RENTAL_PERIOD_THREE_DAYS_LOCATOR,
                             OrderPageLocators.COLOUR_BLACK_LOCATOR,
                             OrderPageLocators.COMMENT_INPUT_LOCATOR, TestData.COMMENT_2,
                             OrderPageLocators.ORDER_BUTTON_FINAL_LOCATOR, OrderPageLocators.CONFIRMATION_FORM_LOCATOR,
                             OrderPageLocators.CONFIRMATION_BUTTON_LOCATOR)
        assert 'Заказ оформлен' in order_page.check_order(OrderPageLocators.ORDER_PLACED_LOCATOR)