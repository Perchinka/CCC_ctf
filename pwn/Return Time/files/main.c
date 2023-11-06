#include <string.h>
#include <stdio.h>

void win() {
	puts("How did you get here?!\n Ok, get your flag");
	system("cat flag.txt"); 
    return;
}

void vulnerable(){
    puts("> ");

	char buffer[16];
	gets(buffer);
    return;
}

int main() {
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);
	
	vulnerable();

	return 0;
}