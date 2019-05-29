import sqlite3
from modules.data_helpers import query_db

def run():
	con = sqlite3.connect('data/imdb.db')
	query = 'SELECT * FROM imdb'
	df = query_db(query, con)
	print(', '.join(df.columns))
if __name__ == '__main__':
	run()
