import csv
import sys

# Usage:
#   python quote_tags_force.py tags.csv quoted_tags.csv

def quote_tags(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as fin, \
         open(output_file, "w", newline="", encoding="utf-8") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar='\\')

        header = next(reader, None)
        if header:
            writer.writerow(header)

        for row in reader:
            if not row or len(row) < 4:
                continue
            userId, movieId, tag, timestamp = (
                row[0].strip(),
                row[1].strip(),
                row[2].strip(),
                row[3].strip(),
            )
            # Manually wrap the tag in quotes
            tag = f'"{tag}"'
            writer.writerow([userId, movieId, tag, timestamp])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python quote_tags_force.py <input.csv> <output.csv>")
        sys.exit(1)
    quote_tags(sys.argv[1], sys.argv[2])
    print(f" Wrote quoted CSV to {sys.argv[2]}")
