from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_PAGE_PERSONAL_DATA_LOCATOR = By.XPATH, '//div[contains(text(), "Для кого самокат")]'
    NAME_INPUT_LOCATOR = By.XPATH, '//*[@placeholder = "* Имя"]'
    LAST_NAME_INPUT_LOCATOR = By.XPATH, '//*[@placeholder = "* Фамилия"]'
    ADDRESS_INPUT_LOCATOR = By.XPATH, '//*[@placeholder = "* Адрес: куда привезти заказ"]'
    METRO_STATION_LOCATOR = By.XPATH, '//*[@placeholder = "* Станция метро"]'
    METRO_STATION_ONE_LOCATOR = By.XPATH, '//li[@class="select-search__row" and @role="menuitem" and @data-value="3"]'
    METRO_STATION_TWO_LOCATOR = By.XPATH, '//li[@class="select-search__row" and @role="menuitem" and @data-value="7"]'
    PHONE_NUMBER_LOCATOR = By.XPATH, '//*[@placeholder = "* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON_LOCATOR = By.XPATH, '//button[text()="Далее"]'
    ORDER_PAGE_RENT_INFO_LOCATOR = By.XPATH, '//div[text()="Про аренду"]'
    RENT_DATE_LOCATOR = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    RENT_NEXT_DATE_LOCATOR = By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]/following::div[contains(@class, "react-datepicker__day")][1]'
    RENT_DAY_AFTER_TOMORROW_LOCATOR = By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]/following::div[contains(@class, "react-datepicker__day")][2]'
    RENTAL_PERIOD_LOCATOR = By.CSS_SELECTOR, '.Dropdown-placeholder'
    RENTAL_PERIOD_DAY_LOCATOR = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    RENTAL_PERIOD_THREE_DAYS_LOCATOR = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"
    COLOUR_BLACK_LOCATOR = By.ID, 'black'
    COLOUR_GREY_LOCATOR = By.ID, 'grey'
    COMMENT_INPUT_LOCATOR = By.XPATH, '//*[@placeholder = "Комментарий для курьера"]'
    ORDER_BUTTON_FINAL_LOCATOR = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]'
    CONFIRMATION_FORM_LOCATOR = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    CONFIRMATION_BUTTON_LOCATOR = By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text() = "Да"]'
    ORDER_PLACED_LOCATOR = By.XPATH, '//div[text()="Заказ оформлен"]'
    CHECK_STATUS_LOCATOR = By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text() = "Посмотреть статус"]'







