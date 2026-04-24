
#!/usr/bin/env bash

mkdir -p data/output

for file in data/input/avg_case/*; do
    echo "Processing $file..."
    [ -f "$file" ] || continue
    name=$(basename "$file")
    python3 -m main "$file" > "data/output/avg_case/${name%.*}.txt"
done