import numpy as np
grid = np.zeros((256, 256, 256))

def update(file_name):
	with open(file_name, "rb") as f:
		three_bytes = []
		byte = f.read(1)
		while byte:
			if len(three_bytes) == 3:
				grid[three_bytes[0], three_bytes[1], three_bytes[2]] = 1
				three_bytes.clear()
				byte = f.read(1)
				continue
			three_bytes.append(int.from_bytes(byte, "big"))
			byte = f.read(1)

update("part1")
update("part2")
update("part3")
update("part4")


combinations = []
for a in range(256):
	for b in range(256):
		for c in range(256):
			if grid[a, b, c] == 0:
				combinations.append((a, b, c))

print (combinations)

for num, word in enumerate(combinations):
	w = ""
	for c in word:
		w += chr(c)
	print(str(num) + " " + w)