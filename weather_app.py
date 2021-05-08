import requests
import json
from tkinter import *


def weather():
	city = city_listbox.get()
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=6feed0d455440d9fd99b9d181e8b3c29".format(city)
	res = requests.get(url)
	# print(res)
	output = json.loads(res.content)
	# print(output)
	weather_status = output['weather'][0]['description']
	temperature = output['main']['temp']
	humidity = output['main']['humidity']
	wind_speed = output['wind']['speed']

	weather_status_label.configure(text = "Weather Status : "+ weather_status)
	temperature_label.configure(text = "Temperature : "+ str(temperature))
	humidity_label.configure(text = "Humidity : "+ str(humidity))
	wind_speed_label.configure(text = "Wind Speed : "+ str(wind_speed))


window = Tk()
window.title("Weather App")
window.geometry("400x350")

city_name_list = ["lucknow","delhi","bangalore","pune","mumbai","hyderabad","ahmedabad","chennai","kolkata","surat","jaipur","kanpur","nagpur","indore","thane","bhopal","patna","visakhapatnam","vadodara","ghaziabad","ludhiana","agra","nashik","faridabad","meerut","rajkot","kalyan & dombivali","varanasi","srinagar","aurangabad","dhanbad","amritsar","allahabad","coimbatore","jabalpur","gwalior","jodhpur","madurai","raipur","kota","guwahati","chandigarh","bareilly","mysore","gurgaon","jalandhar","bhubaneshwar","bikaner","noida","jamshedpur"]

city_listbox = StringVar(window)
city_listbox.set("Select the city")

option = OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=2 , column=2 , padx=150 , pady=10)

b1 = Button(window , text="Enter" , width=15 , command=weather)
b1.grid(row=5 , column=2 , padx=150)

weather_status_label = Label(window,font=("times",10,"bold"))
weather_status_label.grid(row=10 , column=2)

temperature_label = Label(window,font=("times",10,"bold"))
temperature_label.grid(row=12 , column=2)

humidity_label = Label(window,font=("times",10,"bold"))
humidity_label.grid(row=14 , column=2)

wind_speed_label = Label(window,font=("times",10,"bold"))
wind_speed_label.grid(row=16 , column=2)

window.mainloop() 