import tkinter as tk
from tkinter import *
from API_Verification import verifyAPI
from weatherData import getWeatherData

if __name__ == '__main__':
    ver_API = verifyAPI()

    # GUI
    root = tk.Tk()
    root.title("Weather App by Miguel G.")
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
    c.place(x=352, y=200)

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

    # Weather Log
    weather_label = Label(root, bg='#57adff')
    weather_label.place(x=400, y=120)

    name_location = Label(font=('Lucida Sans', 15, 'bold'), fg="white", bg="#57adff")
    name_location.place(x=310, y=10)

    # Other
    name = Label(root, font=("Lucida Sans", 12, 'bold'), fg="white", bg="#57adff")
    name.place(x=115, y=360)

    # Alert List
    alert_list = tk.Listbox(root, font=("Helvetica", 8,'bold'), height=10, width=47, bg='orange')
    alert_list.place(x=585, y=120)

    alert_name = Label(root, font=("Lucida Sans", 12, 'bold'), fg="white", bg="#57adff")
    alert_name.place(x=700, y=360)

    # API Verification
    if ver_API:
        weather_data = getWeatherData(alert_name, name, name_location, alert_list, t, max_t, min_t, c, w, h, p, a_q, v, weather_label) # Takes ALL the labels and replaces them with expected values
        with open('log.txt', 'a') as f:
            f.write(f'\nDEBUG: Data successfully extracted!\n')
            f.close()
    else:
        error1 = Label(root, text="Error: Unable to retrieve data due to an API issue", font=('Lucida Sans', 10, 'bold'), fg="red")
        error1.place(x=290, y=10)
    
    # Refresh Data (Button appears if API works)
    if ver_API:
        refresh_buttom = Button(root, text="Refresh Data", font=('Lucida Sans', 10, 'bold'), fg="black", borderwidth=0,
                            cursor="hand2", command=weather_data)
        refresh_buttom.place(x=790, y=15)

    root.mainloop()
