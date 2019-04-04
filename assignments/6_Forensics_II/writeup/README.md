Name: William Guo 
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: William Guo

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?
   185.199.110.153

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

3. What are the hackers' IP addresses, and where are they connecting from?
   159.203.113.181. They are connecting from a server on the 10th floor of New York, NY

4. What port are they using to steal files on the server?
   20 

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,
	find_me.jpeg
	
    a) What kind of file is it?
	   JPEG File
	
    b) Where was this photo taken? Provide a city, state and the name of the building in your answer.
	   Punta del Este, Uruguay. Sculpture is The Fingers of Punta del Este
	
    c) When was this photo taken? Provide a timestamp in your answer.
	   December 12th 2018 at 17:16:24

    d) What kind of camera took this photo?
	   An iPhone 8 back camera

    e) How high up was this photo taken? Provide an answer in meters.
	   4.572631836 m

6. Which file did the attackers leave on the server?
   greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
   I would add additonal passwords or some kind of administrative privelege in order to export or import files. Also I would hash the password
   and salt it as well to make the password harder to crack.

### Part 2 (55 Pts)

    1. When was `greetz.fpff` generated?
	   It was generated on 2019-03-27 00:15:05
    2. Who authored `greetz.fpff`?
	   It was authored by fl1nch
    4. List each section, giving us the data in it *and* its type.
	   
	   Section Type: SECTION_ASCII
	   Hey you, keep looking :)

	   Section Type: SECTION_COORD
       (52.336035, 4.880673)

	   Section Type: SECTION_PNG
       PNG File written to image.png

       Section Type: SECTION_ASCII
       }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
	   CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}

       Section Type: SECTION_ASCII
       Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=
	   
    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.
       The first flag was directly in the section text as: CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
	   The second flag I found was in the PNG image. It was CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}
	   The third flag I found was the last section. I translated it to a base64 format and got back
	   CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}

