from PIL import Image

#read base image
background = Image.open("bg.jpg")

# read all the profile images
img = Image.open("profile.jpg")
# place each and write the image to folder
print(img.size)
print(background.size)
x, y = img.size
# resize the image
size = (1354,2030)
background = background.resize(size,Image.ANTIALIAS)

background.paste(img,(0,0,x,y))
background.save('output.png',"PNG")
