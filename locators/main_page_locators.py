from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id = "accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id = "accordion__panel-{}"]'
    ORDER_BUTTON_MIDDLE = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]'
    HOME_PAGE_LOCATOR = By.CLASS_NAME, 'Home_HomePage__ZXKIX'
    THIRD_PARD_OF_PAGE_LOCATOR = By.CLASS_NAME, 'Home_ThirdPart__LSTEE'
