from python_assessment.modules.data_helpers import (
	query_db, 
	calculate_profit_column,
	parse_genres)
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
		df_profit = calculate_profit_column(df)
		con.close()

		gross_df = pd.to_numeric(df.gross[0])
		budget_df = pd.to_numeric(df.budget[0])
		profit_df = (gross_df-budget_df)/budget_df

		gross_df_prof = df_profit.gross[0]
		budget_df_prof = df_profit.budget[0]
		profit_df_prof = (gross_df_prof-budget_df_prof)/budget_df_prof

		assert profit_df == profit_df_prof 
		assert pd.isna(df_profit.profit).any() == False

	def test_parse_genres():
		con = sqlite3.connect('data/imdb.db')
		df = pd.read_sql_query('SELECT * FROM imdb', con)
		con.close()
		pass
