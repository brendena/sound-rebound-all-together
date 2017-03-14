import sys
from PIL import Image
from pathlib import Path
from PIL import ImageFont
from PIL import ImageDraw 
'''
http://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
http://stackoverflow.com/questions/10647311/how-do-you-merge-images-into-a-canvas-using-pil-pillow
'''

types = ['zcr','rms','mfcc','mel']
typeClassifier = ['Naiye Bayes','Random Forest','KNN DTW','soft voting']
numberFramePerSection = [i for i in range(1,16)]
hopLength = [i for i in range(2,18,2)]

width = 800
height = 600

for nFrames in numberFramePerSection:
	for hLength in hopLength:
		if nFrames % hLength !=0:
			break

		imageFiles = []

		for typeAudio in types:
			for classifier in typeClassifier:
				file = "./images/" + classifier + "_"+ typeAudio+"_"+str(nFrames)+"nFrames_"+str(hLength)+"hLength.png"
				if Path(file).is_file():
					imageFiles.append(file)
				else:
					imageFiles.append("./images/blank.png")

		

		newWidth = width * len(typeClassifier)
		newHeight = height*len(types)
		new_im = Image.new('RGB', (newWidth,newHeight+200))


		#Here I resize my opened image, so it is no bigger than 100,100
		#im.thumbnail((100,100))
		

		count = 0
		for row in range(0,newWidth,width):
			for column in range(0,newHeight,height):
				
				new_im.paste(Image.open(imageFiles[count]),(row,column))
				count = count + 1

		draw = ImageDraw.Draw(new_im)

		font = ImageFont.truetype("resources/UbuntuMono-RI.ttf", 40)

		for i in range(0,len(types)):
			draw.text(( i*width + width/2,newHeight),types[i],(155,155,155),font=font)

		new_im.save('./images/combinedImages/'+str(hLength)+ "_"+ str(nFrames)+ '.png')

		break
