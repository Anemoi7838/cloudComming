import os
import cv2
import sys
import shutil
import datetime
import requests
def gps():
    geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
    geo_data = requests.get(geo_request_url).json()
    lat = geo_data['latitude']
    lon = geo_data['longitude']
    return(lat,lon)
def images():
    url = date()
    furl_header="https://static.tenki.jp/static-images/rainmesh-short/"
    furl_footer="area-4-large.jpg"
    images_path = "app/static/images"
    fileName = "now.jpg"

    os.makedirs(images_path,exist_ok=True)

    response = requests.get(url)
    image = response.content
    
    with open(fileName, "wb") as f:
        f.write(image)
    shutil.move(fileName,images_path+"/"+fileName)


    for it in range(10,70,10):
        fileName = "forecast"+str(it)+".jpg"
        furl = furl_header + str(it) +"/" + furl_footer
        response = requests.get(furl)
        image = response.content
        with open(fileName, "wb") as f:
            f.write(image)
        shutil.move(fileName,images_path+"/"+fileName)

def date():
    url_header="https://imageflux.tenki.jp/large/static-images/radar/"
    url_footer="area-4-large.jpg"

    dt_now = datetime.datetime.now()
    year = dt_now.strftime("%Y")
    month = dt_now.strftime("%m")
    day = dt_now.strftime("%d")
    hour = dt_now.strftime("%H")
    minute = dt_now.minute
    if minute <= 5 :
        hour = (dt_now - datetime.timedelta(hours=1)).strftime("%H")
        minute = "00"
    elif minute <= 10:
        minute = "05"
    elif minute <= 15:
        minute = "10"
    elif minute <= 20:
        minute = "15"
    elif minute <= 25:
        minute = "20"
    elif minute <= 30:
        minute = "25"
    elif minute <= 35:
        minute = "30"
    elif minute <= 40:
        minute = "35"
    elif minute <= 45:
        minute = "40"
    elif minute <= 50:
        minute = "50"
    elif minute <= 55:
        minute = "50"
    elif minute <= 60:
        minute = "55"
    url = url_header+str(year)+"/"+str(month)+"/"+str(day)+"/"+str(hour)+"/"+str(minute)+"/00/"+url_footer
    print(url)
    return url