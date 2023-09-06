import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        //parse input
        Scanner scan = new Scanner(System.in);
        int length = scan.nextInt();
        int[] terrain = new int [length];
        for (int i = 0; i < length; ++i) {
            terrain[i] = scan.nextInt();
        }

        int pushupLocations = 0;
        
        for (int i = 0; i < length - 1; ++i) {
            if (terrain[i] - terrain[i + 1] >= 4) {
                ++pushupLocations;
            }
        }
        System.out.println(pushupLocations);
        return;
    }
}