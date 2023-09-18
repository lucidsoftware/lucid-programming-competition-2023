# Dino Time

Born as a teeny lizard in a dino-eat-dino world, you have only one goal: Become the largest dinosaur of them all.

```
+-----------------------------------+
|................~~       ^#########|
|.........AA.....~~       ^#########|
|................~~        ^########|
|.........BB.. ..~~         ^^######|
|................~~          ^^^####|
|....AA..........~~             ^^##|
|.....@A..C..... ~~   F  F        ^^|
|........CCC.....~~                 |
|.........C......~~     F        Q  |
|................~~             Q Q |
|....""""........~~~                |
|...""""""........~~         J      |
|....""""..........~~               |
|..................~~     G         |
| A A A............~~~              |
+-----------------------------------+
```

Given an ascii map full of dinos and obstacles, calculate the theoretical largest your dino can become. You must traverse
this land, eating as much as you can, and plan your path accordingly to prevent starvation.

## Rules of Dino-land

- You start as `@` with a dino size of 1
- You can only eat dinosaurs with a size less than or equal to your current size
  - You cannot eat dinosaurs larger than yourself, or they'd eat you
- In order to grow by one, you must eat a total size of dinos equal to your current size

  - Example: \
     If you are a dinosaur of size 5, you can eat 5 dinos of size 1, or 2 dinos of size 2 and 3, or 1 dinosaur of size 5.
  - Excess dinosaurs eaten stay in your tummy, meaning their values carry over.

- Dinos disappear when they are eaten, leaving dry ground `.` behind
- Your max energy is the equal to the size of your dinosaur
- If you can't find anything to eat, your dinosaur will die.
  - Moving tiles takes between 1 - 3 energy, depending on the tile,
- Not all land is passable, meaning that you must find your way around the rocks and trees

## Dino-time Legend

| char          | description                                                                         |
| ------------- | ----------------------------------------------------------------------------------- |
| `@`           | You, a tiny little dinosaur of size 1                                               |
| `A-Z`         | Other dinos to be eaten , size corresponds to the letter: A -> 1, B-> 2, ... Z-> 26 |
| `#`, `^`, `&` | Rocks and trees, cannot traverse                                                    |
| `~`, `"`      | rivers and tall grass, takes 2 energy to traverse                                   |
| `*`           | spiky bushes, take 3 energy to navigate                                             |
| `.`           | dry ground, takes 1 energy to traverse                                              |

# Input

Input will be piped into your program, with the first line given specifying the row,column count of the upcoming map

Here's some valid input for example:

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

- Dinosaurs can only move orthogonally, no diagonal movements. Square roots haven't been invented yet.
- If you start a move with 0 energy, then you die of starvation
- Every board has a starting dino and all boards are valid, no need to handle malformed input
- Boards will never exceed (10, 10)

# Output

Your problem output should be the maximum possible size for your dinosaur before it's inevitable death.

# Examples

The first 2 tests are examples.

```
4,4
@....
A....
B....
C....
```

Output: `5`

```
4,4
@..~.
A..~.
.D.~~
BD..~
```

Output: `3`
