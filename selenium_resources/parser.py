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
    temper_full_list = []
    while value < 3:
        input_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, SEARCH_INPUT)))
        search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON)))
        ActionChains(driver).move_to_element(input_bar).click().perform()
        ActionChains(driver).send_keys(input_city(value)).perform()
        ActionChains(driver).move_to_element(search_button).double_click().perform()
        value += 1
        time.sleep(1)
        fetch_days()
        temperature = fetch_temperature()
        temper_full_list.append(temperature)
    return temper_full_list

def input_city(value):
    cities = [city1, city2, city3]
    time.sleep(1)
    return cities[value]


def fetch_days():
    day_number = 1
    days = []
    days_full_list = []
    while day_number < 4:
        day_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="daylink-{day_number}"]/div[2]')))
        day = list(day_element.get_attribute('aria-label').split(" "))[0]
        days.append(day)
        days_full_list.append(days)
        day_number += 1
    return days_full_list


def fetch_temperature():
    temp_number = 1
    one_city_temp_list = []
    while temp_number < 4:
        time.sleep(1)
        temperature_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            f'#daylink-{temp_number} > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c')))
        temperatures = temperature_element.text
        one_city_temp_list.append(temperatures)
        temp_number += 1
    return one_city_temp_list

# Tallinn
# //*[@id="daylink-1"]/div[4]/div[1]/div/div[4]/div/div[1]/span[2]/span/span[1]
# //*[@id="daylink-2"]/div[4]/div[1]/div/div[4]/div/div[1]/span[2]/span/span[1]
# //*[@id="daylink-3"]/div[4]/div[1]/div/div[4]/div/div[1]/span[2]/span/span[1]

def close_windows():
    driver.close()
    driver.quit()
    print('Test completed')
