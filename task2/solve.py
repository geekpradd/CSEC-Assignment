import numpy as np
from PIL import Image
import pickle

symbols = ["(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "//", "*"]

dictionary = {x:np.zeros((7, 5)) for x in symbols}

img = open("images.dat", "rb")

image_list = pickle.load(img)

img.close()

dictionary["("] = image_list[0][:, 0:5] 
dictionary["8"] = image_list[0][:, 12:17]
dictionary["3"] = image_list[0][:, 18:23]
dictionary["2"] = image_list[0][:, 24:29]
dictionary["4"] = image_list[0][:, 36:41]
dictionary["9"] = image_list[0][:, 42:47]
dictionary["-"] = image_list[0][:, 51:56]
dictionary["7"] = image_list[0][:, 72:77]
dictionary["1"] = image_list[0][:, 78:83]
dictionary["5"] = image_list[0][:, 90:95]
dictionary["*"] = image_list[1][:, 50:55]
dictionary["0"] = image_list[140][:, 30:35]
dictionary["//"] = image_list[3][:, 50:55]
dictionary["6"] = image_list[11][:, 24:29]
dictionary[")"] = image_list[11][:, 73:78]
dictionary["+"] = image_list[50][:, 44:49]


expressions = []
results = []

final_out = ""
answers = ""
for image in image_list:
	string = ""
	total = image.shape[1]
	for r in range(total-4):
		characters = image[:, r:r+5]
		# print (r)
		for ch in symbols:
			al = characters == dictionary[ch]
			if al.all():
				string += ch

	expressions.append(string)
	results.append(eval(string))
	final_out += "{0} = {1} \n".format(string, eval(string))
	answers += "{0}\n".format(eval(string))

with open("answers-both.txt", "w") as f:
	f.write(final_out)

with open("answers.txt", "w") as f:
	f.write(answers)