from selenium.webdriver.common.by import By


class BasePageLocators:
    DZEN_HEADER_LOCATOR = By.XPATH, '//header[@id ="dzen-header"]'
    COOKIES_BUTTON = By.CLASS_NAME, 'App_CookieButton__3cvqF'
