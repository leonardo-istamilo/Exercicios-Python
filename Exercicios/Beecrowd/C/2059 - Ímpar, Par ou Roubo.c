#include <stdio.h>

int main(){
    int p, j1, j2, r, a;  

    scanf("%d %d %d %d %d", &p, &j1, &j2, &r, &a);

    if (r == 1){
        if (a == 1){
        printf("Jogador 2 ganha!\n");
        }
        else if (a == 0){
            printf("Jogador 1 ganha!\n");
        }
    }
    else if (r == 0 ){
        if (a == 1){
            printf("Jogador 1 ganha!\n");
        }
        else   {
           if (p == 1){
                if ((j1 + j2) % 2 == 0){ 
                printf("Jogador 1 ganha!\n");
                }
                else{
                    printf("Jogador 2 ganha!\n");
                }
            }
            else{
                    if ((j1 + j2) % 2 == 0){ 
                printf("Jogador 2 ganha!\n");
                }
                else{
                    printf("Jogador 1 ganha!\n");
                }
   }    
        }
    }
    return 0;
}