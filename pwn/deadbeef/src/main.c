#include <stdio.h>
#include <string.h>

int main(){
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    int var;
    int check = 0x12341234;
    char buf[40];

    puts("Input>");
    fgets(buf,45,stdin);

    printf("\n[buf]: %s", buf);
    printf("[check]: %p\n", check);

    if (check != 0xdeadbeef){
        printf("\nNope, change payload :D \n");
    }
    else{
        puts("You won, here is you flag");
        system("cat ./flag.txt");
    }

    return 0;
}