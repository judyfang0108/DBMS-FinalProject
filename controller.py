from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *
from function import * 

#connect database first
db = connect_db("config.ini")

#gui instruction dictionary
instruction = {
        'select':"SELECT p_id, receiver \nFROM packages \nWHERE \nreceiver like '珊%' and \ndest=10 and \nr_phone like '%660'",
        'delete1':"DELETE FROM receipts WHERE r_id=9",
        'delete2':"DELETE FROM receipt_details WHERE receipt=9",
        'update':"UPDATE packages \nset status='已送達', arrival_date=current_date() \nWHERE p_id=10",
        'in':"select name, email \nFROM employees, shops \nWHERE shop=s_id and\n city IN ('新北市', '台北市')",
        'not_in':"SELECT i_id, i_name FROM items \nWHERE i_id NOT IN (SELECT item \nFROM purchases \nWHERE \nloc=6 and p_date between \nDATE_SUB('2022-04-26', INTERVAL 5 DAY) and '2022-04-26')",
        'exists':"SELECT name, email \nFROM employees \nWHERE \nEXISTS (SELECT * FROM shops \nWHERE mgn_id=id_number)",
        'not_exists':"SELECT \nname, id_number, phone, birthday \nFROM employees \nWHERE \nNOT EXISTS (SELECT * FROM shops \nWHERE city='澎湖縣' and shop=s_id)",
        'count':"SELECT shop, COUNT(*) \nFROM employees \nGROUP BY shop",
        'sum':"SELECT SUM(total) \nFROM receipts \nWHERE \nloc=6 and \nr_date between '2022-04-25' and '2022-04-26'",
        'max':"SELECT name, phone, birthday \nFROM employees, shops \nWHERE \nmgn_id=id_number and \nbirthday=(SELECT MAX(birthday) \nFROM employees, shops \nWHERE mgn_id=id_number)",
        'min':"SELECT i_id, i_name, price \nFROM items \nWHERE \nprice=(SELECT MIN(price) FROM items)",
        'avg':"SELECT AVG(total) \nFROM receipts",
        'having':"SELECT shop, s_name, COUNT(*) \nFROM employees, shops \nWHERE \ns_id=shop \nGROUP BY \nshop, s_name HAVING COUNT(*)<2"
}

