import sqlite3
import os 

rutaDataBase = os.path.join('data', 'LocalUser.db')
conn = sqlite3.connect(rutaDataBase)
cursor = conn.cursor()

cursor.execute('''
               
            CREATE TABLE IF NOT EXISTS LocalUser(
                id TEXT NOT NULL,
                name TEXT NOT NULL,
                gmail TEXT NOT NULL
            )
        ''')

conn.commit()


def add(values):
    cursor.execute('DELETE FROM LocalUser')
    conn.commit()
    
    id = values[0][0]
    name = values[0][1]
    gmail = values[0][2]
    cursor.execute('INSERT INTO LocalUser (id, name, gmail) VALUES (?, ?, ?)', (id, name, gmail))
    
    conn.commit()
    cursor.close()
    conn.close()
    
def isNotLogin():
    cursor.execute('SELECT * FROM LocalUSer')
    verify = cursor.fetchall()
    
    if not verify: #si esta vacio regresa un true
        return True
    else:
        return False
 
    
def name():
    if isNotLogin():
        return 'No User'
    else:    
        cursor.execute('SELECT * FROM LocalUser')
        name = cursor.fetchall()
        return name[0][1]    
        
def data():
    if isNotLogin():
        return True
    else:    
        cursor.execute('SELECT * FROM LocalUser')
        data = cursor.fetchall()
        return data[0][1], data[0][2]
        

        