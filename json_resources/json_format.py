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
                                f'{temperatur_list[1][0]}':
                                    {
                                        'temperature': f'{temperatur_list[1][1]}',
                                        'description': f'{temperatur_list[1][2]}'
                                    },
                                f'{temperatur_list[1][3]}':
                                    {
                                        'temperature': f'{temperatur_list[1][4]}',
                                        'description': f'{temperatur_list[1][5]}'
                                    },
                                f'{temperatur_list[0][6]}':
                                    {
                                        'temperature': f'{temperatur_list[1][7]}',
                                        'description': f'{temperatur_list[1][8]}'
                                    }
                            }
                    },
                f'{city3}':
                    {
                        'DayOfTheWeek':
                            {
                                f'{temperatur_list[2][0]}':
                                    {
                                        'temperature': f'{temperatur_list[2][1]}',
                                        'description': f'{temperatur_list[2][2]}'
                                    },
                                f'{temperatur_list[2][3]}':
                                    {
                                        'temperature': f'{temperatur_list[2][4]}',
                                        'description': f'{temperatur_list[2][5]}'
                                    },
                                f'{temperatur_list[2][6]}':
                                    {
                                        'temperature': f'{temperatur_list[2][7]}',
                                        'description': f'{temperatur_list[2][8]}'
                                    }
                            }
                    }
            }
    }
    json_object = json.dumps(dict, indent=4)

    with open("output/weather_json.json", "w", encoding='utf-8', errors="xmlcharrefreplace") as data:
        data.write(json_object)

    return dict
