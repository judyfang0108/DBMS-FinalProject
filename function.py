import mysql.connector
import configparser

#connect database
def connect_db(file):
        config = configparser.ConfigParser()
        config.read(file)
        host = config["database"]["host"]
        user = config["database"]["user"]
        password = config["database"]["password"]
        database = config["database"]["database"]

        db = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
        )
        return db

#mysql search function
def f_search(db, select):
        cursor = db.cursor()
        cursor.execute(select)
        res = cursor.fetchall()
        cursor.close()
        return res

#my sql data change function
def f_change(db, change):
        cursor = db.cursor()
        cursor.execute(change)
        db.commit()
        cursor.close()
        return

# if we use mysql in gui, we will use this function
def f_mysql(db, sql):
        if sql.startswith('s') or sql.startswith('S') :
                #if the beginning of instruction is 'select'
                try:
                        res = f_search(db, sql)
                        return '\n'.join(str(p) for p in res)
                # if we have wrong instruction
                except:
                        return "Wrong instruction"
        else:
                try:
                        f_change(db, sql)
                        return ""
                # if we have wrong instruction
                except:
                        return "Wrong instruction"

#use when we choose insert in gui, we will insert the first data and change the receipt's value in the second data
def f_insert(db):
        cursor = db.cursor()
        cursor.execute("insert into receipts (r_date, total, loc) values ('2022-04-26 14:28', 87, 4)")
        db.commit()
        cursor.execute("SELECT @@IDENTITY as r_id")
        r_id = cursor.fetchall()
        sql = "insert into \nreceipt_details (receipt, item, count) \nvalues (%d, 3, 3)"%(r_id[0][0])
        cursor.execute(sql)
        db.commit()
        cursor.close()
        #return the string that we wil show in the sub window
        return "1.insert into \nreceipts (r_date, total, loc) \nvalues ('2022-04-26 14:28', 87, 4)\n"+"2."+sql