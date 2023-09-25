# Problem Statement

Many dinosaurs survive by eating other dinosaurs, in this problem we want to determine the longest chain of dinosaurs from herbivore to apex predator.

# Input
The input will be formatted in the following way:
```
N
A <- B, C
D <- F
....
{predator} <- {list of preys separated by ", "}
```

Where $N$ is the number of lines in the input and the dinosaur before the arrow is the predator of the dinosaurs after the arrow.

# Output
Output the length of the longest chain

# Constraints
- $0 < N \leq 100$
- Inputs will not have cycles

# Examples

## Example input #1:
```
3
A <- B, C
B <- C
C <- D
```

## Example output #1:
```
4
```

## Example input #2:
```
12
A <- B
B <- C
C <- D
D <- E
E <- F
F <- G
G <- H
H <- I
I <- J
J <- K
K <- L
L <- M
```

## Example output #2:
```
13
```