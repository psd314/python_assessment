import csv
import sqlite3

con = sqlite3.connect("imdb.db")
c = con.cursor()

c.execute('DROP TABLE IF EXISTS imdb')

with open('movie_metadata.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    is_header = True
    qs = ""
    for row in reader:
        if is_header:
            header_cols = ', '.join(row)
            qs = ', '.join(['?']*len(row))
            c.execute(f'CREATE TABLE imdb ({header_cols});')
            is_header = False
        else:
            with con:
                c.execute(f'INSERT INTO imdb VALUES ({qs})', tuple(row))
