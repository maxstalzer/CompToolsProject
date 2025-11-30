import csv
import sys

def links_cleaner(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as fin, \
         open(output_file, "w", newline="", encoding="utf-8") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)

        header = next(reader, None)
        if header:
            writer.writerow(header)

        for row in reader:
            if not row or len(row) < 3:
                continue
            movieId, imdbId, tmdbId = row[0].strip(), row[1].strip(), row[2].strip()

            writer.writerow([int(movieId), imdbId, tmdbId])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python links_cleaner.py <input.csv> <output.csv>")
        sys.exit(1)
        
    links_cleaner(sys.argv[1], sys.argv[2])
    print(f"Wrote {sys.argv[2]}")
