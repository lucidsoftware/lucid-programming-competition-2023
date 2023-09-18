# Timeline Twisting

While popular media has shown certain species of dinosaurs as having lived during the same time period, in many cases these representations aren't accurate. Some species evolved from others (and thus necessarily must come later in the timeline), and others could never have existed simultaneously because of environmental factors (and thus necessarily must exist either earlier or later in the timeline).

You have a list of dinosaur species, the duration of time that each species is known to have existed, and any number of logical constraints on when a species could have existed relative to another species. Between two species $A$ and $B$, there are three possible constraints:
* $1$: $A$ existed before $B$
* $2$: $A$ existed after $B$
* $3$: $A$ existed either before or after $B$

Determine the shortest length of time necessary such that all the dinosaur species could have existed in a logically consistent way.


## Input
The first line of input contains two space separated integers:
* $n$: the amount of dinosaur species
* $c$: the number of constraints

The second line of input contains $n$ space separated integers. Call this sequence of numbers $d$. $d_i$ is the duration of time that species $i$ existed.

The next $c$ lines each contain 3 space separated integers:
* $x$: the first species
* $y$: the second species
* $z$: the constraint between species $x$ and $y$

```
n c
d0 d1 ... d(n-1)
x0 y0 z0
x1 y1 z1
...
x(c-1) y(c-1) z(c-1)
```

## Constraints
* All numbers are integers
* $1 \leq n \leq 10^3$
* $0 \leq c \leq n * (n - 1)$
* $1 \leq d_i \leq 10^6$
* $0 \leq x, y < n$
* $z \in \Set{1, 2, 3}$
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
0 2 3
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
or
```
    5  8
[ 2 ][0]
[   1    ]
         10
```

### Example 2
#### Input
```
3 2
5 3 3
2 1 2
0 2 3
```

#### Output
```
8
```

#### Explanation
This arrangement is logically consistent, but not the shortest:
```
[1][2][ 0 ]
  3  6    11
```

Since the order of species 0 and 2 doesn't matter, we can do this instead:
```
[1]  [2]
[ 0 ]
  3 5  8
```
