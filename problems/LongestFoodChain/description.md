# Problem Statement

Many dinosaurs survive by eating other dinosaurs, in this problem we want to determine the longest chain of dinosaurs from herbivore to apex predator. 

# Input
The input will be formatted in the following way:
```
n
A <- B, C
....
D <- F
```

Where **n is the number of lines in the input file** and the dinosaur before the arrow is the predator of the dinosaurs after the arrow.

# Output
Output the length of the longest chain. ex:

```
5
```

# Constraints
```
0 < n <= 100
Inputs will not have cycles
```

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