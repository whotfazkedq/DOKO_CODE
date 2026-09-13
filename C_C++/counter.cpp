#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main(void){
    int objective_time;
    int counter;
    int times_reached = 0;
    int max_objectives;
    printf("Enter the maximum number of objectives to reach: ");
    scanf("%d", &max_objectives);

    srand((unsigned int)time(NULL));

    while(1){
        objective_time = rand() % 50 + 1;
        counter = 0;

        printf("\nNew Objective: %d seconds\n", objective_time);

        while(counter <= objective_time){
            printf("Counter: %d seconds\n", counter);
            sleep(1);
            counter++;

        }
        times_reached++;
        printf("Objective Reached %d times\n", times_reached);
        if (times_reached >= max_objectives){
            printf("Objective time reached, %d times\n", max_objectives);
            break;
        }

    }
    return 0;
}