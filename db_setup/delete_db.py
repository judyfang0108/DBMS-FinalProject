import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read("../config.ini")
host = config["database"]["host"]
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

#drop database
db = mysql.connector.connect(
        host = host,
        user = user,
        password = password
)

cursor = db.cursor()
cursor.execute("drop database "+database)

print("[server] Database 'DBMS_Project' and its table delete")
cursor.close()
db.close()