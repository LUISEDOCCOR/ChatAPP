import mysql.connector
import bcrypt
import localdb as ldb

db_config = {
    "host" : "localhost",
    "user": "root",
    "password" : "",
    "database" : "chatapp"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

if conn.is_connected:
    print('EN SERVICIO')    
else:
    print('FUERA DE SERVICIO')    
    

def add(User, Gmail, Password):
    salt = bcrypt.gensalt()
    hashPassword = bcrypt.hashpw(Password.encode('utf-8'), salt)
    cursor.execute('INSERT INTO users (name, gmail, password) VALUES (%s,%s,%s)', (User, Gmail, hashPassword))
    conn.commit()
    

def verifyGmail (Gmail):
    cursor.execute('SELECT * FROM users WHERE gmail = (%s)', (Gmail,))
    verify = cursor.fetchall()

    if not verify:
        return True
    else:
        return False


def login (Gmail, Password):
    cursor.execute('SELECT * FROM users WHERE gmail = (%s) LIMIT 1', (Gmail,))
    verify = cursor.fetchall()

    if not verify:
        return False
    else:
        RootPassword = verify[0][3].encode('utf-8') 
        if bcrypt.checkpw(Password.encode('utf-8'), RootPassword):
            ldb.add(verify)

            return True
        else:
            return False 
        
