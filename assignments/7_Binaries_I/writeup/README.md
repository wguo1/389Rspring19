# Writeup 7 - Binaries I

Name: William Guo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: William Guo

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf("int a = 0x1ceb00da;
    int b = 0xfeedface;
    
	
	printf("a = %d\n", a);
	printf("b = %d\n", b);

    a = a ^ b;
    b = b ^ a;
    a = a ^ b;

    printf("a = %d\n", a);
	printf("b = %d\n", b);
    
    return 0;");
```

### Part 2 (10 Pts)
This program switches the 2 numbers given using multiple XORs.
