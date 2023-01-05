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
    return(lon,lat)
def nowUrl(ulon,ulat):
    ndatelist = date("now")
    url_header = "https://www.jma.go.jp/bosai/jmatile/data/nowc/"
    url_footer = "/surf/hrpns/8/"+str(int(ulon))+"/"+str(int(ulat))+".png"
    url = url_header + ndatelist[0] + ndatelist[1] + ndatelist[2] + ndatelist[3] + ndatelist[4] + \
        "00/none/" + ndatelist[0] + ndatelist[1] + ndatelist[2] + ndatelist[3] + ndatelist[4] + "00" +url_footer
    print(url)
    return url
def frcstUrl(ulon,ulat):
    fdatelist = date("frcst")
    url_header = "https://www.jma.go.jp/bosai/jmatile/data/nowc/"
    url_footer = "/surf/hrpns/8/"+str(int(ulon))+"/"+str(int(ulat))+".png"
    url = []
    for index in range(int(len(fdatelist)/5)-1):
        url.append(url_header + fdatelist[0] + fdatelist[1] + fdatelist[2] + fdatelist[3] + fdatelist[4] + \
        "00/none/" + fdatelist[5*index+5] + fdatelist[5*index+6] + fdatelist[5*index+7] + fdatelist[5*index+8] + fdatelist[5*index+9] + "00" +url_footer)
    print(url)
    return url
def gsiUrl(ulon,ulat):
    url_header = "https://www.jma.go.jp/tile/gsi/pale/8/"
    url_footer = str(int(ulon))+"/"+str(int(ulat))+".png"
    gurlList = url_header + url_footer
    return gurlList

def borderUrl(ulon,ulat):
    url_header = "https://www.jma.go.jp/bosai/jmatile/data/map/none/none/none/surf/mask/8/"
    url_footer = str(int(ulon))+"/"+str(int(ulat))+".png"
    burlList = url_header + url_footer
    return burlList


def images(ulon,ulat):
    purl = nowUrl(ulon,ulat)
    pimages_path = "app/static/images/prec"
    fileName = "now.png"

    os.makedirs(pimages_path,exist_ok=True)

    response = requests.get(purl)
    image = response.content    
    with open(fileName, "wb") as f:
        f.write(image)
    shutil.move(fileName,pimages_path+"/"+fileName)
    fpurl = frcstUrl(ulon,ulat)
    #print(fpurl)
    fileNames = [ "forecast05.png", "forecast10.png", "forecast15.png", "forecast20.png", "forecast25.png", "forecast30.png",\
     "forecast35.png", "forecast40.png", "forecast45.png", "forecast50.png", "forecast55.png", "forecast60.png"] 
    index = 0
    for fileName in fileNames:
        response = requests.get(fpurl[index])
        image = response.content    
        with open(fileName, "wb") as f:
            f.write(image)
        shutil.move(fileName,pimages_path+"/"+fileName)
        index += 1
    
    gurl = gsiUrl(ulon,ulat)
    gimages_path = "app/static/images/gsi"
    fname = "GSI.png"
    os.makedirs(gimages_path,exist_ok=True)
    response = requests.get(gurl)
    image = response.content    
    with open(fname, "wb") as f:
        f.write(image)
    shutil.move(fname,gimages_path+"/"+fname)
    
    # burl = borderUrl(ulon,ulat)
    # bimages_path = "app/static/images/border"
    # fname = "BORDER.png"
    # os.makedirs(bimages_path,exist_ok=True)
    # response = requests.get(burl)
    # image = response.content
    
    # with open(fname, "wb") as f:
    #     f.write(image)
    # shutil.move(fname,bimages_path+"/"+fname)
    

def date(time):
    dt_now = datetime.datetime.now()
    timelag = dt_now -datetime.timedelta(minutes=3)
    if time == "now":
        ntimelag = timelag - datetime.timedelta(minutes=timelag.minute % 5)
        gmtNTimelag = ntimelag - datetime.timedelta(hours=9)
        ndatelist = []
        ndatelist.append(gmtNTimelag.strftime("%Y"))
        ndatelist.append(gmtNTimelag.strftime("%m"))
        ndatelist.append(gmtNTimelag.strftime("%d"))
        ndatelist.append(gmtNTimelag.strftime("%H"))
        ndatelist.append(gmtNTimelag.strftime("%M"))
        return ndatelist
    elif time == "frcst":
        ftimelag = timelag - datetime.timedelta(minutes=timelag.minute%10)
        gmtFTimelag = ftimelag - datetime.timedelta(hours=9)
        fdatelist = []
        fdatelist.append(gmtFTimelag.strftime("%Y"))
        fdatelist.append(gmtFTimelag.strftime("%m"))
        fdatelist.append(gmtFTimelag.strftime("%d"))
        fdatelist.append(gmtFTimelag.strftime("%H"))
        fdatelist.append(gmtFTimelag.strftime("%M"))
        trange = gmtFTimelag
        while ( trange < gmtFTimelag + datetime.timedelta(hours=1) ):
            trange = trange + datetime.timedelta(minutes=5)
            fdatelist.append(trange.strftime("%Y"))
            fdatelist.append(trange.strftime("%m"))
            fdatelist.append(trange.strftime("%d"))
            fdatelist.append(trange.strftime("%H"))
            fdatelist.append(trange.strftime("%M"))
            print(trange)
        return fdatelist
    elif time == "display":
        fdatelist = []
        # ftimelag = timelag - datetime.timedelta(minutes=timelag.minute%5)
        # fdatelist.append(ftimelag.strftime("%H:%M"))
        ftimelag = timelag - datetime.timedelta(minutes=timelag.minute%10)
        trange = ftimelag
        while( trange < ftimelag + datetime.timedelta(hours=1)):
            trange = trange + datetime.timedelta(minutes=5)
            fdatelist.append(trange.strftime("%H:%M"))
        return fdatelist
    else:
        print("select now or frcst.")
        sys.exit()
    