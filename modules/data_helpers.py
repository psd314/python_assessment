import pandas as pd

def query_db(query, con):
	return pd.read_sql_query(query, con)

def calculate_profit_column(df):
	# fillna with a small number to prevent division by zero
	df['gross'] = pd.to_numeric(df['gross']).fillna(1e-7)
	df['budget'] = pd.to_numeric(df['budget']).fillna(1e-7)
	# calculate profitability
	df['profit'] = (df['gross']-df['budget'])/df['budget']
	return df

def parse_genres(df):
	# split genres into indvidual columns and label with True when genre matches index
	genres = df['genres'].str.split('|').apply(lambda x: pd.Series([True]*len(x), index=x))
	genre_cols = genres.columns
	df[genre_cols] = df[genre_cols].fillna(False)

	return df
