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
    value = 0
    while value < 3:
        input_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, SEARCH_INPUT)))
        search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON)))
        ActionChains(driver).move_to_element(input_bar).click().perform()
        ActionChains(driver).send_keys(input_city(value)).perform()
        ActionChains(driver).move_to_element(search_button).double_click().perform()
        value += 1
        time.sleep(1)
        fetch_days()


def input_city(value):
    cities = [city1, city2, city3]
    time.sleep(1)
    return cities[value]


def fetch_days():
    day_number = 1
    while day_number < 4:
        day_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="daylink-{day_number}"]/div[2]')))
        day = list(day_element.get_attribute('aria-label').split(" "))
        print(day[0])
        day_number += 1


# Kaunas
# // *[ @ id = "daylink-1"] / div[2] / div / span[1] / text()[1]
# // *[ @ id = "daylink-2"] / div[2] / div / span[1] / text()[1]
# // *[ @ id = "daylink-3"] / div[2] / div / span[1] / text()[1]
# New York
# // *[ @ id = "daylink-1"] / div[2] / div / span[1] / text()[1]
# // *[ @ id = "daylink-2"] / div[2] / div / span[1] / text()[1]
# // *[ @ id = "daylink-3"] / div[2] / div / span[1] / text()[1]

def close_windows():
    driver.close()
    driver.quit()
    print('Test completed')
