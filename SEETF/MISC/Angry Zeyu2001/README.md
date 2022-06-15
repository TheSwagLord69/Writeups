# angry_zeyu2001

Looking through the images, I noticed that this image had been strip cut.

![Initial cuts](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Images/inital%20pieces.jpg)

After analyzing the images, i realised that the images were relevant to its neighbouring images of similar titles.
The format of the image's alignment is xxx.yyy where x is the horizontal index and y is the vertical index.

![Analyzing the cuts](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Images/similar.jpg)

I decided to join the image bits in vertical strips first to confirm my hypothesis.

![Vertical Strips](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Images/strips.jpg)

The vertical strips seem to be doing an incremental vertical shift upwards after the second strip.

![Combined Vertical Images](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Images/Capture.jpg)

I edited my code to include a vertical shift downwards after the second vertical strip, and combined the images horizontally.

![Flag Image](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Images/flag.jpg)

The image was not perfect, but the flag could still be seen.

## Flag

> **SEE{boss_aint_too_happy_bout_me_9379c958d872435}**

## Code

```python
from PIL import Image
import os
import re
import cv2
import numpy as np
from collections import deque

jpglist = []

for i in os.listdir():
    if str(i)[-3:] == "jpg":
        jpglist.append(i)
        
bitmaps = []
for c, i in enumerate(jpglist):
    c = cv2.imread(os.getcwd() + "\\" + str(i))
    bitmaps.append(c)

#Store Vertical Images
vert_list = []

#Counter
ctr = -1

#Combine Images Vertically
z=0
for i in range(54):
    x = z
    if x > 0:
        x=z+1
    print(x)
    
    mylist = deque([bitmaps[x+0],bitmaps[x+1],bitmaps[x+2],bitmaps[x+3],bitmaps[x+4],bitmaps[x+5],bitmaps[x+6],bitmaps[x+7],bitmaps[x+8],bitmaps[x+9],bitmaps[x+10],bitmaps[x+11],bitmaps[x+12],bitmaps[x+13],bitmaps[x+14],bitmaps[x+15],bitmaps[x+16],bitmaps[x+17],bitmaps[x+18],bitmaps[x+19],bitmaps[x+20],bitmaps[x+21],bitmaps[x+22]])
    #mylist.rotate(-1) 
    if i>1:
        mylist.rotate(ctr)
        ctr = ctr-1
    
    #im_v = cv2.vconcat([bitmaps[x+0],bitmaps[x+1],bitmaps[x+2],bitmaps[x+3],bitmaps[x+4],bitmaps[x+5],bitmaps[x+6],bitmaps[x+7],bitmaps[x+8],bitmaps[x+9],bitmaps[x+10],bitmaps[x+11],bitmaps[x+12],bitmaps[x+13],bitmaps[x+14],bitmaps[x+15],bitmaps[x+16],bitmaps[x+17],bitmaps[x+18],bitmaps[x+19],bitmaps[x+20],bitmaps[x+21],bitmaps[x+22]])
    im_v = cv2.vconcat(mylist)
    cv2.imwrite('test'+str(i)+'.jpg', im_v)
    z = z+22
    
    vert_list.append(im_v)
    
#Combine Images Horizontally
im_h = cv2.hconcat(vert_list)
cv2.imwrite('flag.jpg', im_h)
```
