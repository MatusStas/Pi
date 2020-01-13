from PIL import Image, ImageDraw
import numpy
import math


size = 1024
offset = 10


def colorCircle(img,arr):
	for item in arr:
		x,y,color = item
		img.putpixel((x,y),color)


def drawCircle(img):
	draw = ImageDraw.Draw(img)
	draw.ellipse((offset,offset,size+offset,size+offset), fill = 'white', outline = 'black')


def getPi(n,img):
	outside = 0
	inside = 0
	arr = []

	for i in range(n):
		x = numpy.random.randint(img.size[0])
		y = numpy.random.randint(img.size[1])
		if (x-(offset+size//2))**2 + (y-(offset+size//2))**2 > (size//2)**2:
			outside += 1
			arr.append([x,y,(255,0,0)])
		else:
			inside += 1
			arr.append([x,y,(0,0,0)])

	return inside/outside, arr


def makePi(n):
	img = Image.new("RGB", (size+2*offset,size+2*offset), "white")
	pi, arr = getPi(n,img)
	if 3.14 < pi < 3.15:
		drawCircle(img)
		colorCircle(img, arr)
		img.show()
		img.save(f'{pi}.jpg')


def main():
	n = 10**5
	while(1):
		makePi(n)


main()