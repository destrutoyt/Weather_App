import requests
from datetime import date

def verifyAPI(): # Test API before use
    try:
        city = "New York"
        api_test = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=945496a8afcbb976a61d9831f8efab72" # Third string contains API KEY (&appid=APP_KEY)
        response = requests.get(api_test)
        response.raise_for_status()

        if response.status_code == 200:
            with open('log.txt', 'a') as f:
                f.write(f'\nDate Session: {date.today()}\n')
                f.write('DEBUG: API verification passed. Program can be used')
                f.close()
            return True

    except requests.exceptions.RequestException as e:
        with open('log.txt', 'a') as f:
            f.write(f'DEBUG (Critical): API did not work as expected: {e}\n')
            f.write(f'RECOMMENDED ACTIONS:\n1. Get a new API KEY from OpenWeatherMaps\n2. Double check that api_test is executed correctly')
            f.close()
        return False