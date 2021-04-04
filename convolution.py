from PIL import Image

def convolute(image,convolutionTable,size):
	newImage = Image.new('RGB', (im.size[0], im.size[1]))
	pixelsMap = image.load()
	newPixelsMap = newImage.load()
	for y in range(size//2,im.size[1]-size//2):
		for x in range(size//2,im.size[0]-size//2):
			newPixel = [0,0,0]
			for j in range(size):
				for i in range(size):
						newPixel = [pixelsMap[y + j - size//2,x + i - size//2][e] * convolutionTable[j][i] + newPixel[e] for e in range(3)]
			newPixelsMap[y,x] = tuple([int(e / 1) for e in newPixel]) #(size * size)
	return newImage

im = Image.open('test.png')
convolution = [	[1/9,1/9,1/9],
				[1/9,1/9,1/9],
				[1/9,1/9,1/9]]
newImage = convolute(im,convolution,3)
newImage.save('test.png')