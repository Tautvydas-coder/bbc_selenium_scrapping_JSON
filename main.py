from selenium_resources.parser import *
from json_resources.json_format import *

# TODO all info should be in the Dict
# TODO save all info in the JSON file (e.g. info->weather_chal.txt)

if __name__ == '__main__':
    open_website()
    accept_personal_data()
    accept_cookies()
    search_bar()
    list = search_bar()
    print(list)
    # input_city(value=0)
    # fetch_days()
    # temperatures()
    dictionary(list)
    close_windows()
