#!/bin/sh

input_file="../ex03/hh_positions.csv"
tail -n +2 "$input_file" | while IFS= read -r line
do
    date=$(echo "$line" | cut -d',' -f2 | cut -d'T' -f1 | tr -d '"')
    
    if [ ! -f "${date}.csv" ]; then
        head -n 1 "$input_file" > "${date}.csv"
    fi
    
    echo "$line" >> "${date}.csv"
done