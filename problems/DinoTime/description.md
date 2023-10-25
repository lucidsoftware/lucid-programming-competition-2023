# Dino Time

Born as a teeny lizard in a dino-eat-dino world, you have only one goal: Become the largest dinosaur of them all.

```
+-----------------------------------+
|................~~.......^#########|
|.........AA.....~~.......^#########|
|................~~........^########|
|.........BB.....~~.........^^######|
|................~~..........^^^####|
|....AA..........~~.............^^##|
|.....@A..C......~~...F..F........^^|
|........CCC.....~~.................|
|.........C......~~.....F........Q..|
|................~~.............Q.Q.|
|....""""........~~~................|
|...""""""........~~.........J......|
|....""""..........~~...............|
|..................~~.....G.........|
|.A.A.A............~~~..............|
+-----------------------------------+
```

Given an ASCII map full of dinosaurs and obstacles, calculate the theoretical largest your dino can become. You must traverse this land, eating as much as you can, and plan your path accordingly to prevent starvation.

## Rules of Dino-land

- You start as `@` with a dino of size 1 and energy 1 and leave dry ground `.` at the starting point.
- You can only eat dinosaurs with a size less than or equal to your current size.
- You cannot eat or travel to dinosaurs larger than yourself, or they'd eat you.
- In order to grow by one, you must eat dinosaurs whose total combined sizes of equal to your current size. For example, if you are a dinosaur of size 5, you can eat five dinosaurs of size 1, two dinosaurs of sizes 2 and 3, or one dinosaur of size 5.
- Excess dinosaurs eaten stay in your tummy, meaning their values carry over when you grow.
- Dinosaurs disappear when they are eaten, leaving dry ground `.` behind.
- Whenever you eat a dinosaur, your energy resets to the max.
- Your max energy is equal to the size of your dinosaur.
- If you can't find anything to eat, your dinosaur will die.
- Moving between tiles takes between 1 and 3 energy, depending on the tile.
- Not all land is passable, meaning that you must find your way around the rocks and trees.

## Dino-time Legend

| char          | description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| `@`           | You, a tiny little dinosaur of size 1                                                  |
| `A-Z`         | Other dinosaurs to be eaten, size corresponds to the letter: A -> 1, B-> 2, ... Z-> 26 |
| `#`, `^`, `&` | Rocks and trees, cannot traverse                                                       |
| `~`, `"`      | rivers and tall grass, takes 2 energy to traverse                                      |
| `*`           | spiky bushes, take 3 energy to navigate                                                |
| `.`           | dry ground, takes 1 energy to traverse                                                 |

# Input

The first line of input specifies the number of rows $M$ and the number of columns $N$. The following lines contain the map data.

```
<M>,<N>
<row 1>
<row 1>
...
<row M>
```

Here are some valid inputs:

The following contains 5 rows and 5 columns

```
5,5
.....
.@...
...~~
...~A
ABA~C
```

The following contains 10 rows and 8 columns

```
10,8
........
.@......
........
........
~~...^^.
~~...^^.
~~......
.....CDC
........
."""....
```

# Constraints

- Dinosaurs can only move orthogonally, with no diagonal movements. Square roots haven't been invented yet.
- If you start a move with 0 energy, then you die of starvation.
- The board is guaranteed to have a starting dino and it is guaranteed to be valid, i.e., there will be no malformed input.
- The board size will never exceed (10, 10).
- Your dino cannot walk more than 10 steps regardless of your energy, as 11 hasn't been invented yet.

# Output

Print the maximum possible size for your dinosaur before its inevitable death.

# Examples

```
5,5
.....
.....
..@..
.ABD.
.....
```

Output: `1`

```
7,7
@AAAAAA
......D
.......
.......
.......
.......
.......
```

Output: `5`
