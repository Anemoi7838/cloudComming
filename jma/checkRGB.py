import cv2
import requests
import numpy as np

img = cv2.imread("app/static/images/cnpst/jmaF05.png")
print(img)
cv2.imshow("test",img)
cv2.waitKey(0)
#cv2.destroyAllWindow()