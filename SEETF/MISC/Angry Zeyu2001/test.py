from PIL import Image
import os
import re
import cv2
import numpy as np

jpglist = []

for i in os.listdir():
    if str(i)[-3:] == "jpg":
        jpglist.append(i)
        
bitmaps = []
for c, i in enumerate(jpglist):
    c = cv2.imread(os.getcwd() + "\\" + str(i))
    bitmaps.append(c)
    
#Combine Images Vertically
z=0
for i in range(52):
    x = z
    if x > 0:
        x=z+1
    print(x)
    im_v = cv2.vconcat([bitmaps[x+0],bitmaps[x+1],bitmaps[x+2],bitmaps[x+3],bitmaps[x+4],bitmaps[x+5],bitmaps[x+6],bitmaps[x+7],bitmaps[x+8],bitmaps[x+9],bitmaps[x+10],bitmaps[x+11],bitmaps[x+12],bitmaps[x+13],bitmaps[x+14],bitmaps[x+15],bitmaps[x+16],bitmaps[x+17],bitmaps[x+18],bitmaps[x+19],bitmaps[x+20],bitmaps[x+21],bitmaps[x+22]])
    cv2.imwrite('test'+str(i)+'.jpg', im_v)
    z = z+22
