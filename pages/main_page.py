import allure

from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Форматируем локаторы в зависимости от номера вопроса и получает текст ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element_with_wait(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def acception_cookies(self):
        self.accept_cookies(CommonLocators.COOKIES_BUTTON)