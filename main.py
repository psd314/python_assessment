import sqlite3
import pandas as pd
from modules.data_helpers import (
	query_db, 
	calculate_profit_column,
	get_most_profitable_directors)

def run():
	con = sqlite3.connect('data/imdb.db')
	query = 'SELECT * FROM imdb'
	df = query_db(query, con)
	df = calculate_profit_column(df)
	directors = get_most_profitable_directors(df)

	print('\nTop 10 Directors By Profitability\n')
	print(directors)
if __name__ == '__main__':
	run()
