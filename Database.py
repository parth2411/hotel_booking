import sqlite3

def createTable():
    connection = sqlite3.connect("login.db")

    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('akash','akash@gmail.com','akash123'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    for  data in result:
        print("Username:",data[0])
        print("Email:",data[1])
        print("password :",data[2])

    connection.close()

createTable()
    
