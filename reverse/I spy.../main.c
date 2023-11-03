#include <stdio.h>
#include <string.h>

void win(){
    printf("You won, flag is \"CCC{n0_guess_g4mes}\" \n");
}

int main(){
    char pass[20];

    printf("I'm not sure how to play this game, but I spy something...\n");
    gets(pass);
    if(strcmp(pass, "CCC{n0_guess_g4mes}") == 0){
        win();
    }
    else{
        printf("No \n");
    }

    return 0;
}