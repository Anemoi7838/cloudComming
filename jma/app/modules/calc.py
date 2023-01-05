import numpy as np
lon_slope=0.00549453125
lat_slope=-0.0043765625
plonlist=np.array([126.5624,127.9714,129.3777,130.7675,132.1792,
                   133.5910,135.0082,136.4058,137.8124,139.2228,
                   140.6263,142.0326,143.4306,144.8423,146.2527])
platlist=np.array([27.0591,28.3067,29.5376,30.7536,31.9498,33.1398,
                   34.3094,35.4584,36.6000,37.7164,38.8161,39.9118,
                   40.9736,42.0350,43.0668,44.0895,45.0870,46.0751])

def lonlat(x,y,plon,plat):
    lon = lon_slope * int(x) + plon
    lat = lat_slope * int(y) + plat
    return lon,lat
#print(lonlat(75,167))

def xy(lon,lat,plon,plat):
    y = int((float(lat) - plat)/lat_slope)
    x = int((float(lon) - plon)/lon_slope)
    if x > 251:
        x = 251
    if y > 251:
        y = 251
    return x,y
#print(xy(137.1780312,36.69799))

#def imagePosition(lon,lat):
def imagePosition(lon,lat):
    
    imgPosition=np.zeros((15,18,4))
    yy=0
    for plon in plonlist:
        xx=0
        for plat in platlist:
            imgPosition[yy,:,0] = plon
            imgPosition[:,xx,1] = plat
            imgPosition[yy,xx,2] = 218 + yy
            imgPosition[yy,xx,3] = 108 - xx
            print(imgPosition[yy,xx,:])
            if lon < imgPosition[yy,xx,0] and lat < imgPosition[yy,xx,1]:
                plon = imgPosition[yy-1,xx,0]
                plat = imgPosition[yy-1,xx,1]
                ulon = imgPosition[yy-1,xx,2]
                ulat = imgPosition[yy-1,xx,3]
                print(imgPosition[yy-1,xx,:])
                return plon,plat,ulon,ulat
            xx+=1
        yy+=1
            
    #return plon,plat,ulon,ulat
#imagePosition()
#a,b,c,d=imagePosition(137.17803,36.69799)
#print(a,b,c,d)
    