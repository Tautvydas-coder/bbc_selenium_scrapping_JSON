from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_service.activate_drivers import driver_service
from resources.variables import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = driver_service()
driver.get('chrome://settings/clearBrowserData')


def open_website():
    driver.maximize_window()
    driver.get(URL)
    driver.implicitly_wait(5)


def accept_personal_data():
    data = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="weather-home"]/body/div[9]/div[2]/div[1]/div[2]/div[2]/button[1]')))
    ActionChains(driver).move_to_element(data).click(data).perform()


def accept_cookies():
    cookies = driver.find_element(By.ID, 'bbccookies-continue-button')
    ActionChains(driver).move_to_element(cookies).click(cookies).perform()
