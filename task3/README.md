## Web Challenge

The password is `cp6xycx9r42y3q5jsvl8mthwwc8zuccj`.

The script is called task3.py and I've basically used SQL injection to obtain the password. Please note that the python requests module needs to be installed to run task3.py. Please note I am using Python 3.6 and this may not work with Python 2.

So the URL given redirects us to PHP site in which we can enter a username and check if this username exists in the table. No other information is given out and no echo is used to retrieve values from the table. This is initially caused some issues for me (being a newbie in SQL injection) as the questions I previously did involved cleverly changing the search parameters so that the entire table is outputted in the client side (by using something like `password' OR '1' = '1`) which would cause all the entries in the table to pass through the WHERE. But since nothing from the table is being displayed in the CLIENT side (other than proof of existence) this approach fails.

I initially thought that maybe we could use the DEBUG flag to display the results (as it's echoing something which is not fixed but it's only echoing the query sigh) but that ended up going nowhere. But wait a second the table structure is given as a comment. And the password is stored as plain text! Bad move. Should have atleast hashed it and made life more hard for me.

So let's go through the code once. The code is clearly open to SQL injection and runs this query and checks if there are any rows satisfying the query. If so it gives a positive signal and else it gives a negative signal.

So we can use this! Firstly we want the admin passowrd and clearly by inputing admin we see an admin user exists. But we can modify the query and since we know the name of the password column (never make your table structure open) we can use SQL functions on this column.

Let's find the length of the password. We want to run queries of the form:

```
SELECT * from users where username = "admin" AND LENGTH(password) = x;
```

where x is a parameter. Clearly only when x is equal to the actual password length we will have any rows in the output (i'm assuming there is only one admin) I quickly hack up a script (using requests to make the POST request, I simply have to modify the username field and add in the part after the first = symbol) and comparing the output using some string manipulation to check whether we obtained any rows or not (simply comparing with positive/negative echo output).

The function corresponding to finding the length is `check_length`. I run the script here and find that the length is `32`.

Now to actually obtain the characters we can simply bruteforce over the positions. I assume that the character at every position is alphanumeric  + some basic symbols. These I take from the python `string.printable` object. Turns out only numbers and lowercase characters would have worked.

To check if the password character at position `i` is equal to character `c`, we need to run queries of the form:

```
SELECT * from users where username  = "admin"  and SUBSTR(password, i, 1) = "c";
```

Again I wrote a function `check_character(position, character)` to do this and I just run the above query and check if the output is positive (rows exist) or not. Bruteforcing through all 32 positions over alphanumeric characters then allows me to obtain the password characters at each index which I then combine to get the final password.

Thus we finally obtain the password `cp6xycx9r42y3q5jsvl8mthwwc8zuccj`. This challenge would have been far tougher (and probably impossible) if the password column was named something else and this name was not displayed since then we would not have been able to run SQL functions to extract information out of this column. Overall a fun challenge and I learnt a new way of doing SQL injection through this!

