# Dino Chess
It has been a few hundred years but the chess developers have decided to finally update the game by adding a new piece, the dino. The dino can move similarly to the king in eight directions but unlike the king it moves `m` squares (but not less than `m` squares) and can jump over other pieces. (When a dino moves each position must change by either `+m`, `-m`, or `0` but both position changes can not be `0`.)

With the addition of the new piece folks have started thinking about how this piece will interact with the board and the question of what is the maximum amount of non-attacking dinos that can be placed on an `n` x `n` board is asked. A non-attacking dino is one such that none of the squares it attacks occupy another dino. 

Given a dino that can move `m` squares on an `n` by `n` board, what is the maximum amount of non-attacking dinos that can be placed on a single board?

# Input
Input will be provided in the following format:

```
<m> <n>
```

* The first (and only) line will contain two space-separated numbers
    * The first number, `m`, is an integer denoting the number of squares the dino can move
    * The second number, `n`, is an integer denoting the size of the board (`n` x `n`)
   
# Constraints
* `1 < m <= n <= 1000`
* `m` and `n` will be integers

# Output
Your output should be a single integer denoting the maximum amount of non-attacking dinos you can place on an `n` by `n` board.

# Examples
The first 3 tests are examples.
