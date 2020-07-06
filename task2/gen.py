import numpy as np 
from PIL import Image

images = []
def conv(x):
	x = x.strip()
	out = []
	for c in x:
		if c == '1':
			out.append(255)
		else:
			out.append(0)
	return out

def dump(r, data):
	print ("At " + str(r))
	total = len(data[0])

	data = [conv(x) for x in data[:-1]]
	array = np.array(data, dtype=np.uint8)
	images.append(array)
	img = Image.fromarray(array)
	img.save("outputs/out{0}.jpg".format(r))

f = open("output.txt", "r")
data = f.readlines()
cycles = len(data)//8

for r in range(cycles):
	dump(r, data[r*8:(r+1)*8])

f.close()

outfile = "images.dat"
of = open(outfile, "wb")
import pickle
pickle.dump(images, of)

of.close()
