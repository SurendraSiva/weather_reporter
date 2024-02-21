import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
def get_info(city):
    key='04c628cba30b53746a53a3c4fbd61d8f'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': key, 'units': 'metric'}
    #requets apperas like https://api.openweathermap.org/data/2.5/weather?q=city&appid=key&units=metric
    try:
        response=requests.get(base_url,params=params)
        data=response.json()
        t=data['main']['temp']
        ft=data['main']['feels_like']
        d=data['weather'][0]['description']
        p=data['main']['pressure']
        h=data['main']['humidity']
        s=data['wind']['speed']
        l1.config(text=f'Temperature                  : {t}°C')
        l2.config(text=f'Feels like temperature  : {ft}°C')
        l3.config(text=f'Weather Description     : {d}')
        l4.config(text=f'Atmospheric Pressure   : {p} hPa')
        l5.config(text=f'Humidity                       : {h}%')
        l6.config(text=f'Windspeed                    : {s} m/s')
    except Exception as e:
        messagebox.showerror('Error','Unable to fetch weather details')
    
frame=tk.Tk()
frame.title('Weather Reporter')
bg=PhotoImage(file='weather_back.jpg')
img=Label(frame,image=bg)
img.place(relheight=1,relwidth=1)
l=Label(frame,text='Enter the city:',font=('Times',16,'italic'),background='#7a897b')
l.place(x=40,y=150)
l1=Label(frame,text='Temperature                  : ',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l1.place(x=70,y=260)
l2=Label(frame,text='Feels like temperature  :',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l2.place(x=70,y=310)
l3=Label(frame,text='Weather Description     :',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l3.place(x=70,y=360)
l4=Label(frame,text='Atmospheric Pressure   :',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l4.place(x=70,y=410)
l5=Label(frame,text='Humidity                       :',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l5.place(x=70,y=460)
l6=Label(frame,text='Windspeed                    :',font=('Times',16,'italic'),width=40,anchor=W,background='#dadad3')
l6.place(x=70,y=510)
e1=Entry(frame,font=('Times',16,'italic'),width=30,background='#dadad3')
e1.place(x=200,y=150)
b=Button(frame,text="Get weather Information",font=('Times',15,'italic'),command=lambda:get_info(e1.get()),background='#5c8a9c')
b.place(x=200,y=200)
frame.geometry('600x700+50+50')
frame.mainloop()