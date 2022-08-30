import json

dict = {
    'city':
        {
            'Vilnius':
                {
                    'DayOfTheWeek':
                        {
                            'Monday':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                },
                            'Tuesday':
                                {
                                    'temperature': '23',
                                    'description': 'Sunny and a gentle breeze'
                                }
                        }
                }
        }
}

print(dict['city']['Vilnius']['DayOfTheWeek']['Tuesday']['description'])

