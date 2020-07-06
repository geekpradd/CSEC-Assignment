## Equations

So initially I thought maybe it has something to do with seven segment displays since every unit is composed of seven rows. However nothing worked in that direction and as they say sometimes overthinking is bad. So instead I just tried plotting the image as grayscale and voila!

Basically it turned out that taking every 7 lines and converting it to an image using PIL worked. The code is in `gen.py` and the images are then outputted into the outputs folder.

Now we need to convert it into something that Python can understand. I thought of using PyTesseract OCR but that didn't work out. Instead maybe we can hand engineer?

I observed that every character has width of 5 units. And this structure of the character remains the same throughout. So if we can simply find out the corresponding array structure of each character we are done.

This is what `solve.py` is doing. Note that I also saved the images in pickle format (please use Python 3) as the solving part just needs the numpy arrays. Then in solve.py I manually find out the arrays for each symbol and feed it into a dictionary.

Now it becomes straightforward, we simply loop through windows of size "5" over each equation and if it matches an entry in our dictionary we add that character to a string. Python's eval function then allows us to solve the equation.

I then outputted the answers in `answers.txt` and both the parsed equation and the answers in `answers-both.txt`. Also do keep in mind that division corresponds to "//" and not "/" as mentioned in the question (again as per Python 3).