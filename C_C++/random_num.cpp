#include <stdio.h>
#include <stdlib.h>

int readInt(const char* prompt){
    int val;
    int res;
    int c;
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

int main(){
    int min, max, num;
    char choice;
    
    puts("Random Number Generator");
    min = readInt("Enter the minimum value: ");
    max = readInt("Enter the maximum value: ");

    num = min + rand() % (max - min + 1);
    printf("Your random number is: %d\n", num);
    do{
        
        printf("Would you like to generate another random number? (y/n): ");
        scanf(" %c", &choice);
    
        if(choice == 'y' || choice == 'Y'){
            main();
        } else if(choice == 'n' || choice == 'N'){
            puts("Closing");
        } else {
            puts("Invalid choice, select yes or no");
        }
    } while (choice != 'y' && choice != 'Y' && choice != 'n' && choice != 'N');
    return 0;
}