#!/bin/bash
read N
read -a terrain

count=0

for ((j = 0; j < N - 1; j++)); do
    if ((terrain[j] - terrain[j + 1] >= 4)); then
        ((count++))
    fi
done

echo $count
