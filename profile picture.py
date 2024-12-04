from PIL import Image
image=Image.open("example.jpg")
rotated_image=image.rotate(45)
RGB_image=image.convert("RGB")
red,green,blue=image.split()

coordinates_1=(25,0,671,522)
cropped_red1=red.crop(coordinates_1)
coordinates_red1=(50,0,696,522)
cropped_red2=red.crop(coordinates_red1)
blend_red=Image.blend(cropped_red1,cropped_red2,0.5)

cropped_green=green.crop(coordinates_1)

cropped_blue1=blue.crop(coordinates_1)
coordinates_2=(0,0,646,522)
cropped_blue2=blue.crop(coordinates_2)
blend_blue=Image.blend(cropped_blue1,cropped_blue2,0.5)
image=Image.merge("RGB",(blend_red,cropped_green,blend_blue))

image.thumbnail((80,80))
image.save("thumbnail.jpg")
