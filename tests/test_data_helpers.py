from python_assessment.modules.data_helpers import (
	query_db, 
	calculate_profit_column,
	parse_genres,
	get_most_profitable_directors,
	get_genre_ratings)
import sqlite3
import pandas as pd

class TestDataHelpers():
	def test_query_db(self):
		con = sqlite3.connect('data/imdb.db')
		df_db = pd.read_sql_query('SELECT * FROM imdb', con)
		df_func = query_db('SELECT * FROM imdb', con)
		con.close()
		assert df_db.shape == df_func.shape
		assert df_db.iloc[-1,0] == df_func.iloc[-1,0]
		assert df_db.columns[-1] == df_func.columns[-1]

	def test_calculate_profit_column(self):
		con = sqlite3.connect('data/imdb.db')
		df = pd.read_sql_query('SELECT * FROM imdb', con)
		df_ = df
		df_profit = calculate_profit_column(df_)
		con.close()
		
		for i in range(df_profit.shape[0]):
			gross_df = pd.to_numeric(df.gross[i])
			budget_df = pd.to_numeric(df.budget[i])
			profit_df = (gross_df-budget_df)/budget_df
			
			# verify that calculations from raw data df
			# returned by calculate_profit_column function
			if not pd.isna(df_profit.loc[i, 'profit']):
				assert profit_df == df_profit.loc[i, 'profit']	

	def test_get_most_profitable_directors(self):
		con = sqlite3.connect('data/imdb.db')
		df = pd.read_sql_query('SELECT * FROM imdb', con)
		con.close()
		df_ = df
		df_ = calculate_profit_column(df_)
		directors = get_most_profitable_directors(df_)
		
		# loop through directors and verify their totals are correct with
		for d in directors.index.values:
			assert df_.profit[df_.director_name==d].sum() == directors[d]

	def test_parse_genres(self):
		con = sqlite3.connect('data/imdb.db')
		df = pd.read_sql_query('SELECT * FROM imdb', con)
		con.close()
		df_, genre_cols = parse_genres(df)
			
		row_genres = df.genres[0].split('|')
		# check if genres are correctly mapped to columns
		for r in genre_cols:
			if r in row_genres:
				assert df_.loc[0, r] == True
			else:
				assert df_.loc[0, r] == False


	def test_get_genre_ratings(self):
		con = sqlite3.connect('data/imdb.db')
		df = pd.read_sql_query('SELECT * FROM imdb', con)
		con.close()

		df_, genre_cols = parse_genres(df)
		scores = get_genre_ratings(df_, genre_cols)

		worst_genre = scores.index[0]
		worst_genre_scores = df_[df_[worst_genre]==True]
		worst_score = worst_genre_scores['imdb_score'].mean()
		
		assert worst_score == scores[0]
		
