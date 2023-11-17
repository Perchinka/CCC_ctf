#include <stdio.h>
#include <string.h>

int main(){
	setbuf(stdout, NULL);
       	setbuf(stdin, NULL);
       	setbuf(stderr, NULL);

        char pass[9] = "89231456\x00";
        char buf[9];
        printf("Input password:\n");
        scanf("%s", buf);
        if(!strcmp(pass, buf)){
                printf("Login ok!!!\n"); 
                system("cat flag.txt");
	}
        else{ 
                printf("FAIL...\n");
	}
}
