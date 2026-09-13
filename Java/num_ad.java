package DOKO_CODE;
import java.util.Scanner;
public class num_ad {
    public static void main(String[]args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("two numbers adition: ");
        System.out.print("enter first number: ");
        float num1 = scanner.nextFloat();
        System.out.print("enter second number: ");
        float num2 = scanner.nextFloat();
        float sum = num1 + num2;
        System.out.println(num1 + " + " + num2 + " = " + sum);
        scanner.close(); 
    }
}