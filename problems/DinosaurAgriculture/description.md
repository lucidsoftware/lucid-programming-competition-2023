# Dinosaur Agriculture

Stan the Stegosaurus has become tired of foraging for food all the time, and wants to start his own garden. Stan loves having variety in his diet, so he wants as many possible types of plants in his garden. The garden will contain a number of planting boxes, and there can be at most one type of plant per box. Unfortunately, Stan only has limited space to build his garden, so he will have to be smart in how he plans the garden to maximize the variety of plants he can grow. Additionally, the planting boxes have walls of varied heights to optimize how sunlight hits the box, and as such Stan will only put the boxes in his garden in a very particular orientation. Stan gets very hungry, so he wants to fill as much space as possible in his garden and minimize the empty space. However, variety is more important to Stan, so he will prioritize a higher number of planter boxes over a lower amount of unused space. This is all getting very confusing for Stan, so he has asked you to figure out the highest number of planting boxes Stan can fit into his garden given the size of Stan's garden and the sizes of all the planting boxes he has.

# Input

The first line of input contains three integers, $H$, $W$, and $N$, the height and width of Stan's garden, and how many planter boxes he has.
The next $N$ lines each contain two integers $h$ and $w$, the height and width of one of Stan's planter boxes.

# Output

Output two integers on a single line, the number of planter boxes and the amount of unused space in an optimal arrangement of Stan's garden.

# Constraints

* $1 \leq H, W \leq 12$
* $1 \leq h \leq H$
* $1 \leq w \leq W$
* $0 \leq N \leq 20$
* $1 \leq H \times W \leq 12$
* Planting boxes must be placed in Stan's garden axis-aligned and on unit lines, and can not be rotated.

# Examples

The first 2 test cases are examples.