from ui import *
from SubWindow import *
class Form_controller(QtWidgets.QWidget):
        def __init__(self):
                super().__init__()
                self.ui = Ui_Form()
                self.combo_text = "SELECT-FROM-WHERE"
                self.instruct = None
                self.ui.setupUi(self)
                self.setup_control()
                self.sub_window = SubWindow_controller()
        
        def setup_control(self):
                #connect combo_text with combo box
                self.ui.comboBox.currentTextChanged.connect(self.text_change)
                self.ui.pushButton.clicked.connect(self.on_clicked)

        def text_change(self, text):
                self.combo_text = text

        def on_clicked(self):
                #action after click button
                if self.combo_text == "SELECT-FROM-WHERE":
                        result = f_search(db, instruction["select"])
                        self.ui.textBrowser.setText(instruction["select"])
                        buf = "%s%s"%("id".ljust(10),"姓名")+"\n"
                        for p_id, name in result:
                                buf = buf+"%s%s"%(str(p_id).ljust(10),name)+"\n"
                elif self.combo_text == "DELETE":
                        try:
                                f_change(db, instruction["delete1"])
                                f_change(db, instruction["delete2"])
                                buf=""
                        except:
                                buf="Already Done"
                        self.ui.textBrowser.setText("1."+instruction["delete1"]+"\n2."+instruction["delete2"])
                        buf=""
                elif self.combo_text == "INSERT":
                        try:
                                sql = f_insert(db)
                                buf=""
                        except:
                                buf="Already Done"
                        self.ui.textBrowser.setText(sql)
                elif self.combo_text == "UPDATE":
                        try:
                                f_change(db, instruction["update"])
                                buf=""
                        except:
                                buf="Already Done"
                        self.ui.textBrowser.setText(instruction["update"])
                elif self.combo_text == "IN":
                        result = f_search(db, instruction["in"])
                        self.ui.textBrowser.setText(instruction["in"])
                        buf = "%s%s"%("名字".ljust(10,chr(12288)),"信箱")+"\n"
                        for name, email in result:
                                buf = buf+"%s%s"%(name.ljust(10,chr(12288)), email)+"\n"
                elif self.combo_text == "NOT IN":
                        result = f_search(db, instruction["not_in"])
                        self.ui.textBrowser.setText(instruction["not_in"])
                        buf = "{0}\t{1}\n".format("商品號碼", "商品名稱", chr(12288))
                        for i_id, name in result:
                               buf = buf+"{0:{2}<4}\t{1}\n".format(i_id, name, chr(12288))
                elif self.combo_text == "EXISTS":
                        result = f_search(db, instruction["exists"])
                        self.ui.textBrowser.setText(instruction["exists"])
                        buf = "%s%s"%("店經理名字".ljust(10,chr(12288)),"信箱")+"\n"
                        for name, email in result:
                                buf = buf+"%s%s"%(name.ljust(10,chr(12288)), email)+"\n"
                elif self.combo_text == "NOT EXISTS":
                        result = f_search(db, instruction["not_exists"])
                        self.ui.textBrowser.setText(instruction["not_exists"])
                        buf = "{0:{4}<10}{1:<12}\t{2:{4}<10}\t{3}\n".format("名字", "身份證字號", "手機", "生日", chr(12288))
                        for name, id, phone, b_day in result:
                               buf = buf+"{0:{4}<10}{1:<12}\t{2:<10}\t{3}\n".format(name, id, phone, b_day, chr(12288))
                elif self.combo_text == "COUNT":
                        result = f_search(db, instruction["count"])
                        self.ui.textBrowser.setText(instruction["count"])
                        self.ui.textBrowser.setText(instruction["not_exists"])
                        buf = "{0}\t{1}\n".format("店號", "店員人數", chr(12288))
                        for shop, people in result:
                               buf = buf+"{0}\t{1}\n".format(shop, people)
                elif self.combo_text == "SUM":
                        result = f_search(db, instruction["sum"])
                        self.ui.textBrowser.setText(instruction["sum"])
                        buf = "營業額="+str(result[0][0])
                elif self.combo_text == "MAX":
                        result = f_search(db, instruction["max"])
                        self.ui.textBrowser.setText(instruction["max"])
                        buf = "{0:{3}<10}{1:{3}<6}\t{2}\n".format("名字", "手機", "生日", chr(12288))
                        for name, phone, b_day in result:
                               buf = buf+"{0:{3}<10}{1:<12}\t{2}\n".format(name, phone, b_day, chr(12288))
                elif self.combo_text == "MIN":
                        result = f_search(db, instruction["min"])
                        self.ui.textBrowser.setText(instruction["min"])
                        buf = "{0}\t{1:{3}<20}\t{2}\n".format("商品號碼", "商品名稱", "售價", chr(12288))
                        for i_id, name, price in result:
                               buf = buf+"{0:{3}<4}\t{1:{3}<20}\t{2}\n".format(i_id, name, price, chr(12288))
                elif self.combo_text == "AVG":
                        result = f_search(db, instruction["avg"])
                        self.ui.textBrowser.setText(instruction["avg"])
                        buf = "平均花費="+str(result[0][0])
                elif self.combo_text == "HAVING":
                        result = f_search(db, instruction["having"])
                        self.ui.textBrowser.setText(instruction["having"])
                        buf = "{0}\t{1:{3}<6}\t{2}\n".format("店號", "店名", "人數", chr(12288))
                        for s_id, name, people in result:
                               buf = buf+"{0}\t{1:{3}<6}\t{2}\n".format(s_id, name, people, chr(12288))
                elif self.combo_text == "MySQL":
                        #take the instruction from PlainText
                        self.instruct = self.ui.textEdit.toPlainText()
                        buf = f_mysql(db, self.instruct)
                        self.ui.textBrowser.setText(self.instruct)
                #show or change sub window
                self.sub_window.setup_text(buf)
                self.sub_window.show()
                return

class SubWindow_controller(QtWidgets.QWidget):
        def __init__(self):
                super().__init__()
                self.sub_ui = Ui_SubWindow()
                self.sub_ui.setupUi(self)
        
        def setup_text(self, text):
                self.sub_ui.textBrowser.setText(text)