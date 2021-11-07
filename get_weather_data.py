import requests, json, calendar, datetime
from os.path import join

config_file = "/home/pi/projects/weather/config.json"
weather_translation_path = "/home/pi/projects/weather/wsymb2.json"

with open(config_file, 'r') as f:
    config = json.load(f)

with open(weather_translation_path, 'r') as f:
    weather_transation = json.load(f)

smhi_url = config["smhi_url"]
lat, lon = config["lat"], config["lon"]
smhi_endpoint = config["smhi_endpoint"].format(lon, lat)

r = requests.get(smhi_url + smhi_endpoint)

response_json = json.loads(r.text)
response_json["statusCode"] = r.status_code
response_json["timeSeries"] = response_json["timeSeries"][:18] # Keep next 24h

for timestamp in response_json["timeSeries"]:
    date, time = timestamp["validTime"].split("T")  # from "2021-10-02T16:00:00Z" to "2021-10-02" and "16:00:00Z"
    time = "{}:{}".format(*time.split(":")[0:2]) # from "16:00:00Z" to "16:00"
    timestamp["time"] = time
    timestamp["date"] = date
    
    y, m, d = date.split("-")
    date = datetime.date(int(y), int(m), int(d))
    timestamp["dayName"] = calendar.day_name[date.weekday()]

    for param in timestamp["parameters"]:
        if param["name"] == "Wsymb2":
            weather_code = int(param["values"][0])
            timestamp["weather"] = weather_transation[str(weather_code)]
            timestamp["weather_code"] = weather_code
            break

data_file_path = config["data_file"]
with open(data_file_path, 'w') as f:
    json.dump(response_json, f)
