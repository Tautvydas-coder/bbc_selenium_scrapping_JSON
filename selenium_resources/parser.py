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
    days_weather_full_info = []
    while value < 3:
        input_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, SEARCH_INPUT)))
        search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON)))
        ActionChains(driver).move_to_element(input_bar).click().perform()
        ActionChains(driver).send_keys(input_city(value)).perform()
        ActionChains(driver).move_to_element(search_button).double_click().perform()
        value += 1
        time.sleep(1)

        wather_info = fetch_weather_information()
        days_weather_full_info.append(wather_info)

    return days_weather_full_info


def input_city(value):
    cities = [city1, city2, city3]
    time.sleep(1)
    return cities[value]


def fetch_weather_information():
    index = 1
    day_weather_info = []
    days_weather_full_info = []
    while index < 4:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="daylink-{index}"]'))).click()

        day_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="daylink-{index}"]/div[2]')))
        day = list(day_element.get_attribute('aria-label').split(" "))[0]
        print(day)

        temperature_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            f'#daylink-{index} > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c')))
        temperature = temperature_element.text
        print(temperature)

        description_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            f'//*[@id="daylink-{index}"]/div[4]/div[2]/div')))
        description = description_element.text
        print(description)
        index += 1

        day_weather_info.append(day)
        day_weather_info.append(temperature)
        day_weather_info.append(description)
        print(day_weather_info)

    return day_weather_info

def close_windows():
    driver.close()
    driver.quit()
    print('Test completed')
