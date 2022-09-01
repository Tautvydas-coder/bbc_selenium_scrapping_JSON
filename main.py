from selenium_resources.parser import *
from json_resources.json_format import *

# Remake scrapping to one function, because description only activated when day is press
# TODO get three days descriptions
# TODO all info should be in the Dict
# TODO save all info in the JSON file (e.g. info->weather_chal.txt)

if __name__ == '__main__':
    open_website()
    accept_personal_data()
    accept_cookies()
    temperatur_list = search_bar()
    print(temperatur_list)
    input_city(value=0)
    # fetch_days()
    # temperatures()
    dictionary(temperatur_list)
    close_windows()
