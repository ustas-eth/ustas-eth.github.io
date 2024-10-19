#!/bin/bash

# Read the input file
input_file="content/posts/zk-bootcamp/index.md"

# Counter for weight
weight=1

# Read the file line by line
while IFS= read -r line; do
  if [[ $line =~ ^##[[:space:]]Day[[:space:]][0-9]+ ]]; then
    # Extract day number
    day_number=$(echo "$line" | sed -E 's/^## Day ([0-9]+).*/\1/')
    
    # Create folder for the day
    folder_name="content/posts/zk-bootcamp/day-$day_number"
    mkdir -p "$folder_name"
    
    # Create index.md file for the day
    output_file="$folder_name/index.md"
    
    # Add title and weight to the beginning of the file
    echo "---" > "$output_file"
    echo "title: \"Day $day_number\"" >> "$output_file"
    echo "weight: $weight" >> "$output_file"
    echo "---" >> "$output_file"
    echo "" >> "$output_file"
    
    # Increment weight for next day
    ((weight++))
  fi
  
  # Append content to the current day's file
  if [[ -n "$output_file" ]]; then
    echo "$line" >> "$output_file"
  fi
done < "$input_file"

echo "Splitting complete. Day folders and files have been created."
