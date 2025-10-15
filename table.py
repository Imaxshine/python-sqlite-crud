import db_conn as dbConn

def create_table():
            connection = dbConn.get_connection()
            # Cursor au Pointer
            cursor = connection.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS products
            (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        taken_by TEXT,
                        quantity REAL,
                        location TEXT,
                        price INTEGER
            )
            """
            cursor.execute(query)
            connection.commit()
            if connection is not None:
                        print('Meza imeundwa Kikamilifu')
            else:
                        print('Tumeshindwa kuunda meza')
                        
create_table()