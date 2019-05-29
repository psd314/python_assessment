import pandas as pd

def query_db(query, con):
	return pd.read_sql_query(query, con)

def calculate_profit_column(df):
	# fillna with a small number to prevent division by zero
	df['gross'] = pd.to_numeric(df['gross'])
	df['budget'] = pd.to_numeric(df['budget'])
	# calculate profitability
	df['profit'] = (df['gross']-df['budget'])/df['budget']
	return df

def get_most_profitable_directors(df):
	# remove rows with NaN from calculation
	df_ = df.dropna(subset=['profit'])
	# aggregate profitability by summing and sort descending
	df_ = df_.groupby('director_name')['profit'].agg(sum).sort_values(ascending=False)[:10]
	return df_

def parse_genres(df):
	# split genres into indvidual columns and label with True when genre matches index
	genres = df['genres'].str.split('|').apply(lambda x: pd.Series([True]*len(x), index=x))
	genre_cols = genres.columns
	df_ = pd.concat([df, genres], axis=1)
	df_[genre_cols] = df_[genre_cols].fillna(False)

	return (df_, genre_cols)

def get_genre_ratings(df, genre_cols):
	imdb = pd.to_numeric(df['imdb_score'])
	df['imdb_score'] = imdb
	scores = {}
	for g in genre_cols:
		genre = df[df[g]==True]
		scores[g] = genre['imdb_score'].mean()
	return pd.Series(scores).sort_values()[:10]
