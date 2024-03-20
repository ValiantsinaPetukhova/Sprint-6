import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    @allure.step('Создаем заказ, передаем набор тестовых данных')
    def set_order(self,  name, last_name, address, metro_station_one_locator,  phone_number, rent_chose_date_locator,
                  rental_period_exact_locator, scooter_colour_locator, comment):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PAGE_PERSONAL_DATA_LOCATOR))
        self.send_text_to_the_element(OrderPageLocators.NAME_INPUT_LOCATOR, name)
        self.send_text_to_the_element(OrderPageLocators.LAST_NAME_INPUT_LOCATOR, last_name)
        self.send_text_to_the_element(OrderPageLocators.ADDRESS_INPUT_LOCATOR, address)
        self.click_to_element_with_wait(OrderPageLocators.METRO_STATION_LOCATOR)
        self.click_to_element_with_wait(metro_station_one_locator)

        self.send_text_to_the_element(OrderPageLocators.PHONE_NUMBER_LOCATOR, phone_number)
        self.click_to_element_with_wait(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PAGE_RENT_INFO_LOCATOR))
        self.click_to_element_with_wait(OrderPageLocators.RENT_DATE_LOCATOR)
        self.click_to_element_with_wait(rent_chose_date_locator)
        self.click_to_element_with_wait(OrderPageLocators.RENTAL_PERIOD_LOCATOR)
        self.click_to_element_with_wait(rental_period_exact_locator)
        self.click_to_element_with_wait(scooter_colour_locator)
        self.send_text_to_the_element(OrderPageLocators.COMMENT_INPUT_LOCATOR, comment)
        self.click_to_element_with_wait(OrderPageLocators.ORDER_BUTTON_FINAL_LOCATOR)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.CONFIRMATION_FORM_LOCATOR))
        self.click_to_element_with_wait(OrderPageLocators.CONFIRMATION_BUTTON_LOCATOR)

    @allure.step('Проверяем, что заказ успешно создан')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_PLACED_LOCATOR)




