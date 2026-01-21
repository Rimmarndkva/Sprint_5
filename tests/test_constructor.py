from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import ConstructorPageLocators, LoginPageLocators

def test_switch_to_sauces(driver):
    driver.get("https://stellarburgers.education-services.ru")
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    
    tab = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)
    assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

def test_switch_to_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru")
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
    
    tab = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB)
    assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

def test_switch_to_buns(driver):
    driver.get("https://stellarburgers.education-services.ru")
  
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()

    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    
    tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
    assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

def test_go_to_constructor_from_logo(driver):
    driver.get("https://stellarburgers.education-services.ru/account/profile")
  
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']|.//a[text()='Профиль']")))
    
    logo = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(ConstructorPageLocators.LOGO))
    logo.click()
    
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))