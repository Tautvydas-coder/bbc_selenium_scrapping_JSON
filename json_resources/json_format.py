import json
from resources.variables import *
from selenium_resources.parser import *
from main import *

def dictionary(listas_temp):
    dict = {
        'city':
            {
                f'{city1}':
                    {
                        'DayOfTheWeek':
                            {
                                f'{fetch_days()[0][0]}':
                                    {
                                        'temperature': f'{listas_temp[0][0]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[0][1]}':
                                    {
                                        'temperature': f'{listas_temp[0][1]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[0][2]}':
                                    {
                                        'temperature': f'{listas_temp[0][2]}',
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
                                        'temperature': f'{listas_temp[1][0]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[1][1]}':
                                    {
                                        'temperature': f'{listas_temp[1][1]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[1][2]}':
                                    {
                                        'temperature': f'{listas_temp[1][2]}',
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
                                        'temperature': f'{listas_temp[2][0]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[2][1]}':
                                    {
                                        'temperature': f'{listas_temp[2][1]}',
                                        'description': 'Sunny and a gentle breeze'
                                    },
                                f'{fetch_days()[2][2]}':
                                    {
                                        'temperature': f'{listas_temp[2][2]}',
                                        'description': 'Sunny and a gentle breeze'
                                    }
                            }
                    }
            }
    }
    # print(dict['city']['Vilnius']['DayOfTheWeek']['Tuesday']['description'])
    print(dict)
