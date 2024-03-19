package LabTask5;

import java.util.*;
public class Graded4 {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int count = 0;

        System.out.println("Enter the amount of numbers: ");
        int n = scan.nextInt();

        System.out.println("Enter numbers: ");
        for (int i = 1; i <= n; i++) {

            int num = scan.nextInt();
            if (num != 0)
                count += 1;
            else
                break;
                

        }

        System.out.println("The nummbers before zero are: " + count);


        
    }
}
