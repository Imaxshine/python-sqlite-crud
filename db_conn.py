# id
# name
# taken_by
# quantity
# location
# price
import sqlite3

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect('business.db')
        # print('Database imeundwa')
        return conn
    
    except Exception as e:
        print(f'Error: {e}')
        
