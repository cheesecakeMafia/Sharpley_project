import pandas as pd
import sqlite3

db = sqlite3.connect('candleData.db')
dfs = pd.read_excel('minute_candle.xlsx', sheet_name=None)

for table, df in dfs.items():
    df.to_sql('minute_candle', db)
    print(f'{df} inserted successfully')

# rows = db.execute("SELECT * FROM minute_candle limit 5").fetchall()
# print(rows)

db.close()