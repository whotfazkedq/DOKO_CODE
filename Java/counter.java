package DOKO_CODE;
import java.util.Scanner;
import java.util.Random;
import java.util.InputMismatchException;

public class counter { 
    public static void main(String[] args) throws InterruptedException {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        int timesReached = 0; 

        System.out.print("Enter the number of times to reach the objective: ");
        int maxObjectives = 0;

        
        try {
            maxObjectives = scanner.nextInt();
        } catch (InputMismatchException e) {
            System.out.println("Error: Please enter a valid integer.");
            scanner.close();
            return; 
        }

        while (true) {
            int objectiveTime = random.nextInt(10) + 1;
            int counter = 1; 

            System.out.println("\nNew Objective: " + objectiveTime + " seconds");

            
            while (counter <= objectiveTime) {
                System.out.println("Counter: " + counter + " seconds");
                Thread.sleep(1000);
                counter++;
            }
            
            timesReached++;
            System.out.println("Objective Reached " + timesReached + " times");
            
            if (timesReached >= maxObjectives) {
                System.out.println("Objective time reached, " + maxObjectives + " times");
                break;
            }
        }
        scanner.close();
    }
}