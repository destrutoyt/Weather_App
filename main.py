import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import pytz
import time
import threading
from alert_module import identify_alerts

def verifyAPI():
    try:
        city = "New York"
        api_test = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=945496a8afcbb976a61d9831f8efab72"
        response = requests.get(api_test)
        response.raise_for_status()

        if response.status_code == 200:
            messagebox.showinfo("API Verification", "API verification successful")
            getDataButton.config(state="normal")
            print("API verification passed. Program can be used")
        else:
            messagebox.showerror("API Verification", "API verification was unsuccessful! \nCheck API!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("API Verification", "There was a request issue with your API \nCheck API!")
        print(e)


def getWeatherData():
    # Get timezone
    city = 'Poland'
    name.config(text="Weather Details")
    alert_name.config(text="Alerts")
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
    print("AIQ:", aiq)

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

    global time_thread
    time_thread = threading.Thread(target=update_time)
    time_thread.daemon = True
    time_thread.start()
def update_time():
    while True:
        timezone = pytz.timezone('Europe/Rome')
        current_time = datetime.now(timezone).time()
        time_string = current_time.strftime("%H:%M:%S")
        clock.config(text=time_string,state="normal")
        time.sleep(1)  # Update time every second


# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("900x400+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# Images / Canvas
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

details_image = PhotoImage(file="images/Detailed_Canva.png")
Label(root, image=details_image, bg="#57adff").place(x=80, y=55)

# Labels
label1 = Label(root, text="Temperature", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label1.place(x=95, y=75)

label2 = Label(root, text="Humidity", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label2.place(x=95, y=110)

label3 = Label(root, text="Pressure", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label3.place(x=95, y=145)

label4 = Label(root, text="Wind Speed", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label4.place(x=95, y=180)

label5 = Label(root, text="Max Temp", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label5.place(x=95, y=215)

label6 = Label(root, text="Min Temp", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label6.place(x=95, y=250)

label7 = Label(root, text="Air Quality", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label7.place(x=95, y=285)

label8 = Label(root, text="Visibility", font=('Lucida Sans', 10, 'bold'), fg="white", bg="#57adff")
label8.place(x=95, y=320)

t = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
t.place(x=220, y=75)

c = Labelc = Label(font=('Lucida Sans', 12, 'bold'), fg="lime", bg="#57adff")  # CONDITION
c.place(x=375, y=200)

h = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
h.place(x=220, y=110)

p = Label(font=('Lucida Sans', 10, 'bold'), fg="black", bg='#57adff')
p.place(x=220, y=145)

w = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
w.place(x=220, y=180)

max_t = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
max_t.place(x=220, y=215)

min_t = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
min_t.place(x=220, y=250)

a_q = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
a_q.place(x=220, y=285)

v = Label(font=('Lucida Sans', 10, 'bold'), fg="white", bg='#57adff')
v.place(x=220, y=320)

# WEATHER LOGO
weather_label = Label(root, bg='#57adff')
weather_label.place(x=415, y=120)

name_location = Label(font=('Lucida Sans', 15, 'bold'), fg="white", bg="#57adff")
name_location.place(x=310, y=10)

# Buttons
verifyAPIButton = Button(root, text="Verify API", font=('Lucida Sans', 10, 'bold'), fg="green", borderwidth=0,
                         cursor="hand2", command=verifyAPI)
verifyAPIButton.place(x=360, y=300)

getDataButton = Button(root, text="GET DATA", font=('Lucida Sans', 10, 'bold'), borderwidth=0, cursor="hand2",
                       command=getWeatherData, state="disabled")
getDataButton.place(x=480, y=300)
# Other
name = Label(root, font=("Lucida Sans", 12, 'bold'), fg="white", bg="#57adff")
name.place(x=115, y=360)

#Alert List
alert_list = tk.Listbox(root, font=("Helvetica", 8,'bold'), height=10, width=47, bg='orange')
alert_list.place(x=585, y=120)

alert_name = Label(root, font=("Lucida Sans", 12, 'bold'), fg="white", bg="#57adff")
alert_name.place(x=700, y=360)
# Time
clock = Label(root, font=("Helvetica", 11, 'bold'), fg="white", bg="#57adff")
clock.place(x=425, y=220)

root.mainloop()
