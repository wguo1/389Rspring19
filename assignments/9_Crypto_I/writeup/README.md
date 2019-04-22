# Crypto I Writeup

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (70 Pts)
I thought this project was pretty simplistic. Obviously this would be useless in the real
world since we could assume that the password was only salted with a single character.
Though it was pretty straightforward for this project. Simply appending a character to the
password in plaintext and then hashing that and comparing it with the hashes that we do know.
Then outputing it. There really wasn't anything difficult about this assignment. Really cool
concepts though using SHA256 and just the concept of hashing in general.
### Part 2 (30 Pts)
This part was pretty straightforward too. I did have trouble comparing strings though before I
noticed that the output included a bunch of stuff other than the hash. Other than that I took a
different approach this time by using a dictionary and essentially creating a hashmap of all of the
hashes with those as keys and the passwords as the values. The flag was CMSC389R-{h@sh1ng_@nd_sl@sh1ng}.

 
