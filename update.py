import db_conn as dbConn

def updateData(name:str, Taken:str, Quantity:int, location:str, price:int, Id:int):
    connection = dbConn.get_connection()
    pointer = connection.cursor()
    # UPDATE
    query = "UPDATE products SET name = ?, taken_by = ?, quantity = ?, location = ?, price = ? WHERE id = ?"
    data = (name, Taken, Quantity, location, price, Id)
    pointer.execute(query, data)
    connection.commit()
    print('Usakinishaji umekamilika kikamilifu')
    print()
    import read as SomaData
    SomaData.ReadData()
    
def userUpdate():
    
    import read
    
    try:
        Id = int(input('Ingiza kitambulisho cha bidhaa > '))
        Name = input('Jina jipya la bidhaa > ')
        Taken = input("Jina jipya la mdeni > ")
        quantity = float(input('Kiasi kipya cha bidhaa > '))
        Location = input('Eneo la mdeni > ')
        Price = float(input('Bei ya bidhaa > ')) 
        
        updateData(Name, Taken, quantity, Location, Price, Id)
        
    except ValueError as error:
        print(f"{error}")
        
        
        
    