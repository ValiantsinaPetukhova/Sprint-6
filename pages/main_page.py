import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Форматируем локаторы в зависимости от номера вопроса и получает текст ответа')
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element_with_wait(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def scroll_to_the_middle_of_the_page(self):
        self.scroll_to_the_element(MainPageLocators.THIRD_PARD_OF_PAGE_LOCATOR)

    def click_to_the_order_top_button(self):
        self.click_to_element_with_wait(HeaderPageLocators.ORDER_BUTTON_TOP)

    def click_to_the_middle_order_button(self):
        self.click_to_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)