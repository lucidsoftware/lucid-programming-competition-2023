# Hunting Grounds
T-Rex divvy up their hunting grounds into rectangular plots each day. The map of the hunting grounds is an $N$ by $N$ grid. Each grid cell is assigned a hunting value and the hunting value of a plot is the sum of the cells it covers. Rexy is hungry after escaping the shattered plains and wants to get a good plot. He will ask you for the total hunting value of many different rectangular plots.

Rexy will give you the ($y$, $x$) coordinates of the top left and bottom right corners of the rectangle he is interested in. He chose the order $y$ then $x$ because in most dinosaur programming languages you index a 2D array as `grid[y][x]`. The coordinates are inclusive and 1 indexed. The origin, ($1$, $1$), is in the top left.

## Input
- The first line of input will have two integers, $N$ and $Q$, the dimension of the $N \times N$ hunting grounds grid and the number of queries Terry will give you.
- The next $N$ lines will each have $N$ space separated integers, $G_{ij}$. This is the hunting grid.
- The next $Q$ lines will each have 4 space separated integers, `y1 x1 y2 x2`, the coordinates of the query's rectangle corners.

## Constraints
* $1 \leq N \leq 1000$
* $1 \leq Q \leq 10^5$
* $0 \leq G_{ij} \leq 1000$
* $1 \leq x1, y1 \leq x2, y2 < N$

Note, the constraints on $N$ and $G_{ij}$ imply the total sum of a grid should never exceed 1 billion.

## Output
Your output should have $Q$ lines (one for each query).
Each line should have the sum total hunting value of that rectangle of the grid.

## Examples
The first 3 test cases are these examples.

### Example 0
#### Input
```
6 3
6 1 3 4 5 2
2 3 1 1 1 1
4 7 2 1 9 3
0 1 0 9 2 3
9 9 7 9 9 3
2 3 2 7 8 1
2 2 3 4
1 1 1 1
3 5 6 6
```
#### Output
```
15
6
38
```
#### Explanation
The first query, `2 2 3 4` means a pair of (y, x) coordinates (2, 2) and (3, 4) representing this rectangle with sum to 15.
```
3 1 1
7 2 1
```
The second query is just the top left square, `6`.
The third query, (3, 5) to (6, 6), is this rectangle in the bottom right with sum 38.
```
9 3
2 3
9 3
8 1
```

### Example 1
#### Input
```
1 1
7
1 1 1 1
```
#### Output
```
7
```
#### Explanation
This 1x1 grid is the smallest possible.
This is the only query possible on a 1X1 grid.

### Example 2
#### Input
```
4 6
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
1 1 2 3
1 2 2 3
1 1 1 4
4 4 4 4
1 4 4 4
1 1 4 4
```
#### Output
```
24
18
10
16
40
136
```
#### Explanation
The first query is this rectangle with sum 24:
```
1  2  3
5  6  7
```
The second query is this rectangle with sum 18:
```
2 3
6 7
```
The third query is the top row with sum 10.

The fourth query is the bottom right corner, 16.

The fifth query is the right column with sum 40.

The sixth query is the whole grid with sum 136.
