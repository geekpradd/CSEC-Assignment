## Wifi Password Cracking

This was something completely new for me although it turned out relatively easy (once you know which commands to use that is). Anyway the password is "bhavesh007bhavika".

Extracting the ZIP resulted in two files a PCAP network dump data file and a dictionary of candidate passwords (with a guarantee that one of the words is the password, I think it's difficult to get something like this in practice!). So having previously tried some network data investigative problems I opened the PCAP file in Wireshark. And I tried going through the entries. It did not go well. Firstly there were a lot of devices in the data and most of it was ordinary network traffic. Having to wade through this seemed pretty impossible (plus for some reason I was hoping the password would be there in plain text which was dumb of me to assume).

So I tried another way, I used `strings` to dump out any ASCII strings in the PCAP file and wrote a python script to wade through the unique strings in this dump and compare this with the dictionary we are given. This did not work. So the password is not there in plain text after all (ofcourse that would be dumb but forgive me for trying since it's my first).

I then had to google and I found some old CTF problems in which one had to construct the dictionary and then use it to do a dictionary attack on the network file. It turns out `aircrack-ng` allows us to do a dictionary attack (probably by using the WPA protocol on the dictionary words and comparing it with the data in the packet file, not sure but I guess since it's one directional this is how it would normally work). 

Here we are already given the network file and the dictionary! So after installing `aircrack-ng` all we need to do is run:

```
aircrack-ng friday.pcap -w wordlist.txt
```

And magic happens in front of us and we obtain the password which is "bhavesh007bhavika" (probably a bad idea to name your password after two people and use the bond number in between but who am I to judge xD).

The output of the above command is stored in output.txt in the same folder as this writeup.