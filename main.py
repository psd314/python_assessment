import sqlite3
import pandas as pd
from modules.data_helpers import (
	query_db, 
	parse_genres,
	calculate_profit_column,
	get_most_profitable_directors,
	get_genre_ratings)

def run():
	con = sqlite3.connect('data/imdb.db')
	query = 'SELECT * FROM imdb'
	df = query_db(query, con)
	df = calculate_profit_column(df)
	directors = get_most_profitable_directors(df)

	print('\nTop 10 Directors By Profitability\n')
	print(directors)

	genre_df, genre_cols = parse_genres(df)
	print("\nBONUS! The 10 Genres you DON'T want to see.")
	print("Worst performing average imdb scores by genre")
	print(get_genre_ratings(genre_df, genre_cols))
if __name__ == '__main__':
	run()
