#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
    int opt[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(opt) / sizeof(opt[0]);
    srand(time(NULL));
    int scoreA = rand() % n;
    int scoreB = rand() % n;
    char teamA[10];
    char teamB[10];
    printf("Enter the name of Team A: ");
    scanf("%s", teamA);
    printf("Enter the name of Team B: ");
    scanf("%s", teamB);

    printf("%s %d:%d %s\n", teamA, opt[scoreA], opt[scoreB], teamB);
    if (scoreA == scoreB){
        printf("match result was a tie\n");
    }
    if (scoreA > scoreB){
        printf("%s won\n", teamA);
    }
    if (scoreA < scoreB){
        printf("%s won\n", teamB);
    }

    printf("Closing");
    
    
    return 0;
}
