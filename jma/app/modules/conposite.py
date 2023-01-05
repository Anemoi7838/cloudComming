import cv2
import numpy as np
import app.modules.calc as calc
def gsi():
    images_path = "app/static/images/gsi/"
    gsiImg = []
    gsiN = []
    gsiS = []
    gsinw = cv2.imread(images_path + "gnw.jpg")
    gsine = cv2.imread(images_path + "gne.jpg")
    gsiN.append(gsinw)
    gsiN.append(gsine)
    gsiN = cv2.hconcat(gsiN)
    gsisw = cv2.imread(images_path + "gsw.jpg")
    gsise = cv2.imread(images_path + "gse.jpg")
    gsiS.append(gsisw)
    gsiS.append(gsise)
    gsiS = cv2.hconcat(gsiS)
    gsiImg.append(gsiN)
    gsiImg.append(gsiS)
    gsiImg = cv2.vconcat(gsiImg)
    cv2.imwrite(images_path + "GSI.jpg",gsiImg)

def border():
    images_path = "app/static/images/border/"
    bImg = []
    bN = []
    bS = []
    bnw = cv2.imread(images_path + "bnw.jpg")
    bne = cv2.imread(images_path + "bne.jpg")
    bN.append(bnw)
    bN.append(bne)
    bN = cv2.hconcat(bN)
    bsw = cv2.imread(images_path + "bsw.jpg")
    bse = cv2.imread(images_path + "bse.jpg")
    bS.append(bsw)
    bS.append(bse)
    bS = cv2.hconcat(bS)
    bImg.append(bN)
    bImg.append(bS)
    bImg = cv2.vconcat(bImg)
    cv2.imwrite(images_path + "BORDER.jpg",bImg)

def surf():
    images_path = "app/static/images/"
    gimages_path = "app/static/images/gsi/"
    bimages_path = "app/static/images/border/"
    gsiImg = cv2.imread(gimages_path + "GSI.png")
    #bImg = cv2.imread(bimages_path + "BORDER.png")
    #cnpst = cv2.addWeighted(src1=gsiImg,alpha=0.5,src2=bImg,beta=0.5,gamma=0)
    cv2.imwrite(images_path + "surf.png",gsiImg)

def cnpst(lon,lat,plon,plat,times):
    images_path = "app/static/images/"
    inFiles = ["now.png","forecast10.png","forecast15.png","forecast20.png","forecast25.png","forecast30.png",\
    "forecast35.png","forecast40.png","forecast45.png","forecast50.png","forecast55.png","forecast60.png"]
    outFiles = ["jmaNow.png","jmaF10.png","jmaF15.png","jmaF20.png","jmaF25.png","jmaF30.png",\
    "jmaF35.png","jmaF40.png","jmaF45.png","jmaF50.png","jmaF55.png","jmaF60.png"]
    for (inFile,outFile,time) in zip(inFiles,outFiles,times):
        precImg = cv2.imread(images_path + "prec/" + inFile,-1)
        surfImg = cv2.resize(cv2.imread(images_path + "surf.png"),(precImg.shape[0],precImg.shape[1])).astype(np.float64)
        height,width = precImg.shape[0],precImg.shape[1]
        mask = precImg[:,:,3]
        mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        mask = mask/255
        precImg = precImg[:,:,:3]
        surfImg[0:height,0:width] *= 1 - mask
        surfImg[0:height,0:width] += precImg * mask
        x,y = calc.xy(lon,lat,plon,plat)
        circle = cv2.resize(cv2.imread(images_path + "circle.png"),(5,5))
        surfImg[y:y+circle.shape[0],x:x+circle.shape[1]] = circle
        cv2.putText(surfImg,time,(10,20),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.5, color=(0,0,0),thickness=2)
        cv2.imwrite(images_path + "/cnpst/"+ outFile ,surfImg)
   