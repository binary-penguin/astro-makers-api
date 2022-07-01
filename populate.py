import imp
from pprint import pprint
import mysql.connector
import json
from mysql.connector import errorcode
import requests

# Credentials
f = open("credentials.json")
data = json.load(f)
NASA_KEY = data["nasa_key"]
DB_KEY = data["db_key"]


cnx = mysql.connector.connect(user='sql3503289', password=DB_KEY,
                                host='sql3.freemysqlhosting.net',
                                database='sql3503289')


cursor = cnx.cursor()

add_pic = """INSERT INTO pictures (explanation, hdurl, url, title) VALUES (%s, %s, %s, %s)"""

count = 0

base_url = 'https://api.nasa.gov/planetary/apod?api_key=' + NASA_KEY

for month in range(1, 8):
    if count >= 100:
        break
    for day in range(1, 26):
        if count >= 100:
            break
        str_month = "0" + str(month) if month < 10 else str(month)
        str_day = "0" + str(day) if day < 10 else str(day)
        url = base_url + "&" + "date=2021-" + str_month + "-" + str_day

        r = requests.get(url)
        response_data = r.json()

        explanation = response_data["explanation"]

        if not "hdurl" in response_data:
            continue
        
        hdurl = response_data["hdurl"]
        title = response_data["title"]
        url = response_data["url"]

        cursor.execute(add_pic, (explanation, hdurl, url, title))
        cnx.commit()
        count += 1


print("done!")
cursor.close()
cnx.close()
