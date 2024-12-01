from PIL import Image
red=Image.open("red3.jpg")
blue=Image.open("blue3.jpg")
green=Image.open("green.jpg")
new_image=Image.merge("RGB",(red,green,blue))
new_image.save("new_image.jpg")
