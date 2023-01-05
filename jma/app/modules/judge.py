import cv2
import numpy as np

def rain(x,y):
    x = int(x); y = int(y)
    judge = []
    images_path = "app/static/images/prec/"
    inFiles = [ "now", "forecast10", "forecast15", "forecast20","forecast25","forecast30"\
    ,"forecast35", "forecast40", "forecast45", "forecast50", "forecast55", "forecast60"]
    for inFile in inFiles:
        imgSize = 256
        precImg = cv2.imread(images_path  + inFile + ".png")
        if (x>imgSize-3):
            x = imgSize -3
        if (y>imgSize-3):
            y = imgSize -3
        color = precImg[y,x,:]
        print(color)
        if np.all(color == [255,255,255]):
            judge.append("降水なし")
        elif np.all(color == [104,0,180]):
            judge.append("猛烈な降水")
        elif np.all(color == [0,40,255]):
            judge.append("非常に激しい降水")
        elif np.all(color == [0,153,255]):
            judge.append("激しい降水")
        elif np.all(color == [0,245,255]):
            judge.append("強い降水")
        elif np.all(color == [255,65,0]):
            judge.append("やや強い降水")
        elif np.all(color == [255,140,33]):
            judge.append("降水")
        elif np.all(color == [255,210,160]):
            judge.append("弱い降水")
        elif np.all(color == [255,242,242]):
            judge.append("非常に弱い降水")
        else:
            judge.append("降水なし")
        #print(judge)
    return judge