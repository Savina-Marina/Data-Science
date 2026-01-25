#!/bin/sh
head -1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv | while IFS= read -r line; do
    name=$(echo "$line" | cut -d',' -f3)
    clean_name=$(echo "$name" | tr -d '"')
    
    level="-"
    echo "$clean_name" | grep -qi "junior" && level="Junior"
    echo "$clean_name" | grep -qi "middle" && level="Middle" 
    echo "$clean_name" | grep -qi "senior" && level="Senior"
    
    echo "$line" | awk -F',' -v l="\"$level\"" '{$3=l; print}' OFS=',' >> hh_positions.csv
done