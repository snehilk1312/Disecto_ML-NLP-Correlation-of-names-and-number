import random
import names
from PIL import Image, ImageDraw, ImageFont

# reusable variables
font_name = '/usr/share/fonts/truetype/tlwg/TlwgTypo-Bold.ttf'
color = 'rgb(0, 0, 0)'  # text color - black
size = 50
font = ImageFont.truetype(font_name, size=size)
count = 0

# function to create fake names
def name_creation():
	message = names.get_full_name().split(' ')[0]
	message = str('Name: ' + str(message))
	return message	

# function to create fake ids
def id_creation():
	# unique id , as per aadhar card
	aadhar_id = random.randint(100000000000, 999999999999)
	message = str('ID: ' + str(aadhar_id))
	return message

# generating fake profiles 
for i in range(150):
	count+=1
	image = Image.new(mode='RGB', size=(1000, 300), color=(255, 255, 255))
	draw = ImageDraw.Draw(image)


	message = id_creation()
	draw.text((50, 75), message, fill=color, font=font)

	message = name_creation()
	draw.text((50, 150), message, fill=color, font=font)

	# save created images in images folder
	location = 'images/'
	image.save(location+str(count)+'.jpg')

# generating fake profiles so that 1 image may have more than 1 profile(here 3)	
for i in range(50):
	count+=1
	image = Image.new(mode='RGB', size=(1000, 1000), color=(255, 255, 255))
	draw = ImageDraw.Draw(image)


	message = id_creation()
	draw.text((50, 75), message, fill=color, font=font)

	message = name_creation()
	draw.text((50, 150), message, fill=color, font=font)

	message = id_creation()
	draw.text((50, 300), message, fill=color, font=font)

	message = name_creation()
	draw.text((50, 375), message, fill=color, font=font)

	message = id_creation()
	draw.text((50, 525), message, fill=color, font=font)

	message = name_creation()
	draw.text((50, 600), message, fill=color, font=font)


	# save the edited image
	location = 'images/'
	image.save(location+str(count)+'.jpg')

