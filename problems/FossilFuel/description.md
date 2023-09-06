# Fossil Fuel
You are babysitting and dino nuggets are for dinner! The kids are jeolous though and will only eat if they all get the same amount of food. Given the number of kids to feed and a list of the size of the dino nuggets left in the bag, determine the maximum amount you can feed the kids such that they all eat the same amount. 

# Input
Input will be provided in the following format:

```
<numKidsToFeed>
<nuggetSizes>
```

* The first line, `numKidsToFeed` will contain an integer
* The second line, `nuggetSizes`, will be a space separated list of integers that denotes the size of each dino nugget available to serve the kids

# Constraints

* All kids must eat the same amount of food, not necessarily the same number of nuggets though. For example, 1 nugget of size 2 is the same amount of food as 2 nuggets of size 1.
* Nuggets cannot be split into pieces. For example, a nugget of size 3 cannot be split into a nugget of size 2 and another nugget of size 1.
* Not all nuggets have to be used.
* The number of kids to be fed, k <= 30.
* The length of the list of nugget sizes, n <=30.

# Output
Your output should be the maximum amount of food you can feed each kid. If there is no way to evenly divide the nuggets among all the kids, your output should be 0.

# Examples
The first 3 tests are examples.