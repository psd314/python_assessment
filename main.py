import sqlite3
from modules.data_helpers import query_db, calculate_profit_column

def run():
	con = sqlite3.connect('data/imdb.db')
	query = 'SELECT * FROM imdb'
	df = query_db(query, con)
	df = calculate_profit_column(df)
	print(pd.isna(df.profit[0]).any())
if __name__ == '__main__':
	run()
