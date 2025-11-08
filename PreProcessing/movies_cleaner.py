import csv
import sys
from pathlib import Path

def fix_movies_csv(inp_path, out_path, encoding="utf-8"):
    with open(inp_path, "r", encoding=encoding, newline="") as fin, \
         open(out_path, "w", encoding=encoding, newline="") as fout:
        reader = csv.reader(fin, delimiter=",", quotechar='"', escapechar="\\")
        writer = csv.writer(
            fout,
            delimiter=",",
            quotechar='"',
            escapechar="\\",
            quoting=csv.QUOTE_NONNUMERIC,  # quote all non-numeric fields
            lineterminator="\n"
        )

        for rownum, row in enumerate(reader, start=1):
            if not row:
                continue  # skip blank lines
            if len(row) < 3:
                raise ValueError(f"Row {rownum} has fewer than 3 fields: {row}")

            # Take the first three fields; ignore any extras if present
            movie_id_raw, title_raw, genres_raw = row[0], row[1], row[2]

            # Normalize movie_id as int so it stays unquoted on write
            try:
                movie_id = int(movie_id_raw.strip())
            except ValueError:
                raise ValueError(f"Row {rownum}: movieID is not an integer: {movie_id_raw!r}")

            # Strip whitespace around strings
            title = title_raw.strip()
            genres = genres_raw.strip()

            # (Optional) collapse any internal whitespace around genre pipes
            # e.g., "Action | Comedy" -> "Action|Comedy"
            genres = "|".join(part.strip() for part in genres.split("|"))

            # Write back in the exact target format:
            # movieID,"movieName","Genre|Genre"
            writer.writerow([movie_id, title, genres])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python movies_cleaner.py movies.csv cleaned_movies.csv")
        sys.exit(1)
    inp, out = sys.argv[1], sys.argv[2]
    fix_movies_csv(inp, out)
    print(f"Wrote normalized CSV to {out}")
