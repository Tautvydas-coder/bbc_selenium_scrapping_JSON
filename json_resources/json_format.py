import json
from resources.variables import *
from selenium_resources.parser import *
from main import *

def dictionary(temperatur_list):
    dict = {
        'city':
            {
                f'{city1}':
                    {
                        'DayOfTheWeek':
                            {
                                f'{temperatur_list[0][0]}':
                                    {
                                        'temperature': f'{temperatur_list[0][1]}',
                                        'description': f'{temperatur_list[0][2]}'
                                    },
                                f'{temperatur_list[0][3]}':
                                    {
                                        'temperature': f'{temperatur_list[0][4]}',
                                        'description': f'{temperatur_list[0][5]}'
                                    },
                                f'{temperatur_list[0][6]}':
                                    {
                                        'temperature': f'{temperatur_list[0][7]}',
                                        'description': f'{temperatur_list[0][8]}'
                                    }
                            }
                    },
                f'{city2}':
                    {
                        'DayOfTheWeek':
                            {
                                f'test':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'testa':
                                    {
                                        'temperature':  '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'tests':
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
                                f'teste':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'testh':
                                    {
                                        'temperature': '23',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'testy':
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
