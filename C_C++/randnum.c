#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int readInt(const char* prompt){
    int val, res, c;
    while (1){
        printf("%s", prompt);
        res = scanf("%d", &val);
        if (res == 1){
            break;
        }
        printf("Invalid input, enter numbers only\n");
        while ((c=getchar())!= '\n' && c != EOF);
    }
    return val;
}

int main(void){
    int min, max, count;
    char choice;
    srand((unsigned int)time(NULL));

    puts("Random Number Generator");
    do{
        min = readInt("Enter the minimum value: ");
        max = readInt("Enter the maximum value: ");
    
        while (min > max){
            puts("minimum can't be greater than maximum, try again");
            min = readInt("Enter the minimum value: ");
            max = readInt("Enter the maximum value: ");
        }
        count = readInt("How many numbers do you want to generate?: ");
        while (count <= 0){
            count = readInt("You must select a positive number: ");
        }

        int *nums = malloc(count * sizeof(int));
        if (nums == NULL){
            puts("Counter failed");
            return 1;
        }
        for (int i = 0; i < count; i++){
            nums[i]= min + rand() % (max-min +1);
        }
        printf("Your random numbers are: ");
        for (int i = 0; i < count; i++){
            printf("| %d |", nums[i]);
        }
        printf("\n");

        free(nums);

        printf("Would you like to generate more random numbers? (y/n): ");
        scanf("%s", &choice);
    } while (choice == 'y' || choice == 'Y');
    puts("Closing");
    return 0;
}