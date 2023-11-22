import requests

API_KEY = "526d292effd317f35269014eb5eb66ab"

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_city():
    return input("Введите название города\n"
                 ": ")


def request(city, appid=API_KEY, lang="ru", url=URL):
    params = {
        "q": city,
        "appid": appid,
        "lang": lang
    }
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()


def main():
    print("Привет!")
    while True:
        city = get_city()
        response = request(city)
        if response:
            break
        print("Не смог найти такой город, повторите попытку(")
    data = get_data(response)
    msg = message(data, city)
    print(msg)


def get_data(response):
    data = dict()
    data['description'] = response['weather'][0]['description']
    data['temp'] = int(response['main']['temp'] - 273.15)
    data['feels'] = int(response['main']['feels_like'] - 273.15)
    data['wind'] = response['wind']['speed']
    data['pressure'] = response['main']['pressure']
    return data


def message(data, city):
    return (f"Погода в {city.capitalize()}:\n"
            f"{data['description'].capitalize()}\n"
            f"Температура: {data['temp']}C, "
            f"ощущается как {data['feels']}C\n"
            f"Скорость ветра: {data['wind']} м/c\n"
            f"Давление: {data['pressure']} мм р.с.")


main()
