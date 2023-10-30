# Dinosaur Agriculture

Stan the Stegosaurus has become tired of foraging for food all the time, and wants to start his own garden. Stan loves having variety in his diet, so he wants as many possible types of plants in his garden. Stan also gets very hungry, so he wants to use as much of his available garden area as possible.

The garden will contain a number of planting boxes, and there can be at most one type of plant per box. Planting boxes can not overlap, and must be entirely contained in the available garden area. Additionally, the planting boxes can not be rotated, as they are designed to have optimal growth in only one orientation.

Variety is of utmost importance to Stan, so he will prioritize a higher number of planting boxes over a lower amount of unused space.

This is all getting very confusing for Stan, so he has asked you to figure out the highest number of planting boxes he can fit into his garden given the size of the available space for the garden and the sizes of all the planting boxes available.

# Input

The first line of input contains three integers, $H$, $W$, and $N$, the height and width of Stan's garden, and how many planting boxes he has.
The next $N$ lines each contain two integers $h$ and $w$, the height and width of one of Stan's planting boxes.

# Output

Output two integers on a single line, the number of planting boxes and the amount of unused space in an optimal arrangement of Stan's garden.

An optimal arrangement has the highest possible number of planting boxes. If there are multiple arrangements with the same number of planting boxes, one with more area used by planting boxes is more optimal.

# Constraints

* $1 \leq H, W \leq 12$
* $1 \leq h \leq H$
* $1 \leq w \leq W$
* $0 \leq N \leq 20$
* $1 \leq H \times W \leq 12$
* Planting boxes must be placed in Stan's garden axis-aligned and on unit lines, and can not be rotated.

# Examples

The first 2 test cases are examples.
