import db_conn as dbConn

def getTotal():
    connection = dbConn.get_connection()
    cursor = connection.cursor()
    
    # SELECT SUM(price)
    
    query = """
    SELECT SUM(price) FROM products
    """
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchone()
    print("Jumla ya deni ni: ", format(results[0], ',')  + "/-",sep="")

  