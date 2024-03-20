import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Форматируем локаторы в зависимости от номера вопроса и получает текст ответа')
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element_with_wait(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

