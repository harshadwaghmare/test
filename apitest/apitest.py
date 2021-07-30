import requests

r = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=444101&date=05-06-2021")

response_dict = r.json()

for value in response_dict.values():
    for items1 in value:
        for key1, value1 in items1.items():
            print (str(key1) + " " + str(value1))

