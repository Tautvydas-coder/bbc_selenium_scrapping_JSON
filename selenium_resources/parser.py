import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_service.activate_drivers import driver_service
from resources.variables import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = driver_service()
driver.get(CLEAR_HISTORY)


def open_website():
    driver.maximize_window()
    driver.get(URL)
    driver.implicitly_wait(5)


def accept_personal_data():
    data = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, ACCEPT_PERSONAL_DATA)))
    ActionChains(driver).move_to_element(data).click(data).perform()


def accept_cookies():
    cookies = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, ACCEPT_COOKIES)))
    ActionChains(driver).move_to_element(cookies).click(cookies).perform()


def search_bar():
    temp = 0
    while temp<3:
        input_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, SEARCH_INPUT)))
        search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON)))
        ActionChains(driver).move_to_element(input_bar).click().perform()
        ActionChains(driver).send_keys(input_city(temp)).perform()
        ActionChains(driver).move_to_element(search_button).double_click().perform()
        time.sleep(1)
        temp += 1


def input_city(temp):
    cities = [city1, city2, city3]
    return cities[temp]


def close_windows():
    driver.close()
    driver.quit()
    print('Test completed')
