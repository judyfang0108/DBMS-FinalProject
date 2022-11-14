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
        password = password,
        database = database
)
print("[server] Database connect")
cursor = db.cursor()

#insert employees
sql = "insert into employees (id_number, name, birthday, phone, email, shop) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
        ('A239179811', '哈姆太郎', '2000-08-06', '0928811253', 'hamtaro@gmail.com', 1),
        ('B166762821', '蟹老闆', '1964-11-30', '0933645099', 'mr.krabs@gmail.com' ,8),
        ('R107114771', '大老闆', '1990-09-21', '0954902587', 'taisho@gmial.com', 5),
        ('R264614372', '鈴鈴', '1998-03-03', '0926901160', 'ramurin@gmail.com', 5),
        ('Q275788328', '琪琪', '1998-10-10', '0919602924', 'mimirin@gmail.com', 9),
        ('Q127997935', '桃樂比', '1998-05-05', '0960405496', 'torippii@gmail.com', 9),
        ('X181843566', '巧虎', '1998-05-05', '0961239324', 'shimajiro@gmail.com', 10),
        ('T161653742', '皮老闆', '1964-07-04', '0952083820', 'plankton@gmail.com', 2),
        ('F149887609', '花仁', '1981-01-11', '0926423909', 'jin@gmail.com', 3),
        ('L193524540', '章魚哥', '1997-10-09', '0915962762', 'squidward@gmail.com', 4),
        ('W289630323', '泡芙阿姨', '1978-04-30', '0912189457', 'mrs.puff@gmail.com', 6),
        ('F250330597', '花橘子', '2002-02-04', '0958951290', 'mikan@gmail.com', 7),
        ('W197564130', '花柚子', '2003-07-06', '0987775484', 'yuzuhiko@gmail.com', 6),
        ('S298340177', '葉美玉', '1983-02-16', '0920441525', 'tamako@gmail.com', 10),
        ('P272352281', '陳靜香', '1994-05-02', '0919996358', 'shizuka@gmail.com', 9),
        ('U166916914', '武技安', '1993-06-15', '0986914877', 'takeshi@gmail.com', 7),
        ('H209218606', '美冴', '1987-10-10', '0938976644', 'misae@gmail.com', 1)
]
cursor.executemany(sql, val)

#insert customers
sql = "insert into customers (c_phone, c_name) VALUES (%s, %s)"
val = [
        ('NULL', 'default'),
        ('0933188982', '龔德綺'),
        ('0958315225', '蔡雅雯'),
        ('0929924659', '李美玲'),
        ('0939074975', '袁則琳'),
        ('0930021609', '邱彥君'),
        ('0926971315', '伊哲瑋'),
        ('0953097836', '陳子揚'),
        ('0917064648', '姜民學'),
        ('0927814787', '晏之苓')
]
cursor.executemany(sql, val)

#insert shops
sql = "insert into shops (s_name, city, dist, road, number, mgn_id) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
        ('石門', '新北市', '石門區', '中山路', '78號', 'H209218606'),
        ('船帆石', '屏東縣', '恆春鎮', '船帆路', '720號1樓', 'T161653742'),
        ('大台', '台北市', '大安區', '羅斯福路三段', '333巷18號1樓20號1樓', 'F149887609'),
        ('花樂', '台中市', '石岡區', '豐勢路', '1111號1樓', 'L193524540'),
        ('城中', '台南市', '安南區', '安中路六段', '599號601號', 'R107114771'),
        ('金門醫院', '金門縣', '金湖鎮', '復興路', '2-1號1樓', 'W289630323'),
        ('福隆站', '新北市', '貢寮區', '福隆街', '8號1樓', 'U166916914'),
        ('宏泰', '台北市', '信義區', '松仁路', '91-1號1樓', 'B166762821'),
        ('阿里山', '嘉義縣', '阿里山鄉', '中山村南阿里山', '55號', 'P272352281'),
        ('講美', '澎湖縣', '白沙鄉', '講美村', '78號1樓', 'S298340177')
]
cursor.executemany(sql, val)

