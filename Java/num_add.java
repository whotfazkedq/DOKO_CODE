package Java;
import java.util.Scanner;
public class num_add {
    public static void main(String[]args) {
        Scanner kb = new Scanner(System.in);
        System.out.println("two numbers adition ");
        System.out.print("enter first number: ");
        float num1 = kb.nextFloat();
        System.out.print("enter second number: ");
        float num2 = kb.nextFloat();
        float sum = num1 + num2;
        System.out.println(num1 + " + " + num2 + " = " + sum);
        kb.close();
    }
}