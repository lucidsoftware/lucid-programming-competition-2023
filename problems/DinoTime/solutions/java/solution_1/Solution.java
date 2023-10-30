import java.util.Scanner;

public class Solution {
    static int maxSize = 1;
    static int m = 0;
    static int n = 0;

    public static void main(String[] args) {
        // parse input
        Scanner scan = new Scanner(System.in);
        String[] sizes = scan.next().split(",");
        m = Integer.parseInt(sizes[0]);
        n = Integer.parseInt(sizes[1]);
        scan.nextLine(); // get rid of first line's newline character
        char[][] map = new char[m][n];
        int startRow = 0;
        int startCol = 0;
        for (int i = 0; i < m; ++i) {
            String line = scan.nextLine();
            for (int j = 0; j < n; ++j) {
                map[i][j] = line.charAt(j);
                if (map[i][j] == '@') {
                    startRow = i;
                    startCol = j;
                }
            }
        }

        // print parsed map
        // for (int i = 0; i < m; ++i) {
        // System.out.println();
        // for (int j = 0; j < n; ++j) {
        // System.out.print(map[i][j]);
        // }
        // }

        // step in first 4 directions
        map[startRow][startCol] = '.';
        // up
        if (startRow > 0) {
            step(1, 0, startRow - 1, startCol, deepcopy(map), 1, 0);
        }
        // right
        if (startCol < n - 1) {
            step(1, 0, startRow, startCol + 1, deepcopy(map), 1, 0);
        }
        // down
        if (startRow < m - 1) {
            step(1, 0, startRow + 1, startCol, deepcopy(map), 1, 0);
        }
        // left
        if (startCol > 0) {
            step(1, 0, startRow, startCol - 1, deepcopy(map), 1, 0);
        }
        System.out.println(maxSize);

        return;
    }

    public static void step(int size, int energy, int currRow, int currCol, char[][] map, int stepsTaken,
            int tummyValue) {
        // base cases
        // ran out of energy
        if (energy < 0) {
            maxSize = Math.max(maxSize, size);
            return;
        }
        // Took too many steps
        if (stepsTaken > 10) {
            maxSize = Math.max(maxSize, size);
            return;
        }

        // process current space
        char currSpace = map[currRow][currCol];
        // Invalid space
        if (!canTraverse(currSpace)) {
            maxSize = Math.max(maxSize, size);
            return;
        }
        // Another dino
        if (Character.isLetter(currSpace)) {
            if (dinoSize(currSpace) > size) { // too big
                maxSize = Math.max(maxSize, size);
                return;
            } else { // eat em
                tummyValue += dinoSize(currSpace);
                // grow
                if (tummyValue >= size) {
                    tummyValue -= size;
                    size += 1;
                    energy = size;
                }
            }
        } else { // some other kind of traversable terrain
            energy -= energyToTraverse(currSpace);
        }

        // step in first 4 directions
        map[currRow][currCol] = '.';
        // up
        if (currRow > 0) {
            step(size, energy, currRow - 1, currCol, deepcopy(map), stepsTaken + 1, tummyValue);
        }
        // right
        if (currCol < n - 1) {
            step(size, energy, currRow, currCol + 1, deepcopy(map), stepsTaken + 1, tummyValue);
        }
        // down
        if (currRow < m - 1) {
            step(size, energy, currRow + 1, currCol, deepcopy(map), stepsTaken + 1, tummyValue);
        }
        // left
        if (currCol > 0) {
            step(size, energy, currRow, currCol - 1, deepcopy(map), stepsTaken + 1, tummyValue);
        }
        return;
    }

    // yeah, not sure how java does this. So I wrote my own...
    private static char[][] deepcopy(char[][] thingToCopy) {
        char[][] result = new char[thingToCopy.length][];
        for (int i = 0; i < thingToCopy.length; ++i) {
            result[i] = thingToCopy[i].clone();
        }
        return result;
    }

    private static boolean canTraverse(char c) {
        if (c == '#' || c == '^' || c == '&') {
            return false;
        } else {
            return true;
        }
    }

    private static int dinoSize(char c) {
        return c - 'A' + 1;
    }

    private static int energyToTraverse(char c) {
        if (c == '~' || c == '"') {
            return 2;
        } else if (c == '*') {
            return 3;
        } else {
            return 1;
        }
    }

}

/*
 * Brainstorm:
 *
 * State
 * size
 * energy
 * coordinate
 * current map
 * number of steps taken
 * current value of dinos in tummy
 * Function
 * base cases:
 * energy is 0 (note current size)
 * 11th step (note current size)
 * process current space
 * lose energy
 * Eat dino
 * possibly grow and reset energy
 * Explore move in 4 directions
 * Helper functions:
 * map alphabet to numbers
 * map terrain to numbers
 * Possible memo:
 * if map is same, coordinate is same, energy is <= previous,
 * number of steps taken <= previous, current value of dinos in tummy <=
 * previous
 */