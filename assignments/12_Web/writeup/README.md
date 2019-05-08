# Web Writeup

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (40 Pts)

The flag is CMSC389R-{y0u_ar3_th3_SQ1_ninj@}. I figured it was SQL Injection off of the hint.
I then proceeded to do the classic SQL Injection: 1' OR TRUE'. This ended up getting the SQL
Injection Detection error. So I figured that there is probably a filter or a WAF up. I tried
a bunch of methods found off of OWASP and modified it. Eventually I used "|| '1". But this didn't
work either which was strange. Then I remembered that SQL was done with two apostrophe so I wasn't
closing off the first apostrophe. So after I used "'|| '1" it finally worked

### Part 2 (60 Pts)
The first task was a simple injection injection. I used the following: "<script>alert()</script>"

The second task I used a link and attached it with the javascript command: "<a href = 'javascript:alert()'>Click me</a>"
and then I clicked the link to execute the script

The third task was messing with the url. The "onerror" function raises an error whenever an image is
not found or corrupt. So I used this since the injection obiviously wouldn't correspond to an image: 
https://xss-game.appspot.com/level3/frame#3' onerror = alert();'

The fourth task was messing with the script for the timer. I used what I knew about SQL Injection
and how it was common to comment things out. Then I just applied it here with the following: "1') || alert()//"

The fifth task was kind of a combination of previous tasks and was pretty trivial. I modified the next query
in the url link to : "javascript:alert()"

The sixth task was actually pretty hard. I did a lot of searching. I also used the hints and got the file
path for "google.com/jsapi?callback=foo". So I just had to figure out how to use it. Then I saw in the description
for XMLHttpRequest. Then I noticed that the url was https. After searching I figured out that http was vulnerable
to JS external files and this can be bypassed on https by using "//". The final url comes to: 
https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert




