import csv
import sys

def ratings_cleaner(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", newline="") as fin, \
         open(output_file, "w", encoding="utf-8", newline="") as fout:

        reader = csv.reader(fin)
        writer = csv.writer(
            fout,
            lineterminator="\n",
            quoting=csv.QUOTE_NONE,
            escapechar="\\"
        )

        header = next(reader, None)
        if header:
            writer.writerow(["userId", "movieId", "rating"])  

        for row in reader:
            if len(row) < 3:
                continue

            userId = row[0].strip()
            movieId = row[1].strip()
            rating = row[2].strip()

            writer.writerow([userId, movieId, rating])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ratings_cleaner.py <input.csv> <output.csv>")
        sys.exit(1)

    ratings_cleaner(sys.argv[1], sys.argv[2])
    print(f"Wrote cleaned CSV to {sys.argv[2]}")
