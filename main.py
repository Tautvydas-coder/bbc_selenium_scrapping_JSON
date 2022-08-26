from selenium_resources.parser import *

# TODO input in the field three different cities, separate
# TODO grab nearest 3 days temperature
# TODO all info should be in the Dict
# TODO save all info in the JSON file (e.g. info->weather_chal.txt)

if __name__ == '__main__':
    open_website()
    accept_personal_data()
    accept_cookies()
    search_bar()
    input_city()
