#include <stdio.h>
#include <math.h>

int main(){
    double a, b, c;
    puts("Right-Angled Triangle Hypotenuse Calculator");
    printf("Enter the value of leg a: ");
    scanf("%lf", &a);
    printf("Enter the value of leg b: ");
    scanf("%lf", &b);
    c = sqrt((a*a)+(b*b));
    printf("The value of the Hypotenuse of the Triangle is: %lf\n", c);
    return 0;
}