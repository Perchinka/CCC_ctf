#include <string.h>
#include <stdio.h>

void win() {
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);

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
	vulnerable();

	return 0;
}