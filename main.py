from PIL import Image
import numpy

size = 1024
offset = 10

def getPi(n):
	arr= []
	img = Image.new("RGB", (size+2*offset,size+2*offset), "white")
	drawCircle(img)
	splashPoints(n,img)
	arr = counter(img)
	pi = arr[0]/arr[1]
	if(pi > 3.14):
		img.show()
		print(pi)
		img.save(str(pi)+".jpg")

def drawCircle(img):
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			if((x-offset-size//2)**2 + (y-offset-size//2)**2 > (size//2)**2 and (x-offset-size//2)**2 + (y-offset-size//2)**2 < (size//2+1)**2):
				img.putpixel((x,y),(128,128,128))

def splashPoints(n,img):
	sizeX = img.size[0]
	sizeY = img.size[1]
	for i in range(n):
		for j in range(2):
			tempX = numpy.random.randint(sizeX)
			tempY = numpy.random.randint(sizeY)
		img.putpixel((tempX, tempY), (0,0,0))


def counter(img):
	outside = 0
	inside = 0
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			r,g,b = img.getpixel((x,y))
			if((r,g,b) == (0,0,0)):
				if((x-offset-size//2)**2 + (y-offset-size//2)**2 > (size//2)**2):
					img.putpixel((x,y),(255,0,0))
					outside += 1
				else:
					inside +=1
	return inside,outside
				



def main():
	#n = int(input())
	n = 99999
	i = 0
	while(1):
		print(i)
		i+=1
		getPi(n)



main()