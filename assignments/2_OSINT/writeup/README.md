## Writeup 2 - OSINT

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (45 pts)

1. Elizabeth Moffet

2. She is a Banking CEO at Elite Banking at 1337 Haxor. Url is 1337bank.money

3. Twitter: found with checkusernames.com. The user follows CSEC and they follow her back
   GitHub: found with checkusernames.com
   Email: v0idcache@protonmail.com found at 1337bank.money
   Location: She lives in the Netherlands found on Twitter
   Languages: She speaks English and Dutch also found from her first tweet on Twitter which was in twitter
   
4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
   142.93.136.81: | Location: Amsterdam |  Bought from Namecheap Inc. on February 6th and hosted on DigitalOcean | I found the information by looking up the URL on Security Trails 
   and identifying the historical data as well as using shodan to identify the server location

5. Flag found in robots.txt and hidden_directory: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
   Flag found on index page in comments: Good find! CMSC389R-{h1dd3n_1n_plain_5ight}
   
6. 0022: OpenSSH is running on this port. Found during a lookup on shodan of the IP addresses.
   0080: Werkzeug httpd is running on this port. Found during a lookup on shodan of the IP addresses.
   1337: waste service. Found when running a nmap on the IP address. Used "nmap -p 1-2000 142.93.136.81"

7. Ubuntu-4: Found on a lookup of the IP Address via Censys. It was on the SSH comment as well as in the metadata description of the OS

8. Flag found on dns dumpster search under TXT Records: CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}
   Flag found on git master log by downloading the log from the .git subdirectory and downloadin standard files which in this case was logs/refs/heads/master: CMSC389R-{h1d3_s3cret_g1ts}

   
### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*

I first messed around with the stub code. The program was pretty straight forward and the socket thing was really easy to manipulate once you saw it in action. I had at first only used
shodan to find open ports and so that only showed the TCP and HTML ports which I thought was weird. And after running n map I found the missing port: 1337. Now I could run the program.
Another problem I had was that I had a condition to stop only if the output wasn't "Fail". However I found out that sometimes the connection was bad or was dropped which resulted in just
a blank output which would stop the brute force. I didn't realize this for the longest time and because rockyou.txt is so large I had to run it a couple of times before finding out that the
password was linkinpark. The username was pretty straightforward since I assumed v0idcache is probably pretty consistent across all of her accounts. And after entering into the shell, I messed
around and just went into the home directory where I found flag.txt which showed the flag: CMSC389R-{brut3_f0rce_m4ster}. 

