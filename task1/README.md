## All Possible Combinations 

So here we are given three byte combination with the fourth byte being a newline character. Initially I tried going through the data line by line but that approach fails because newline is itself a byte and so every time a newline character appears other than the fourth position it causes a new line to come in which means that instead of three bytes between newlines we may have one or two bytes and sometimes no bytes.

So instead of reading line by line I use python's binary reading powers to read the data stream byte by byte and to ignore the fourth byte. I use a numpy three dimensional array of dimension `(256, 256, 256)` to mark entries that are there in the data stream.

After we process through all four files I simply go through all entries of this three dimensional array and append those entries into a separate list that were not there in the data stream.

I obtain the following 15 entries where every tuple corresponds to a missing three byte combination:

```
[(32, 87, 101), (32, 97, 115), (65, 108, 108), (68, 77, 171), (97, 116, 105), (98, 108, 101), (99, 114, 101), (105, 110, 103), (105, 115, 32), (107, 32, 102), (109, 32, 115), (111, 108, 118), (111, 114, 32), (112, 114, 111), (118, 101, 32)]
```

These entries are missing from the files. Converting them into characters we obtain the following "words": 

```
 We, as,All,DM«,ati,ble,cre,ing,is ,k f,m s,olv,or ,pro,ve 
```

It seems that there are indeed english characters here and if we permute these we should be able to obtain a sentence (15! is a bit high, I guess we'll have to play jigsaw here).

The code that generates this is in `main.py`. I was unable to upload the part files in this folder due to my slow internet speed but putting them in the same folder as the script should work.