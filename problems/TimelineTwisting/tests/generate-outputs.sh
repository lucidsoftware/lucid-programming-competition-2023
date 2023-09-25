#!/bin/bash
for input_file in *.in
do
    IFS='.' read -ra parts <<< $input_file
    test_num=${parts[0]}
    output_file=$test_num.out
    python3 ../solutions/python3/main.py < $input_file > $output_file
done