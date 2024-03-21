import java.util.Scanner;

public class Task1 {

    static Scanner scan = new Scanner(System.in); 
    public static void main(String[] args) {

        System.out.println("The distance bw the 2 points is: " + inputsOfDegrees());

    }

    private static double inputsOfDegrees(){

        System.out.println("Enter the two point cordinates langs: ");

        double x1 = Math.toRadians(scan.nextDouble());
        double y1 = Math.toRadians(scan.nextDouble());
        System.out.println("Enter the two point cordinates longs: ");

        double x2 = Math.toRadians(scan.nextDouble());
        double y2 = Math.toRadians(scan.nextDouble());

        return 6371.01 * Math.acos(Math.sin(x1) * Math.sin(x2) + Math.cos(x1) * Math.cos(x2) * Math.cos(y1 - y2));
    } 
}
