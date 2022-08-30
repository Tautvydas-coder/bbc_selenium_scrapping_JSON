import json
from resources.variables import *
dict = {
    'city':
        {
            f'{city1}':
                {
                    'DayOfTheWeek':
                        {
                            'day1':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day2':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day3':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                }
                        }
                },
            f'{city2}':
                {
                    'DayOfTheWeek':
                        {
                            'day1':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day2':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day3':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                }
                        }
                },
            f'{city3}':
                {
                    'DayOfTheWeek':
                        {
                            'day1':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day2':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'day3':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                }
                        }
                }
        }
}

# print(dict['city']['Vilnius']['DayOfTheWeek']['Tuesday']['description'])
print(dict)

