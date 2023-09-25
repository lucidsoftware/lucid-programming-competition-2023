# Most Recent Common Ancestor
Your colleagues at the Prehistoric Relics Museum are making an effort to group dinosaur exhibits by evolutionary relationships. As one of the paleontologists on call, they frequently ask you to consult your phylogenetic trees to figure out how closely related two different dinosaurs are. In the interest of saving time that you would rather devote to actual field work, you decide to write a program for them to compute most recent common ancestry.

# Input
```
<N>
<Ancestor> -- <Descendant>
....
<Ancestor> -- <Descendant>
<First>
<Second>
```

The first line contains a single positive integer N. The following N lines contain the names of two dinosaur clades (groups or types), separated by spaces and hyphens as depicted above. These lines indicate that the clade on the left is the immediate ancestor of the clade on the right. The next (and last) two lines each contain the name of a single
clade.

# Constraints
- 1 <= N <= 1,000
- The ancestry relationships given will form a single, rooted tree.
  - There are no cycles.
  - Every clade, expect for the root, will have exactly one ancestor. (No test case will have anastomosis.)
  - Any two clades, except for the root, will have exactly one most recent common ancestor in the tree.
- Neither of the two clades named at the end of the input will be an ancestor, direct or indirect, of the other.

# Output
Output a single line with the name of the clade that is the most recent common ancestor of the two dinosaurs named at the end of the input.

- A clade is a common ancestor if it is an ancestor of both clades named at the end of the input.
- A clade is the most recent common ancestor if is a common ancestor and also not an ancestor of any other common ancestor.

# Examples
The first 4 tests are examples.
