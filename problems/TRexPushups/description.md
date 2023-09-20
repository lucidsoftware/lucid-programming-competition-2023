# Problem Statement

Bob, the T-Rex, is tired of skipping upper body day. He'd like to do more pushups. One problem: he's got a big head and little arms. Bob has never been one to give up though, so he's devised a plan to get gains. He knows a place that has a lot of holes in the ground from some recent meteor strikes. He can do pushups by these holes because his head can fit in them and his arms can actually touch the ground. His head is 4 ft long, so each hole needs to be at least 4 ft deep. Unfortunately, Bob is self-conscious, so he never wants to go to the same hole twice.

The terrain is given as an array of integers, where `terrain[i]` is the elevation in ft at index `i`. Bob needs at least a 4 ft difference between elevations. Additionally, Bob only ever faces forward when doing pushups, so `terrain[i] - terrain[i+1] >= 4`. (-4 would not count)

How many places does Bob have to do pushups?

# Input

The input will be formatted in the following way:

```
n
10 6 2 3 1
```

Where **n is the length of the array**.

# Ouput

Output an integer which represents the number of place Bob can do pushups (as defined above)

```
2
```

# Constraints

```
0 < n <= 10000
0 <= terrain[i] <= 10000
```

# Examples

## Example input #1:

```
5
1 2 3 4 5
```

## Example output #1:

```
0
```

## Example input #2:

```
10
10 6 2 6 10 6 1 0 10 0
```

## Example output #2:

```
5
```
