import db_conn as dbConn
import random as rand
import string
import read as soma

def deleteAll():
    try:
        connection = dbConn.get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM products"
        cursor.execute(query)
        connection.commit()
        
        itemsDeleted = cursor.rowcount
        
        if itemsDeleted > 0:
            print(f"Kumbukumbu zote ({itemsDeleted}) zimefutwa kikamilifu.")
            soma.ReadData()
        else:
            print("Hakuna kumbukumbu iliyofutwa, au hakuna taarifa zilizopatikanaz!")
    except Exception as er:
        print(f"{er}")
    
def deleteVerification():
    s = string.ascii_letters
    getList = list(s)
    rand.shuffle(getList)
    
    codes = ""
    for num in range(4):
        word = getList[num]
        codes += word

    print()
    print(f'Authentication code: {codes}')
    
    try:
        user_code = input('Ingiza code ya authentication (uthibitisho) ili kufuta kumbukumbu zote > ').strip()
        
        if user_code == codes:
            deleteAll()
        else:
            print(f'Samahani code uliyoitumia sio sahihi au imeisha muda wake!')
    except Exception as e:
        print('Ingiza thamani halisi')
    
