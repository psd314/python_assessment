import pandas as pd

def query_db(query, con):
	return pd.read_sql_query(query, con)
