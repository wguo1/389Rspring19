/*
 * Name: *PUT YOUR NAME HERE*
 * Section: *PUT YOUR SECTION NUMBER HERE*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *PUT YOUR NAME HERE*
 */

/* your code goes here */

char *a_fmt(int x) {
	return ("a = %d\n", x);
}

int main() {
	int a = 0x1ceb00da;
    int b = 0xfeedface;
	
	printf("a = %d\n", a);
	printf("b = %d\n", b);

    a = a ^ b;
    b = b ^ a;
    a = a ^ b;

    printf("a = %d\n", a);
	printf("b = %d\n", b);
    
    return 0;
}
