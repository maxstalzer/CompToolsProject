import csv
import sys

# Usage: python quote_links.py links.csv quoted_links.csv

def quote_links(input_file, output_file):
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
            # movieId numeric (unquoted), imdb/tmdb strings (quoted automatically)
            writer.writerow([int(movieId), imdbId, tmdbId])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python quote_links.py <input.csv> <output.csv>")
        sys.exit(1)
    quote_links(sys.argv[1], sys.argv[2])
    print(f"Wrote {sys.argv[2]}")
