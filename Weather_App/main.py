import requests
import json

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
city = input("Enter City: ")
url = f"http://api.weatherapi.com/v1/current.json?key=0349eed8afcb4e3a95f113008252104&q={city}"

response = requests.get(url)
# print(response.text) # op comes in str type so need to convert dict
weather_dict = json.loads(response.text)

# print(weather_dict["current"]["temp_c"])
print(f"""Temperature in {city}: {weather_dict['current']['temp_c']}°C
 and condition in {city}: {weather_dict["current"]['condition']['text']}""")
# Speak the text
engine.say(f"""Temperature in {city}: {weather_dict['current']['temp_c']}°C
     and condition in {city}: {weather_dict['current']['condition']['text']}
""")
engine.say(f"condition in {city}: {weather_dict["current"]['condition']['text']}")
# Wait until speaking is finished
engine.runAndWait()





#
# op : - C:\Python313\python.exe D:\PYTHON\Python_POC\Python_projects\Weather_App\main.py
# Enter City: pune
# Temperature in pune: 37.4°C
#

# http://api.weatherapi.com/v1/current.json?key=0349eed8afcb4e3a95f113008252104&q=nasik