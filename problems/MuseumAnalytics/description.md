# Problem Statement
In the historic city of South Jordan, an extraordinary abundance of dinosaur fossils paved the way for the inception of the illustrious Prehistoric Relics Museum. This newfound treasure trove drew global tourists eager to marvel at the exquisite remains. As the newly appointed Museum registrar, your pivotal role now centers around the quest to unveil the visitors' most beloved dinosaur. Thus, you embarked on a survey, inviting patrons to submit their cherished dinosaur choices. The survey results are elegantly presented: one response per line, with each response listing dinosaurs separated by commas. Now, the challenge awaits: can you identify the dinosaur that truly captivates the most hearts? (Note: It is guaranteed that there will be no ties.)


# Input
The first line contains the number of responses `N`.  
Each of the next `N` lines contain a list of dinosaur names of arbitrary size, separated by comma `,`.  
Note: The dinosaur names may contain lowercase and uppercase letters, spaces, and hyphens.

```
N
<dinosaur 1>,<dinosaur 2>,<dinosaur 3>
<dinosaur 1>,<dinosaur 2>
<dinosaur 1>,<dinosaur 2>,<dinosaur 3>,...<dinosaur 10>
...
<dinosaur 1>
```

# Constraints
- It is guaranteed that there will be just one most beloved dinosaur, i.e., there will be no ties.
- It is guaranteed the list of beloved dinosaurs submitted by the visitors is valid, i.e., it does not contain any duplicates.
- 1 <= N <= 10^4
- 1 <= |the total of number of dinosaurs submitted each visitor| <= 10
- 1 <= |the total of number of unique dinosaurs| <= 10^4
- 5 <= |the length of the name of a dinosaur| <= 25


# Output
On the first line, print the name of the most beloved dinosaur.  
On the second line, print the number of people it is beloved for, i.e., the number of votes.
```
<beloved dinosaur>
<votes received by the beloved dinosaur>
```

# Examples
The first 3 test cases are examples.
