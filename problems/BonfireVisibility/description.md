# Bonfire Visibility

Daisy the Dinosaur was playing with some rocks and sticks and somehow discovered fire! She then decided to make a bonfire to rest at with all her dinosaur friends. However, after they all sat down, she noticed that some of her friends accidentally sat down in front of other friends. Help Daisy start fixing this situation by counting the number of her dinosaur friends can see the fire.

A dinosaur is considered to be blocking another dinosaur if it lies exactly on the straight line from the bonfire to the other dinosaur. If a dinosaur is not blocked by any other dinosaur, it can be counted as seeing the bonfire, no matter how far away it is.

## Input

The input begins with two integers separated by a space corresponding to the (x, y) position of the bonfire. This is followed on a new line by an integer corresponding to the number of dinosaurs around the bonfire. Then for each dinosaur, there will be a line with the (x, y) position of the dinosaur formatted the same as the bonfire position.

```
<Bonfire x position> <Bonfire y position>
<Number of dinosaurs>
<1st dinosaur's x position> <1st dinosaur's y position>
<2nd dinosaur's x position> <2nd dinosaur's y position>
...
<Nth dinosaur's x position> <Nth dinosaur's y position>
```

## Constraints
* No dinosaurs will have the same (x, y) position
* No dinosaur will have the same (x, y) postition as the bonfire
* All given positions will be integer values
* The number of dinosaurs will be between 1 and 10000 (inclusive)
* The x and y coordinates of the bonfire and dinosaurs will be between -1,000,000 and 1,000,000 (inclusive)

## Output

The expected output is a single number corresponding to the number of dinosaurs that can see the bonfire.

## Examples

The first 4 test cases are examples.