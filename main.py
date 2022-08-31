from selenium_resources.parser import *
from json_resources.json_format import *

# TODO all info should be in the Dict
# TODO save all info in the JSON file (e.g. info->weather_chal.txt)

if __name__ == '__main__':
    open_website()
    accept_personal_data()
    accept_cookies()
    listas_temp = search_bar()
    print(listas_temp)
    input_city(value=0)
    # fetch_days()
    # temperatures()
    dictionary(listas_temp)
    close_windows()
