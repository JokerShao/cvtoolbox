import time
from PIL import Image
import cv2


times = 10

# Read images
radar_bg = Image.open('radar_bg.png')
radar = Image.open('radar.png')

# Option A: Fully blend radar image onto the radar background image.
# Blend that composite with alpha 0.7 onto the base image.

t1 = time.time()
for _ in range(times):
    radar_bg = radar_bg.convert('RGBA')
    radar = radar.convert('RGBA')
    comp_a = Image.alpha_composite(radar_bg, radar)
t2 = time.time()
print(1e3*(t2-t1))

# comp_a.putalpha(comp_a.getchannel('A').point(lambda x: x * 0.7))
# comp_a = Image.alpha_composite(basemap, comp_a)
# comp_a.show()
# comp_a.save('comp_a.png')

# # Option B: Blend radar background image with alpha 0.7 onto the base
# # image. Blend radar image with alpha 0.7 onto that composite.
# radar_bg.putalpha(radar_bg.getchannel('A').point(lambda x: x * 0.7))
# radar.putalpha(radar.getchannel('A').point(lambda x: x * 0.7))
# comp_b = Image.alpha_composite(Image.alpha_composite(basemap, radar_bg), radar)
# # comp_b.save('comp_b.png')
# comp_b.show()



# Read the images
foreground = cv2.imread("radar.png", -1)
background = cv2.imread("radar_bg.png", -1)
alpha = foreground[...,3]
# alpha = cv2.imread("puppets_alpha.png")

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)

# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255

t1 = time.time()
for _ in range(times):


    # Multiply the foreground with the alpha matte
    foreground[...,0] = cv2.multiply(alpha, foreground[...,0])
    foreground[...,1] = cv2.multiply(alpha, foreground[...,1])
    foreground[...,2] = cv2.multiply(alpha, foreground[...,2])

    # Multiply the background with ( 1 - alpha )
    background[...,0] = cv2.multiply(1.0 - alpha, background[...,0])
    background[...,1] = cv2.multiply(1.0 - alpha, background[...,1])
    background[...,2] = cv2.multiply(1.0 - alpha, background[...,2])

    # Add the masked foreground and background.
    outImage = cv2.add(foreground, background)

t2 = time.time()
print(1e3*(t2-t1))


# # Display image
# cv2.imshow("outImg", outImage/255)
# cv2.waitKey(0)