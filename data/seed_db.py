import csv
import sqlite3

con = sqlite3.connect("imdb.db")
c = con.cursor()

with open('movie_metadata.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    is_header = True
    qs = ""
    for row in reader:
	# get columns from header
        if is_header:
            header_cols = ', '.join(row)
	    # prepare part of insert string based on length of columns in table
            qs = ', '.join(['?']*28)
            c.execute(f'CREATE TABLE IF NOT EXISTS imdb ({header_cols});')
            is_header = False
        else:
            with con:
                c.execute(f'INSERT INTO imdb VALUES ({qs})', tuple(row))
