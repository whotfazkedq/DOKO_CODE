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
    return 0;
}