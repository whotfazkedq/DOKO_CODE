#include <stdio.h>
#include <math.h>

int main(){
    double a, b, c;
    puts("Calculadora de la Hipotenusa de un Triangulo Rectangulo");
    printf("Ingrese el valor del cateto a: ");
    scanf("%lf", &a);
    printf("Ingrese el valor del cateto b: ");
    scanf("%lf", &b);
    c = sqrt((a*a)+(b*b));
    printf("El valor de la Hipotenusa del Triangulo es: %lf\n", c);
    return 0;
}