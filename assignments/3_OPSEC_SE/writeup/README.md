# Writeup 3 - Operational Security and Social Engineering

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (40 pts)

I would act as a customer represenative of the bank that is being compromised with the premise that her account has been broken into

- Hello my name is XYZ and I'm calling because we believe your bank account has been compromised and we need you to reset your info
- Could you please go to this url to reset your security questions and pin number: (give them a fake url that doesn't work)
- Hmmm... that's strange why the website isn't working. What browser are you using?
- Could you try another browser?
- Ok... that's fine we can reset your security questions and pin number over the phone
- Just to confirm we need to verify your identity. What's your email address, your birthdate and birth city, name, etc.
- Alright good now last confirmation so I can access your account is the old pin number so I can reset it
- Thank you. What would you like your new pin number to be
- Awesome now last thing is to reset your security questions just in case
- What's your mother's maiden name?
- What's the name of your first pet?
- What was the color of your first car?
- What elementary school did you attend?
- Ok everything should all be settled now Ms. Moffet. Is this the best phone number to reach if any further communication is needed?
- Good, thank you and have a nice day m'am.

### Part 2 (60 pts)

1. The first issue I would fix is the password since that is probably one of the most important flaws in any system.
If it is something as important as a bank's server the password should not be as easy as "linkinpark". I would recommend
Elizabeth to follow the password guidelines outlined by NIST. Namely guidelines from this website: https://spycloud.com/new-nist-guidelines/.
Also if possible try to match passwords against publicly availible wordlists like rockyou. It is much easier and more convenient to check
upfront and pay a cost rather than risking havoc later on.
2. The second thing I would fix is to hide the git directory by not making it publicly availible. I didn't even know this was possible but
the website still had all of it's source control information in the .git directory. For websites that use private hosting services, it's
dangerous because it provides a false sense of security. Not securing the .git directory means that an adversary could download all of the
files and programs and basically recreate a model. Obviosuly this means there is a working demo where a advesary could attack continously
without anyone knowing. This website https://en.internetwache.org/dont-publicly-expose-git-or-how-we-downloaded-your-websites-sourcecode-an-analysis-of-alexas-1m-28-07-2015/
depicts a bunch of attacks that could be used to expose identities, flaws, hidden directories/files, etc. The best way to defend against this is
to simply modify the configuration of the webservice and to reject access to the .git folder.
3. I would also fix the user interface and the verification of a password. I couldn't see how the password was stored but
it should be salted, encrypted and stored as ciphertext. Otherwise I think there should be a validation check where the user has to reset
the password after X amount of tries. This would make brute force attacks pretty much non existent. This security feature was in the news a couple of
years ago with the iPhone and the San Bernandino shootings. This would hinder a user if they were actually legit but it's a tradeoff for better 
security.