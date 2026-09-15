#include <stdio.h>
#include <stdlib.h>

int main(){
    int min, max, num;
    puts("Random Number Generator");
    printf("Enter the minimum value: ");
    scanf("%d", &min);
    printf("Enter the maximum value: ");
    scanf("%d", &max);
    num = min + rand() % (max - min + 1);
    printf("Your random number is: %d\n", num);
    printf("Would you like to generate another random number? (y/n): ");
    char choice;
    scanf(" %c", &choice);
    if(choice == 'y' || choice == 'Y'){
        main();
    } else {
        return 0;
    }
    return 0;
}