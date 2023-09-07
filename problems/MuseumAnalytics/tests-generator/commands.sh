# test case generation
for i in $(seq 1 3); do python tests-generator/main.py > "tests/${i}.in" 2> "tests-generator/${i}.log"; done
# run solution to generate output
for i in $(seq 1 3); do cat "tests/${i}.in" | python solutions/python3/main.py > "tests/${i}.out" ; done
