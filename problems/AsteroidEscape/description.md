# Asteroid Escape
An asteroid is set to collide with the planet Earth!
We want a dinosaur to survive the collision, because dinosaurs are awesome (duh!).
To survive this collision, our chosen allosaurus must find high ground to survive the incoming tsunamis and earthquakes.
However, it must also collect enough food to make the journey and survive while residing on high ground.
Luckily, the allosaurus has excellent speed and scavenging abilities.
It just needs to know the best path forward, which we can help calculate!

You are given the numbers $n$, $m$ representing the number of vertices, edges respectively.
You are also given a number $f$ representing the amount of food necessary to survive your journey.
There exist vertices $1,2,$\dots$,n$ representing the locations you can visit on your journey.
Vertex 1 is the starting point of the allosaurus.
Vertex $n$ is the high point on the map, which your dinosaur must reach as quickly as possible.
Each vertex $1,2,\dots,n$ has a food count $f_1, f_2, \dots, f_n$ that the allosaurus collects by being in the vertex (it will always collect food from 1 and $n$).

Additionally, you are given pairs of vertices denoting the edges, which are the paths connecting each vertex.
When given an edge from vertex 1 to 2, you may only travel from 1 to 2 and not vice versa.
In fact, you are guaranteed that any edge from a vertex $i$ will go to some vertex $j$ such that $j > i$.
Using this information, determine the shortest path from vertex 1 to vertex $n$ for the allosaurus such that it collects at least $f$ food.


# Input
* You are given space-separate integers $n, m, f$ denoting the number of vertices, number of edges, and necessary amount of food respectively.
* Next, you are given a line with $n$ space-separated integers $f_1, f_2, \dots, f_n$, each representing the amount of food $f_i$ at vertex $i$. 
* Finally, you are given $m$ lines each containing two space-separated integers $i, j$ such that $i < j$ and vertex $i$ has an edge going into vertex $j$ (but $j$ does not have an edge going into $i$).

```
<n> <m> <f>
<f_1> <f_2> ... <f_n>
<endpoint 1> <endpoint 2>
<endpoint 1> <endpoint 2>
...
<endpoint 1> <endpoint 2>
```

# Constraints
* The number of vertices $n$ is between $2 \leq n \leq 250$
* The number of edges $m$ is between $1 \leq m \leq 15000$
* The amount of food required $f$ is between $0 \leq f \leq 5000$
* If an edge goes from vertex $i$ to vertex $j$, it cannot be used to travel from $j$ to $i$.
* Any edge from a vertex $i$ must go to some vertex $j$ such that $j > i$.
* No edge appears more than once
* There will always be at least one path from vertex 1 to vertex $n$ that collects $f$ food.

# Output
Output the length (edge count) of the shortest path from the starting point (vertex $1$) to the high ground (vertex $n$) such that the allosaurus collects at least $f$ food.
```
<Length of shortest path with at least f food>
```

# Examples
The first 3 test cases are examples.