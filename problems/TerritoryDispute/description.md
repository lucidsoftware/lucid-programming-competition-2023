# Territory Dispute

Dinosaurs may be territorial, but that doesn't mean they can't be civilized. The dinosaur council is having problems assigning territory to its members, and it needs your help to make the final decision as to which pieces of land will be given out individually and which pieces will be made public by the council.

The dinosaurs have compiled a list of potential territories to give out, noting the total size of each. You have been enlisted to find the grouping of territories that will cause the least strife between all of the dinosaurs while still leaving enough public land to be enjoyed by everyone.

In other words, you need to find one territory for each dino such that the difference between the smallest and largest territories handed out is minimized while keeping the sum of the unused territories at least as large as the required size.

## Input
The first line of input will contain three space separated integers:

* N: the number of pieces of land
* D: the number of dinosaurs that need territory
* S: the minimum size of land that must be left over for the council

The remaining lines of input will each contain a single integer representing the size of a piece of land.

```
<N> <D> <S>
<L_1>
<L_2>
...
<L_N>
```

## Output
A single integer: the minimum difference between the smallest and largest territories handed out while still meeting the requirement for left over land.

## Constraints
- $0 < N \leq 10^6$
- $0 < D \leq N$
- $0 \leq S \leq 2 \times 10^9$

The total size of land will never exceed $2 \times 10^9$

The problem will always have at least one solution that gives every dinosaur land and leaves enough left over for the council.

## Examples
The first <2> test cases are samples.