#insert packages
sql = "insert into packages (sender, s_phone, dep, receiver, r_phone, dest, arrival_date, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
        ('綿羊', '0901234567', 3, '雨露', '0914082406', 2, '2022-04-29', '已送達'), 
        ('綿羊', '0901234567', 3, '艾蒙', '0926475837', 4, '2022-04-30', '已送達'),
        ('綿羊', '0901234567', 3, '餅乾怪獸', '0912317662', 1, '2022-04-29', '已送達'),
        ('綿羊', '0901234567', 3, '珊迪', '0933401660', 10, '2022-05-01', '已送達'),
        ('嚕嚕米', '0910987654', 4, '珊迪', '0933401660', 10, '2022-05-02', '已送達'),
        ('派大星', '0928876543', 6, '珊迪', '0955551598', 5, '2022-05-03', '已送達'),
        ('郵差貓', '0923490123', 8, '珊迪', '0955551598', 5, '2022-05-02', '已送達'),
        ('荷馬', '0929007009', 5, '霸子', '0963672909', 8, '2022-05-23', '已送達'),
        ('美枝', '0912100239', 7, '霸子', '0963672909', 8, '2022-05-24', '已送達'),
        ('蘇呆子', '0989224029', 9, '博士', '0931129304', 6, None, '寄送中')
]
cursor.executemany(sql, val)

#insert items
sql = "insert into items (i_name, price) VALUES (%s, %s)"
val = [
        ('晶華酒店-松露烤雞義大利麵', 99),
        ('日式蕎麥風味麵', 52),
        ('波特多洋芋片-蚵仔煎口味', 29),
        ('光泉無加糖濃豆漿375ml', 25),
        ('光泉無加糖濃豆漿936ml', 48),
        ('卡迪那德州薯條茄汁', 39),
        ('樂事Lays九州岩燒海苔-97g', 36),
        ('優菓甜坊黑糖豆花', 35),
        ('冠軍炒飯-青麻辣味雞炒飯', 89),
        ('煉乳牛奶麵包', 35)
]
cursor.executemany(sql, val)

#insert purchase
sql = "insert into purchases (p_date, loc, item, count) VALUES (%s, %s, %s, %s)"
val = [
        ('2022-04-20', 1, 5, 10),
        ('2022-04-20', 2, 6, 20),
        ('2022-04-20', 2, 7, 20),
        ('2022-04-25', 3, 1, 5), 
        ('2022-04-20', 3, 8, 15),
        ('2022-04-20', 4, 3, 20),
        ('2022-04-26', 5, 10, 5),
        ('2022-04-25', 6, 1, 5),
        ('2022-04-25', 6, 2, 5),
        ('2022-04-25', 6, 3, 20),
        ('2022-04-20', 6, 4, 10),
        ('2022-04-25', 6, 9, 5),
        ('2022-04-25', 6, 10, 5),
        ('2022-04-20', 8, 7, 20)
]
cursor.executemany(sql, val)

#insert receipts
sql = "insert into receipts (r_date, total, loc, c_phone) VALUES (%s, %s, %s, %s)"
val = [
        ('2022-04-22 19:30', 75, 2, 'NULL'),
        ('2022-04-22 20:24', 48, 1, '0933188982'),
        ('2022-04-25 12:02', 99, 6, 'NULL'),
        ('2022-04-25 12:03', 52, 6, 'NULL'),
        ('2022-04-25 12:09', 89, 6, 'NULL'),
        ('2022-04-25 12:12', 60, 6, 'NULL'),
        ('2022-04-25 12:12', 134, 3, '0933188982'),
        ('2022-04-25 20:20', 72, 8, 'NULL'),
        ('2022-04-26 14:26', 58, 4, 'NULL'),
        ('2022-04-26 14:28', 105, 5, 'NULL')
]
cursor.executemany(sql, val)

#insert receipt_details
sql = "insert into receipt_details (receipt, item, count) VALUES (%s, %s, %s)"
val = [
        (1, 6, 1), 
        (1, 7, 1),
        (2, 5, 1),
        (3, 1, 1),
        (4, 2, 1),
        (5, 9, 1),
        (6, 4, 1),
        (6, 10, 1),
        (7, 1, 1),
        (7, 8, 1),
        (8, 7, 2),
        (9, 3, 2),
        (10, 10, 3)
]
cursor.executemany(sql, val)
db.commit()

print("[server] Data set up success!")
cursor.close()
db.close()