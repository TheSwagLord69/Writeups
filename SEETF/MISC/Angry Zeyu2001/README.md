# angry_zeyu2001

First, looking through the images, I noticed that this image had been strip cut.

![Initial Strips](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/inital%20pieces.JPG)

The format of the image's alignment is xxx.yyy where x is the horizontal index and y is the vertical index

I decided to join the image in vertical strips first to confirm my hypothesis.

![Vertical Strips](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/strips.JPG)

The vertical strips seem to be doing an incremental vertical shift upwards after the second strip.

![Combined Vertical Images](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/Capture.JPG)

I edited my code to include a vertical shift downwards after the second vertical strip.

![Flag Image](https://github.com/TheSwagLord69/Writeups/blob/main/SEETF/MISC/Angry%20Zeyu2001/flag.jpg)

## Flag

> SEE{boss_aint_too_happy_bout_me_9379c958d872435}
