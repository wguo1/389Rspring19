# Crypto II Writeup

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (70 Pts)
The commands I used were 

"gpg --import key.asc"
"gpg --decrypt message.txt.gpg"


The flag is CMSC389R-{m3ss@g3_!n_A_b0ttl3}

### Part 2 (30 Pts)

1. It is pretty evident that the ecb file is much less discrete than the cbc file.
You can still see the general shape in the ecb file but in the cbc file it is pretty
much impossible to get the original shape.
2. The ecb is much less secure specifcally because it is encrypted across a uniform
key. There is no changes across the entire picture so even though the pixels aren't the
same, uniformally they changed at the same rate. Whereas with cbc there is alot more unpredicatabilty.
For the most part each pixel has it's own key which is xor by the previous result. Thus there is alot
more disruption and therefore more secure.


