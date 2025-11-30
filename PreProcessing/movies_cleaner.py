import csv
import sys
from pathlib import Path

def movies_cleaner(inp_path, out_path, encoding="utf-8"):
    with open(inp_path, "r", encoding=encoding, newline="") as fin, \
         open(out_path, "w", encoding=encoding, newline="") as fout:
        reader = csv.reader(fin, delimiter=",", quotechar='"', escapechar="\\")
        writer = csv.writer(
            fout,
            delimiter=",",
            quotechar='"',
            escapechar="\\",
            quoting=csv.QUOTE_NONNUMERIC,
            lineterminator="\n"
        )

        for rownum, row in enumerate(reader, start=1):
            if not row:
                continue 
            if len(row) < 3:
                raise ValueError(f"Row {rownum} has fewer than 3 fields: {row}")

            movie_id_raw, title_raw, genres_raw = row[0], row[1], row[2]
            try:
                movie_id = int(movie_id_raw.strip())
            except ValueError:
                raise ValueError(f"Row {rownum}: movieID is not an integer: {movie_id_raw!r}")
            title = title_raw.strip()
            genres = genres_raw.strip()
            genres = "|".join(part.strip() for part in genres.split("|"))
            writer.writerow([movie_id, title, genres])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python movies_cleaner.py movies.csv cleaned_movies.csv")
        sys.exit(1)
    inp, out = sys.argv[1], sys.argv[2]
    movies_cleaner(inp, out)

    print(f"Wrote corrected movies CSV to {out}")