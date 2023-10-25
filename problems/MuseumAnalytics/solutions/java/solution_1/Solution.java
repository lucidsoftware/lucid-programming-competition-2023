import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numResponses = scanner.nextInt();
        scanner.nextLine();
        int belovedDinosaurVotes = 0;
        String belovedDinosaurName = "";
        HashMap<String, Integer> dinosaurVotes = new HashMap<>();
        for (int i = 0; i < numResponses; i++) {
            String[] dinosaurs = scanner.nextLine().split(",");
            for (String dinosaur : dinosaurs) {
                dinosaurVotes.put(dinosaur, dinosaurVotes.getOrDefault(dinosaur, 0) + 1);
                if (dinosaurVotes.get(dinosaur) > belovedDinosaurVotes) {
                    belovedDinosaurVotes = dinosaurVotes.get(dinosaur);
                    belovedDinosaurName = dinosaur;
                }
            }
        }
        System.out.println(belovedDinosaurName);
        System.out.println(belovedDinosaurVotes);
    }
}