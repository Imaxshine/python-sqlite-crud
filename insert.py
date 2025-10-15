import db_conn as dbConn

def InsertData(name:str, takenBy:str, quantity:int, location:str, price:int):
    connection = dbConn.get_connection()
    pointer = connection.cursor()
    query = """
    INSERT INTO products (name, taken_by, quantity, location, price) VALUES (?, ?, ?, ?, ?)
    """
    data = (name, takenBy, quantity, location, price)
    pointer.execute(query, data)
    connection.commit()
    connection.close()
    print('Taarifa zimeifadhiwa kikamilifu')
    
    
def getUserData():
    try:
         Name = input('Ingiza jina la bidhaa > ')
         TakenBy = input('Jina la mdeni > ')
         Quantity = int(input('Kiasi cha bidhaa > '))
         Location = input('Eneo la mdeni > ')
         Price = float(input('Bei ya bidhaa > ')) 

         
         InsertData(Name, TakenBy, Quantity, Location, Price)
         
    except ValueError as error:
        print(f'Kosa: {error}')


    
    