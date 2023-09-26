# Desert Discovery

You are a paleontologist-turned-programmer working at a prolific new dig site in the Western United States. Each of the fossils that is unearthed requires careful and painstaking cleaning and inspection.
For each fossil, a specialist has recorded key characteristics and qualitative attributes of the fossil and has assigned it a unique identifier. Your task is to use these observation records to automatically classify each fossil into its most likely species, or flag it as belonging to a hitherto undiscovered species.

You will be given a list of known common dinosaur species in the area and the key attributes of fossils known to belong to each of those species. You will then be given a list of recently discovered fossils along with their observed attributes. For each fossil, you will need to output the most likely species this fossil belongs to by computing a likelihood score.

The likelihood score of a species match should be computed as follows. First, compute the number of matching attributes $M$ as the number attributes exhibited by the fossil that are also on the known list of attributes for fossils of that species. Then, compute the number of non-matching attributes $N$ as the the number of attributes exhibited by the fossil that are *not* on the known list of attributes for fossils of that species. Finally, compute the likelihood score of a match with $100 * (M - N) / K$, where $K$ represents the number of known attributes for fossils of the species.

Using this formula, a perfect match would receive a score of $100$. If a fossil does not receive a minimum score of $50$ for any of the given species, then you should classify it as a `Possible New Discovery` so that an expert paleontologist can more closely study it for clues about its possible origins. You should note that a likelihood score may be negative in the case that there are more non-matching attributes than matching attributes.

# Input
- You will first be given the total number of species.
- Then, for each species, you will be given its name, followed by the number of key attributes it has.
- Each attribute will then be listed on its own line.
- Following the species list, you will be given a similar list of fossils requiring classification.
- The fossils list begins with the total number of fossils.
- Then, for each fossil, you will receive the number of observed attributes, followed by the observed attributes themselves.

```
<Total Number of Species>
<Species Name (A)>
<Num Attributes for A>
<Attribute>
<Attribute>
...
<Species Name (B)>
<Num Attributes for B>
<Attribute>
<Attribute>
...
<Total Number of Fossils>
<Fossil X Num Attributes>
<Attribute>
<Attribute>
...
<Fossil Y Num Attributes>
<Attribute>
<Attribute>
```

# Constraints
* The total number of species will be between $1$ and $500$
* The total number of fossils will be between $1$ and $1000$
* The species name and attribute names will consist of alphanumeric characters and may contain spaces
* The species name and attribute names will be no longer than 250 characters in length
* The number of attributes for a species or fossil will be between $1$ and $50$
* There will be no "ties" for the most likely species. Specifically if there exists any species with a likelihood score greater than or equal to $50$, then there will exist exactly one species which has the largest likelihood score
* Species names will be unique

# Output
- For each fossil, output the name of the species that has the highest likelihood score.
- However, if no species has a likelihood score of $50$ or greater, you should instead output `Possible New Discovery`.


```
<Species Name>
<Species Name>
Possible New Discovery
...
<Species Name>
```
