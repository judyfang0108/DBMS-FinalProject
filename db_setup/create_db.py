import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read("../config.ini")
host = config["database"]["host"]
user = config["database"]["user"]
password = config["database"]["password"]
database = config["database"]["database"]

#create database
db = mysql.connector.connect(
        host = host,
        user = user,
        password = password
)

cursor = db.cursor()
cursor.execute("create database "+database)
cursor.execute("ALTER DATABASE "+database+" CHARACTER SET utf8 COLLATE utf8_general_ci;")

#create table
db = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
)

cursor = db.cursor()
cursor.execute("create table shops (s_id int NOT NULL AUTO_INCREMENT, s_name varchar(30) NOT NULL, city varchar(20) NOT NULL, dist varchar(20) NOT NULL, road varchar(20) NOT NULL, number varchar(20) NOT NULL, mgn_id varchar(15) NOT NULL, PRIMARY KEY(s_id))")
cursor.execute("create table customers (c_phone varchar(50) NOT NULL , c_name varchar(50) NOT NULL, PRIMARY KEY(c_phone))")
cursor.execute("create table packages (p_id int NOT NULL AUTO_INCREMENT, sender varchar(50) NOT NULL, s_phone varchar(20) NOT NULL, dep int NOT NULL, receiver varchar(50) NOT NULL, r_phone varchar(20) NOT NULL, dest int NOT NULL, arrival_date date, status varchar(10) NOT NULL, picked boolean DEFAULT 0, PRIMARY KEY(p_id))")
cursor.execute("create table items (i_id int NOT NULL AUTO_INCREMENT, i_name varchar(50) NOT NULL, price int NOT NULL, PRIMARY KEY(i_id))")
cursor.execute("create table receipts (r_id int NOT NULL AUTO_INCREMENT, r_date datetime DEFAULT CURRENT_TIMESTAMP, total int NOT NULL, loc int NOT NULL, c_phone varchar(20) NOT NULL default 'NULL', PRIMARY KEY(r_id))")
cursor.execute("create table receipt_details (d_id int NOT NULL AUTO_INCREMENT, receipt int NOT NULL, item int NOT NULL, count int DEFAULT 1, PRIMARY KEY(d_id))")
cursor.execute("create table employees (id_number varchar(15) NOT NULL, name varchar(50) NOT NULL, birthday date NOT NULL, phone varchar(20) NOT NULL, email varchar(50) NOT NULL, shop int NOT NULL, PRIMARY KEY(id_number))")
cursor.execute("create table purchases (p_id int NOT NULL AUTO_INCREMENT, p_date datetime DEFAULT CURRENT_TIMESTAMP, loc int NOT NULL, item int NOT NULL, count int DEFAULT 1, PRIMARY KEY(p_id))")

print("[server] Database 'DBMS_Project' and its table create")
cursor.close()
db.close()