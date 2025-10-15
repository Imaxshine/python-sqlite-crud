import insert as sajili
import read as soma
import update as sakinisha
import delete as futa
import debit as deni
import delete_all as futaZote

print('---------------------------------------------------------')
print('Chagua namba ya chaguo sahihi katika orodha hapo chini')
print('---------------------------------------------------------')

print()

print('''
            ==> MENYU <==
      1: Ongeza kumbukumbu
      2: Soma kumbukumbu
      3: Sakinisha kumbukumbu
      4: Tazama jumla kuu ya deni
      5: Futa kumbukumbu
      6: Futa kumbukumbu zote
      ''')

try:
    option = int(input('Ingiza namba ya chaguo > '))
    match option:
        case 1:
            print("""
                  Ingiza kumbukumbu mpya
                  """)
            sajili.getUserData()  
        case 2:
            print("""
                  Jumla ya wadeni
                  """)
            soma.ReadData()
        case 3:
            print('''
                  Unasakinisha data
                  ''')
            soma.ReadData()
            sakinisha.userUpdate()
        case 4:
            print('''
                  Jumla kuu ya deni
                  ''')
            deni.getTotal()
        case 5:
            print("""
                  Kufuta kumbukumbu
                  """)
            futa.passIdToDelete()
        case 6:
            print("""
                  Kufuta kumbukumbu zote ⚠
                  """)
            futaZote.deleteVerification()
        case _:
            print('Chaguo hilo halipo.')
            
            
except ValueError:
    print('Chaguo sio sahihi, tafadhali ingiza chaguo sahihi!')
