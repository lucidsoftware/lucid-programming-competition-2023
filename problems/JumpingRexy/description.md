# Problem Statement

Rexy the dino is stuck on the shattered plains with large gaping canyons in the ground. He needs to find the shortest path out which may require jumping over several of the canyons. As T-Rex aren't good jumpers, Rexy can only make 5 jumps over canyons. What is the shortest distance out of the plains using at most 5 jumps?

You are given a map of the plains represented as a grid where each spot of land is either a plain (P), canyon (C), or boulder (B). Rexy cannot climb on or go through boulders, and his starting location will be marked with a D. Rexy can exit the plains via any P on any edge of the map (the borders).

Calculate the shortest distance Rexy needs to travel to exit the plains while making at most 5 jumps over canyons.

Note: Rexy can only jump one canyon (one letter marked as 'C') with one jump and a single jump does not need to end in a 'P'. That is, Rexy can use multiple jumps, back to back, to cross multiple, back to back, canyons. For example, two jumps can be used to go from 'A' to 'B' in 'A C C B'.

# Input

- The first line contains $N \times M$ describing the size of the rectangular grid.
- Followed by $N$ lines containing $M$ space separated characters each.
- Each cell of the grid is one of the following characters:
    - 'P': A plain that Rexy can walk on.
    - 'C': A canyon that Rexy needs to jump over.
    - 'B': A boulder that Rexy cannot traverse.
    - 'D': Rexy's starting location.
- The grid will always contain exactly one 'D' (Rexy's starting point) and at least one 'P' along the edge (exit point).

```
7 5
B C B B P
B C C P P
B P P C C
B B P P B
B P P C C
B D C C P
B B B B B
```

# Output

- Return an integer representing the shortest distance Rexy needs to travel to exit the plains using at most 5 jumps over canyons. If it's not possible to exit the plains with 5 or fewer jumps, return -1.

```
3
```

# Constraints

- $0 \leq N, M \leq 100$
- There will always be at least one path from 'D' to a 'P' along the edge of the grid.
- Rexy can make at most 5 jumps over canyons.

# Example

## Example input #1:

```
5 5
P P P P P
B B B B P
B B B B P
B B B B P
B B B B D
```

## Example output #1:

```
1
```

## Example input #2:

```
6 6
P P P P P P
B C C C C B
B B B B C B
B B B B C B
B B B B C B
B B B B D B
```

## Example output #2:

```
5
```
