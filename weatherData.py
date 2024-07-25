import requests
from PIL import Image, ImageTk
from customAlerts import identify_alerts
import tkinter as tk

def getWeatherData(alert_name, name, name_location, alert_list, t, max_t, min_t, c, w, h, p, a_q, v, weather_label):
    city = 'New York'
    alert_name.config(text="Alerts")
    name.config(text="Weather Details")
    name_location.config(text=f"Current Weather In {city}")

    # Get weather
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=945496a8afcbb976a61d9831f8efab72"

    # Corrected air_quality_api to use the same 'city' variable
    air_quality_api = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid=945496a8afcbb976a61d9831f8efab72"

    json_data_2 = requests.get(air_quality_api).json()
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Corrected code for AIQ and Visibility
    print("JSON Data 2:")
    print(json_data_2)

    # Corrected code for AIQ and Visibility
    aiq = 'N/A'
    if 'air' in json_data_2:
        print("Found 'air' in JSON Data 2")
        if 'aqi' in json_data_2['air']:
            aiq = json_data_2['air']['aqi']
            print("Found 'aqi' in 'air' in JSON Data 2")

    visibility = json_data.get('visibility', 'N/A')

    # Print AIQ for debugging
    with open('log.txt', 'a') as f:
        f.write(f'\nDEBUG: AIQ: {aiq}')
        f.close()

    check_alerts = identify_alerts(temp, wind, aiq, visibility)
    for alert in check_alerts:
        alert_list.insert(tk.END, alert)

    if temp > 30:
        text_color = "red"
    elif 20 <= temp <= 30:
        text_color = "orange"
    elif 10 <= temp < 20:
        text_color = "lime"
    else:
        text_color = "white"
    t.config(text=(f"{temp}°"), fg=text_color)

    max_t.config(text=(max_temp, "°"))
    min_t.config(text=(min_temp, "°"))
    c.config(text=(condition, "|", "Feels", "Like", temp, '°'))
    w.config(text=wind, fg="red" if wind > 32.7 else "white")
    h.config(text=humidity)
    p.config(text=pressure)
    a_q.config(text=aiq)
    v.config(text=visibility)

    # Get weather icon code
    icon_code = json_data['weather'][0]['icon']
    # Load weather icon using Pillow
    weather_icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    response = requests.get(weather_icon_url, stream=True)

    if response.status_code == 200:
        img_data = response.content
        with open("weather_icon.png", "wb") as img_file:
            img_file.write(img_data)
        # Display weather icon using Pillow with LANCZOS resampling
        weather_icon = Image.open("weather_icon.png")
        weather_icon = weather_icon.resize((80, 80), Image.LANCZOS)
        weather_icon = ImageTk.PhotoImage(weather_icon)
        weather_label.config(image=weather_icon)
        weather_label.image = weather_icon
