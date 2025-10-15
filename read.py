import db_conn as dbConn
import debit as deni

def ReadData():
    connection = dbConn.get_connection()
    cursor = connection.cursor()
    # SELECT
    query = "SELECT * FROM products"
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) > 0:
        for Endex, result in enumerate(results, 1):
            Id, name, taken, quantity, location, price = result
            print(f'{Endex} - ID=>{Id}: Jina la bidhaa: {name}, imekopwa kwa {taken}, kiasi ni {quantity}, eneo la mteja: {location} na kiasi cha deni ni {price:,}/-')
        
        deni.getTotal()
    else:
        print("Hakuna kumbukumbu yoyote inayopatikana kwa sasa!")
