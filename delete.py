import db_conn as dbConn
import read as soma

def deleteData(id:int):
    connection = dbConn.get_connection()
    pointer = connection.cursor()
    query = """
    DELETE FROM products WHERE id = ?
    """
    id_to_delete = (id,)
    pointer.execute(query, id_to_delete)
    connection.commit()
    connection.close()
    
    if pointer.rowcount > 0:
        print('Data imefutwa kikamilifu \n')
        soma.ReadData()
    else:
        print("Hakuna data iliyofutwa au hakuna data ya kufuta!")
        soma.ReadData()
    
def passIdToDelete():
    soma.ReadData()
    try:
        Id = int(input('Ingiza kitambulisho cha bidhaa ya kufuta > '))
        deleteData(Id)
    except ValueError as kosa:
        print(f'{kosa}')
        
