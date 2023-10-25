# T-Rex Typing
The t-rex is known for many things, but its typing ability is not one of them. With only two fingers on each hand, it's pretty challenging to type on a standard QWERTY keyboard! 

Rather than deal with the positions and the resulting awkward movements on a standard keyboard, Tipo the t-rex uses an ortholinear (gridlike) keyboard. This keyboard is a 7 by 12 grid, with 2 home row keys on each half of the center row (with 2 empty keys between). Here is a visual representation of the keyboard's shape:

[https://drive.google.com/file/d/1nd9PmZK6p7U2pqn2r3XRQue31MgNZibb/view?usp=share_link](https://drive.google.com/file/d/1nd9PmZK6p7U2pqn2r3XRQue31MgNZibb/view?usp=share_link)

To further compensate for the lack of finger dexterity, before typing anything, Tipo remaps the keys on his keyboard based on what he needs to type, such that his fingers move as little as possible. Tipo measures distance as the real distance between the center of each key.

Additionally, Tipo found that pressing two keys simultaneously was too much of a hassle. Thus, Tipo has [sticky keys](https://en.wikipedia.org/wiki/Sticky_keys) enabled. Instead of needing to hold shift to type a capital letter, Tipo taps shift to turn on sticky keys, then taps a key to get the shifted version. Sticky keys turns off after the letter is typed, so Tipo would need to press shift again to type a second capital letter.

Apart from capital letters, every character has its own dedicated key. For example, Tipo will type an exclamation point with a dedicated `!` key, rather than pressing `SHIFT + 1`.

Here is a visual representation of what one keyboard layout might be. Note that not every key is used:

[https://drive.google.com/file/d/1OEEn0LrV3VvnlPPewOCN7wtFDpwk_BVi/view?usp=share_link](https://drive.google.com/file/d/1OEEn0LrV3VvnlPPewOCN7wtFDpwk_BVi/view?usp=share_link)

Finally, Tipo found it too easy to lose his place when trying to move from one key to the next without returning his fingers to the home row. After every keypress (including shift), the finger that pressed a key returns to its original position on the home row. Tipo's fingers rest at the positions that correspond to d, f, j, and k on a standard QWERTY keyboard. More formally:

* Fingers rest on the same row
* Fingers from the same hand rest on adjacent keys
* There are two keys between the index fingers

Given a body of text, determine the minimum total distance that Tipo's fingers will travel, assuming he places the keys optimally.

## Input
Input consists of a single line containing a string $s$, the text to be typed by the t-rex.

## Constraints
* $0 < |s| \leq 10^6$
* Input will consist of lowercase and uppercase letters, numbers, spaces, and various punctuation marks. All characters will fit on Tipo's 70-key keyboard (69 keys of characters, 1 key for shift).

## Output
A single decimal number representing the minimum distance that Tipo's fingers must travel. Your answer can have a difference of at most $0.001$ from the solution.

## Notes
* Each key is a 1 unit square and shares its edges with the four keys adjacent to it
* Distance between keys is measured from center to center
* The keyboard has as many columns and rows as you decide

## Examples
The first three test cases are the following examples.

### Example 0
#### Input
```
asdf
```

#### Output
```
0.0
```

#### Explanation
With two fingers on each hand, the letters can be placed under the fingers' resting positions, requiring no movement, like so:
```
+---+---+---+---+---+---+
| a | s |   |   | d | f |
+---+---+---+---+---+---+
```

### Example 1
#### Input
```
peter piper picked a peck of pickled peppers
```

#### Output
```
34.0
```

#### Explanation
This is just one of many possible layouts:
```
+---+---+---+---+---+---+
| a | t |   |   | k | d |
+---+---+---+---+---+---+
| p | e | i | c | _ | r |
+---+---+---+---+---+---+
| o | f |   |   | l | s |
+---+---+---+---+---+---+
```
*Note*: for illustrative purposes, `_` represents a space

### Example 2
#### Input
```
O Romeo, Romeo, wherefore art thou Romeo?
```

#### Output
```
36.0
```

#### Explanation
This is one possible layout:
```
+---+---+---+---+---+---+
| a | f |   |   | u | ? |
+---+---+---+---+---+---+
| o | e | m | ^ | _ | r |
+---+---+---+---+---+---+
| w | t |   |   | h | , |
+---+---+---+---+---+---+
```
*Note*: for illustrative purposes, `_` represents a space, and `^` represents `SHIFT`
