## Equations


Basically it turned out that taking every 7 lines and converting it to an image using PIL worked. The code is in `gen.py` and the images are then outputted into the outputs folder.

To convert this into equation we can use OCR or in my case we observe that the characters only have width of 5 units. We can then create a mapping of every character to their pixels and invert it to find the equation.

Running `solve.py` will output the equations with the answers in answers-both.txt and only the answers in answers.txt