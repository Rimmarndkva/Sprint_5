from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, ".//fieldset[1]//input")
    EMAIL_INPUT = (By.XPATH, ".//fieldset[2]//input") 
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    ERROR_PASSWORD = (By.XPATH, ".//p[contains(@class, 'input__error')]") 

class LoginPageLocators:
  
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    REGISTRATION_FORM_LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class ConstructorPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO = (By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]/a")
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/..")
    ACTIVE_TAB_CLASS = "tab_tab_type_current"