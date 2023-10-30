# Problem Statement

As a scientist you are studying the eating patterns of dinosaurs. You have assembled lists of dinosaurs that are eaten by predator. You are curious about the length of the longest food chain possible given the chains of predators to prey. 

# Input
The input will be formatted in the following way:
```
N
A <- B, C
D <- F
....
{predator name} <- {list of prey names separated by ", "}
```

where $N$ is the number of lines in the input and the dinosaur before the arrow is the predator of the dinosaurs after the arrow.

# Output
Output the length of the longest chain

# Constraints
- $0 < N \leq 100$
- Inputs will not have cycles
- Names of dinosaurs can have multiple letters 

# Examples

The first 2 test cases are examples.