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
    
    
def name():
    cursor.execute('SELECT * FROM LocalUser')
    data = cursor.fetchall()
    return data[0][1]
    