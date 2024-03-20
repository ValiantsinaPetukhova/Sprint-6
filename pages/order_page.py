import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    @allure.step('Создаем заказ, передаем набор тестовых данных')
    def set_order(self, personal_info_locator, name_locator, name, last_name_locator, last_name,
                  address_locator, address, metro_station_locator, metro_station_one_locator, phone_number_locator, phone_number,
                  next_button_locator, rent_info_locator, rent_date_locator, rent_chose_date_locator,
                  rental_period_locator, rental_period_exact_locator, scooter_colour_locator, comment_locator, comment,
                  order_button_fin_locator, confirmation_form_locator, confirm_button_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(personal_info_locator))
        self.send_text_to_the_element(name_locator, name)
        self.send_text_to_the_element(last_name_locator, last_name)
        self.send_text_to_the_element(address_locator, address)
        self.click_to_element_with_wait(metro_station_locator)
        self.click_to_element_with_wait(metro_station_one_locator)

        self.send_text_to_the_element(phone_number_locator, phone_number)
        self.click_to_element_with_wait(next_button_locator)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(rent_info_locator))
        self.click_to_element_with_wait(rent_date_locator)
        self.click_to_element_with_wait(rent_chose_date_locator)
        self.click_to_element_with_wait(rental_period_locator)
        self.click_to_element_with_wait(rental_period_exact_locator)
        self.click_to_element_with_wait(scooter_colour_locator)
        self.send_text_to_the_element(comment_locator, comment)
        self.click_to_element_with_wait(order_button_fin_locator)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(confirmation_form_locator))
        self.click_to_element_with_wait(confirm_button_locator)

    @allure.step('Проверяем, что заказ успешно создан')
    def check_order(self, order_place_locator):
        return self.get_text_from_element(order_place_locator)



