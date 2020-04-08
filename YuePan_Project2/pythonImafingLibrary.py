from PIL import Image

#Example one - basic skills
# open a jpg image
img = Image.open('/Users/nina/Desktop/CPS3320desktop/raw.jpg')

#show the original size
print (img.size)

# Reduce the image by 50%
w, h = img.size

img.thumbnail((w//2, h//2))


# Save the smaller image
img.save('/Users/nina/Desktop/CPS3320desktop/rawsmall.jpg', 'jpeg')

#show the information of the latest image
print (img.size) # the size of the image
print (img.mode) # the mode of the image
print (img.format)  # the format of the image

# change the mode to "L" and save it in jpeg mode
print (img.mode)
rgb2xyz = (0.412453,0.357580, 0.180423, 0,0.212671,0.715160, 0.072169, 0,0.019334,0.119193, 0.950227, 0 )
new_img1 = img.convert("L", rgb2xyz)
print(new_img1.mode)
new_img1.show() 
new_img1.save('/Users/nina/Desktop/CPS3320desktop/new_img1.jpg', 'jpeg')

# change the mode to "P" and save it in png mode
print (img.mode)
new_img2 = img.convert('P')
print(new_img2.mode)
new_img2.show()
new_img2.save('/Users/nina/Desktop/CPS3320desktop/new_img2.png', 'png')

# Eample 2- Filter & Blend
from PIL import ImageFilter  
# Filter an image
imgF = Image.open('/Users/nina/Desktop/CPS3320desktop/raw.jpg')
bluF = imgF.filter(ImageFilter.BLUR)                ##Blur
conF = imgF.filter(ImageFilter.CONTOUR)             ##Find the coutour
edgeF = imgF.filter(ImageFilter.FIND_EDGES)         ##Find the edge
imgF.show()
bluF.show()
conF.show()
edgeF.show()
# Put all 4 pictures together
F4 = Image.open('/Users/nina/Desktop/CPS3320desktop/filter4.jpeg')
F4.show()


b1 = Image.open('/Users/nina/Desktop/CPS3320desktop/b1.png')
b2 = Image.open('/Users/nina/Desktop/CPS3320desktop/b2.png')
print (b1.size)
print (b2.size)
#Make the second picture the same size as the first picture
b11  = b1.resize((888, 660))
b11.show() 
b2.show()
#Interpolate a new image using the given two images and the transparency variable alpha. 
#The two images must have the same size and pattern.
bb112 = Image.blend(b11, b2, 0.4)
bb112.show()
