# Triceratops Evolution
Triceratops are occasionally mistaken for predators, given their large horns and sturdy build. 
However, they are in reality herbivores who have evolved to gain various defensive traits.
These traits are critical for the survival of the triceratops, as its relatively low speed prevents it from using escape as a means of deterring predators.

Given the importance of these traits in the survival of the triceratops, we are interested in the probability that certain traits get passed on to future generations of triceratops.
You are given three probabilities $p_0,p_1,p_2$ denoting the odds of a child (generation $i$) inheriting the trait, given that zero, one, or two parents (generation $i-1$) have the trait respectively.
Given the probability $g_1$ that any given triceratops of generation 1 has the trait, determine the probability that any given triceratops of generation $N$ will have the trait.


# Input
The input format consists of one integer $N$ along with the four probabilities $g_1, p_0, p_1, p_2$ all on the same line, seprated by space.
We want to know the probability that any given triceratops of generation $N$ has the trait.
$g_1$ is the probability that any triceratops of generation 1 has the trait.
$p_0, p_1, p_2$ are the probabilities that a triceratops of the next generation inherits the trait, given zero, one, or two of its parents had the trait respectively.
```
<N> <g_1> <p_0> <p_1> <p_2>
```

# Constraints
* The target generation $N$ will always be integer values between 2 and 10 (inclusive)
* The probabilities $g_1, p_0, p_1, p_2$ will always be floating point values between 0.0 and 1.0 (inclusive). Each probability will have at most four decimal points of precision.
* When a triceratops of generation $i$ is born, it must have two parents of generation $i-1$

# Output
Output the probability that any given triceratops of generation $N$ has the trait, rounded to 4 decimal places (i.e. 0.275794 => 0.2758). Always print 4 decimal places. For example, 0.5 should be printed as 0.5000
```
<Probability of having trait on generation N>
```

# Examples
The first 3 test cases are examples.