import json
from resources.variables import *
from selenium_resources.parser import *


def dictionary():
    dict = {
        'city':
            {
                f'{city1}':
                    {
                        'DayOfTheWeek':
                            {
                                f'{fetch_days()[0][0]}':
                                    {
                                        'temperature': f'{fetch_temperature()[0][0]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[0][1]}':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[0][2]}':
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
                                f'{fetch_days()[1][0]}':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[1][1]}':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[1][2]}':
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
                                f'{fetch_days()[2][0]}':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[2][1]}':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[2][2]}':
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
