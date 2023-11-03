#include <stdio.h>
#include <string.h>

int main(){
	setbuf(stdout, NULL);
       	setbuf(stdin, NULL);
       	setbuf(stderr, NULL);

        char pass[9] = "password\x00";
        char buf[9];
        printf("Input password:\n");
        scanf("%s", buf);
        if(!strcmp(pass, buf)){
                printf("Login ok!!! *flag_replaced*\n");
	}
        else{ 
                printf("FAIL...\n");
	}
}
