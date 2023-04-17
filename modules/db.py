import json

import mysql.connector
from modules import utility

def init():
    global username
    global password
    global host
    username = utility.loadConfig().get("db", "username")
    password = utility.loadConfig().get("db", "password")
    host = utility.loadConfig().get("db", "host")

    mysqlExecute("CREATE TABLE IF NOT EXISTS `projectBoxes` (barcode TEXT, contense TEXT )", (), None)

def mysqlExecute(query: str, args: tuple = (), ammount: str = "all"):
    mydb = mysql.connector.connect(host=host, user=username, password=password, database=username)
    mydb.autocommit = True
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(query, args)
    if ammount == "all":
        result = mycursor.fetchall()
    elif ammount == "one":
        result = mycursor.fetchone()
    else:
        result = None
    mycursor.close()
    mydb.close()
    return result

def addNewProjectBox(barcode: str):
    mysqlExecute("INSERT INTO projectBoxes (barcode, contense) VALUES (%s, %s)", (barcode, None), None)

def getProjectBox(barcode: str):
    return mysqlExecute("SELECT * FROM projectBoxes WHERE barcode = %s", (barcode,), "one")

def addContenseToProjectBox(barcode: str, contense: dict):
    data = mysqlExecute("SELECT * FROM projectBoxes WHERE barcode = %s", (barcode,), "one")
    contenseNew = json.load(data["contense"])
    contenseNew.append(contense)
    mysqlExecute("UPDATE projectBoxes SET contense = %s WHERE barcode = %s", (contenseNew, barcode), None)

def removeContenseFromProjectBox(barcode: str, contense: dict):
    data = mysqlExecute("SELECT * FROM projectBoxes WHERE barcode = %s", (barcode,), "one")
    contenseNew = json.load(data["contense"])
    contenseNew.remove(contense)
    mysqlExecute("UPDATE projectBoxes SET contense = %s WHERE barcode = %s", (contenseNew, barcode), None)

def getContenseFromProjectBox(barcode: str):
    data = mysqlExecute("SELECT * FROM projectBoxes WHERE barcode = %s", (barcode,), "one")
    return json.load(data["contense"])