from webdriver_service.activate_drivers import driver_service
from resources.variables import *

driver = driver_service()
driver.get('chrome://settings/clearBrowserData')


def open_website():
    driver.implicitly_wait(5)
    driver.get(URL)
    driver.maximize_window()
