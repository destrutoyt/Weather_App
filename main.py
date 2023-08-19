import requests
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import pytz

def verifyAPI():
    try:
        city="New York"
        api_test="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=945496a8afcbb976a61d9831f8efab72" #ONLY FOR PERSONAL USE!
        response = requests.get(api_test)
        response.raise_for_status()

        if response.status_code == 200:
            messagebox.showinfo("API Verification", "API verification successful")
            getDataButton.config(state="normal")
        else:
            messagebox.showerror("API Verification", "API verification was unsuccessful! \nCheck API!")
    except requests.exceptions.RequestException:
        messagebox.showerror("API Verification", "There was a request issue with your API \nCheck API!")
def getWeatherData():
    #Get timezone
    city='Carteret'
    timezone = pytz.timezone('Europe/Rome')
    current_time = datetime.now(timezone).time()
    time_string = current_time
    time_without_fraction = time_string.replace(microsecond=0)
    clock.config(text=time_without_fraction)
    name.config(text="CURRENT WEATHER")
    root.after(1000,getWeatherData)
    name_country.config(text=f"You are getting data from: {city}")

    #Get weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=945496a8afcbb976a61d9831f8efab72"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,'°'))
    w.config(text=wind)
    h.config(text=humidity)
    p.config(text=pressure)
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

#GUI
root = Tk()
root.title("Weather App")
root.geometry("900x400+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

#icons
image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

test = PhotoImage(file="images/Rounded Rectangle 2.png")
Label(root,image=test,bg="#57adff").place(x=125,y=120)

#label
label1=Label(root,text="Temperature",font=('Lucida Sans',11,'bold'),fg="white",bg="#2E81B2")
label1.place(x=180,y=280)

label2=Label(root,text="Humidity",font=('Lucida Sans',11,'bold'),fg="white",bg="#2E81B2")
label2.place(x=350,y=280)

label3=Label(root,text="Pressure",font=('Lucida Sans',11,'bold'),fg="white",bg="#2E81B2")
label3.place(x=500,y=280)

label4=Label(root,text="Wind Speed",font=('Lucida Sans',11,'bold'),fg="white",bg="#57adff")
label4.place(x=650,y=280)

t=Label(font=('Lucida Sans',11,'bold'),fg="yellow",bg='#57adff')
t.place(x=214,y=310)

c=Labelc=Label(font=('Lucida Sans',11,'bold'),fg="lime",bg="#57adff")
c.place(x=200,y=160)

h=Label(font=('Lucida Sans',11,'bold'),fg="cyan",bg='#57adff')
h.place(x=372,y=310)

p=Label(font=('Lucida Sans',11,'bold'),fg="black",bg='#57adff')
p.place(x=510,y=310)

w=Label(font=('Lucida Sans',11,'bold'),fg="white",bg='#57adff')
w.place(x=678,y=310)

weather_label = Label(root,bg='#57adff')
weather_label.place(x=100, y=100)

name_country=Label(font=('Lucida Sans',15,'bold'),fg="white",bg="#57adff")
name_country.place(x=280,y=50)

#Buttons
verifyAPIButton = Button(root, text="Verify API", font=('Lucida Sans', 10, 'bold'),fg="green", borderwidth=0, cursor="hand2", command=verifyAPI)
verifyAPIButton.place(x=360, y=200)

getDataButton = Button(root, text="GET DATA", font=('Lucida Sans', 10, 'bold'), borderwidth=0, cursor="hand2", command=getWeatherData, state="disabled")
getDataButton.place(x=480, y=200)
#time
name=Label(root,font=("Lucida Sans", 12,'bold'),fg="#C5F5DA",bg="#57adff")
name.place(x=200,y=100)
clock=Label(root,font=("Helvetica", 11,'bold'),fg="white",bg="#57adff")
clock.place(x=200,y=130)


root.mainloop()
