# This script only exists to win a bet on the number of languages we could stick in this repo.

# `python3 testcasegen.py --species 10 --fossils 10 --attrs-pool-size 8 --attrs-high 3 > tests/2.in`;
# `python3 testcasegen.py --species 10 --fossils 20 --attrs-pool-size 16 --attrs-high 5 > tests/3.in`;
# `python3 testcasegen.py --species 20 --fossils 30 --attrs-pool-size 16 --attrs-high 6 > tests/4.in`;
# `python3 testcasegen.py --species 25 --fossils 40 --attrs-pool-size 16 --attrs-high 8 --attrs-low 5 > tests/5.in`;
# `python3 testcasegen.py --species 30 --fossils 50 --attrs-pool-size 22 --attrs-high 11 > tests/6.in`;
# `python3 testcasegen.py --species 100 --fossils 100 --attrs-pool-size 32 --attrs-high 21 > tests/7.in`;
# `python3 testcasegen.py --species 200 --fossils 150 --attrs-pool-size 30 --attrs-high 15 > tests/8.in`;
# `python3 testcasegen.py --species 500 --fossils 100 --attrs-pool-size 50 --attrs-high 20 > tests/9.in`;
# `python3 testcasegen.py --species 7 --fossils 1000 --attrs-pool-size 14 --attrs-high 14 > tests/10.in`;
# `python3 testcasegen.py --species 1 --fossils 5 --attrs-pool-size 3 --attrs-high 3 > tests/11.in`;
# `python3 testcasegen.py --species 1 --fossils 1 --attrs-pool-size 10 --attrs-high 10 > tests/12.in`;
# `python3 testcasegen.py --species 1 --fossils 1 --attrs-pool-size 10 --attrs-high 10 > tests/13.in`;


for (0...13){
    `python3 ./solutions/python3/main.py < tests/$_.in > tests/$_.out`;
}