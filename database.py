import mysql.connector
import bcrypt

db_config = {
    "host" : "localhost",
    "user": "root",
    "password" : "",
    "database" : "chatapp"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

if conn.is_connected:
    print('TRUE')    
else:
    print('FALSE')    
    

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

