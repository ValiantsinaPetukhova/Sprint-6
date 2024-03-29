import allure
import pytest

from data import TestData
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка поля вопросов и ответов')
    @allure.description('На странице ищем вопрос, кликаем по нему и проверяем его ответ')
    @pytest.mark.parametrize('num, result',
                             [
                                 (0, TestData.ANSWER_0),
                                 (1, TestData.ANSWER_1),
                                 (2, TestData.ANSWER_2),
                                 (3, TestData.ANSWER_3),
                                 (4, TestData.ANSWER_4),
                                 (5, TestData.ANSWER_5),
                                 (6, TestData.ANSWER_6),
                                 (7, TestData.ANSWER_7)
                             ])
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.acception_cookies()
        assert main_page.get_answer_text(num) == result
