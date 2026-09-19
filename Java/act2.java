package Java;
import java.util.Scanner;

public class act2 {
    public static void main(String[] args){
        Scanner waza = new Scanner(System.in);
        System.out.print("Inserte un numero del 0 al 127: ");
        byte num1 = waza.nextByte();
        System.out.println("Tu numero es: "+num1);

        System.out.print("Ingresa cualquier numero: ");
        int num2 = waza.nextInt();
        System.out.println("tu segundo numero es: "+num2);

        waza.close();
    }
}
