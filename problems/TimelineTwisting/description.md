# Timeline Twisting

While popular media has shown certain species of dinosaurs as having lived during the same time period, in many cases these representations aren't accurate. Some species evolved from others (and thus necessarily must come later in the timeline), and others could never have existed simultaneously because of environmental factors (and thus necessarily must exist either earlier or later in the timeline).

You have a list of dinosaur species, the duration of time that each species is known to have existed, and any number of logical constraints on when a species could have existed relative to another species. Between two species $A$ and $B$, there are two possible constraints:

* $1$: $A$ existed before $B$
* $2$: $A$ existed after $B$

Determine the shortest length of time necessary such that all the dinosaur species could have existed in a logically consistent way.


## Input
The first line of input contains two space separated integers:

* $N$: the amount of dinosaur species
* $C$: the number of constraints

The second line of input contains $N$ space separated integers. Call this sequence of numbers $D$. $D_i$ is the duration of time that species $i$ existed.

The next $C$ lines each contain 3 space separated integers:

* $x$: the first species
* $y$: the second species
* $z$: the constraint between species $x$ and $y$

```
N C
D_1 D_2 ... D_N
x_1 y_1 z_1
x_2 y_2 z_2
...
x_C y_C z_C
```

## Constraints
* All numbers are integers
* $1 \leq N \leq 10^3$
* $0 \leq C \leq N * (N - 1)$
* $1 \leq D_i \leq 10^6$
* $0 \leq x, y < n$
* $z \in Set(\{1, 2\})$
* There will always be at least one logically consistent way for all the dinosaur species to have existed

## Output
A single integer: the minimum amount of time required for all the species to have existed in a logically consistent way.


## Examples
The first 3 test cases are the following examples.

### Example 0
#### Input
```
2 1
9 5
0 1 1
```

#### Output
```
14
```

#### Explanation
```
[   0   ][ 1 ]
        9    14
```


### Example 1
#### Input
```
3 1
3 10 5
0 2 1
```

#### Output
```
10
```

#### Explanation
```
[0][ 2 ]
[   1    ]
  3    8 10
```

### Example 2
#### Input
```
3 2
5 3 3
2 1 2
0 2 1
```

#### Output
```
8
```

#### Explanation
```
[1]  [2]
[ 0 ]
  3 5  8
```
