# DBMS Project

## File Structure  
- start.py: entry point  
- ui.py, SubWindow.py: GUI  
- controller.py: backend, connected to MySQL database 
- config.ini: database configuration example   
- /db_setup: used to setup the database, table and initial data  
- /ui_design: ui file of our GUI  
## Prerequisite  
- MySQL  
  - we can edit config file to our own account name and passwd   
- Python 3.8  
- pipenv(python moule)  
- mysql-connector-python(python module)  
- pyqt5(python module)  
## System Setup  
1. initial python enviroment  
```bash
#in project root directory
pipenv install --dev  
pipenv shell
```
2. create MySQL dataabase  
```
cd db_setup
python create_db.py
```
3. Data initialize  
```
python data_set.py
```
## Usage  
```bash
#in project root directory
pipenv shell
python start.py
```
## Clean Database  
- drop all the table and whole database  
```bash
pipenv shell
cd db_setup
python delete_db.py
```

# 介面截圖與使用說明
## 介面截圖
1. Button  
![](https://i.imgur.com/CyBWE0j.png)

2. SQL instruction  
![](https://i.imgur.com/5RVCc0l.png)

## 使用說明
1. Button  
- 從左邊的查詢工具旁邊的選單選擇MySQL以外的東西  
- 按下查詢  
- 使用的SQL指令會顯示在左邊第三塊區域內（亦即旁邊沒有標籤的那一塊）  
- 查詢結果會顯示在右邊的白色框內  
2. SQL instruction  
- 從左邊的查詢工具旁邊的選單選擇MySQL  
- 在查詢關鍵字輸入想要查詢的SQL語句  
- 按下查詢  
- 使用的SQL指令會顯示在左邊第三塊區域內（亦即旁邊沒有標籤的那一塊）  
- 查詢結果會顯示在右邊的白色框內，一行是一組輸出  

# 資料庫設計
## ER diagram
![](https://i.imgur.com/NKLYmgB.jpg)

- 應用情境：便利商店應用，包含員工(employee)、店舖(shop)、包裹(package)、顧客(customer)和商品(item)這五項主要的Entity  
- Entitys:  
  - Employee  
    - id_number：身份證字號，是直接拿來當Primary Key用的  
    - Name  
    - Birthday  
    - Phone  
    - Email  
  - Shop  
    - Number：紀錄店家號碼，交貨便除了可以用地址查詢店家，也可以直接輸入店家號碼  
    - Name：店名  
    - Address = City + Dist + Road + House Number：因為一般在寄送包裹時，我們篩選店家的方式也都是從縣市、市區開始一層一層往下篩，所以在這邊選擇這樣紀錄  
  - Package  
    - Number：紀錄包裹號碼用，這樣也才有獨立的東西給顧客查詢  
    - Sender = Name + Phone：寄件人  
    - Receiver = Name + Phone：收件人  
    - Status：貨物現在狀況，可能是運送中/已到店/退貨中...等  
    - Picked：看貨物是否已經被領取，這樣店員在盤點要退貨的貨物會比較方便  
  - Customer  
    - Name  
    - Phone：參考便利商店均是以手機號碼來申請會員  
  - Item  
    - Name  
    - Number：紀錄商品號碼，商品名稱基本上會不同，為了避免搞混多了可以紀錄的  
    - Price  
- Relationships:  
  - Manages：店經理  
  - Works_for：每個員工在不同的店工作，且只會在一家店工作  
  - Destination：包裹要寄到的店家，因為要算退貨日期（七天），所以會需要  arrival date  
  - Departure：因為包裹可能會被退貨，所以還是需要寫原本寄件的地方  
  - Purchase：店家進貨商品，一次不只購買一件，也不只進貨一次，所以有 count和 date這兩個 attibute  
    - 進貨理論上一天只會一次，所以紀錄日期應該足夠  
  - Buying：收據，客人去一家店購買商品會有紀錄，他可能不只來這家店一次，所以會有time這個 attibute區隔  
    - 客人有可能是會員，也有可能不是，所以想說在放資料時可以設計一個欄位，名字是 default，電話是"NULL"這個字串，專門用來標示這些客人消費紀錄  
    -  Total可以從商品的數量來算，但店員只需要計算當日營業額的話，使用 Total這個欄位會比較方便  
    -  有多樣商品，但店家和顧客都相同，為了方便紀錄，分成了收據總額和小計  
    -  因為顧客會每天來很多次，所以時間部份需要紀錄到分跟秒   
## Relation Schema
### Entity
#### shop
- Attribute conversion   
  - Number $\to$ s_id  
  - Name $\to$ s_name  
  - House Number $\to$ number  
  - city + dist + road + number = address  
- Primary Key: s_id (auto increment)   
- Relationship conversion   
  - Manages $\to$ mgn_id
    -  因為是 partial relationship對上 total relationship，所以會在 total的那一方(shop)下面記 employee的 primary key(id_number)，在這裡用 mgn_id表示  
- Table  

|s_id|s_name|city|dist|road|number|mgn_id|
|-|-|-|-|-|-|-|

#### employee  
- Primary Key: id_number(身份證字號不會重複)  
- Relationshop conversion  
  - Works for $\to$ shop  
    - 因為是1:N的 relationship，所以在1的那一方(employee)的下面記下shop的primary key(s_id)，在這裡用shop表示  
- Table   

|id_number|Name|Birthday|phone|email|shop|
|-|-|-|-|-|-|

#### package  
- Attribute conversion   
  - Number $\to$ p_id  
  - Sender-Name $\to$ sender  
  - Sender-Phone $\to$ s_phone  
  - Receiver-Name $\to$ receiver  
  - Receiver-Phone $\to$ r_phone  
  - sender + s_phone = Sender  
  - receiver +r_phone = Receiver  
- Primary Key:p_id (auto increment)  
- Relationship conversion  
    - Departure $\to$ dep  
      - 因為是 partial relationship對上 total relationship且為1:N，所以會在 total的那一方(package)下面記 shop的 primary key(s_id)，在這裡用 dep表示  
    - Destination$\to$dest  
      - 同上，並且有arrival_date attribute  
- Table  

|p_id|sender|s_phone|dep|receiver|r_phone|dest|arrival_date|status|picked|
|-|-|-|-|-|-|-|-|-|-|

#### items  
- Attribute conversion   
  - Number $\to$ i_id  
  - Name $\to$ i_name   
- Primary Key:i_id (auto increment)  
- Table  

|i_id|i_name|Price|
|-|-|-|
  
#### customers
- Attribute conversion   
  - Name $\to$ c_name  
  - Phone $\to$ c_phone  
- Primary Key: c_phone  
- Table  

|c_phone|c_name|
|-|-|

### Relationship Conversion  
#### Buying  
- 是三元的relationship，且因為是1:1:N的 relationship，所以會使用兩組 table紀錄  
- customers and shops  
  - 一筆資料內是一個 item對應一個 shop，選了兩者的Primary Key作為relationship conversion
  - 還會加上 relationship中的 attribute： Time, Total   
    - Time $\to$ r_date  
    - Total $\to$ total  
  - 原先 Key是 shop+loc+r_date，後來使用能自動增加的r_id作為Primary Key   
- Primary key: r_id (auto increment)  
- Table: receipts  

|r_id|r_date|total|loc|c_phone
|-|-|-|-|-|

- items  
  - 使用上面的 Primary Key (r_id)來作為item和shop的relationship conversion  
  - 會加上每個商品有幾樣來做小計  
- Primary key:d_id (auto increment)  
- Table: receipt_detail  

|d_id|receipt|item|count|
|-|-|-|-|

#### Purchase
- 是M:N的 relationship，另外使用了 Purchase table來紀錄一筆資料內是一個 item對應一個 shop，使用兩者的Primary Key來作為relationship conversion  
  - 雖然 key是 shop+loc+item，但設計後使用能自動增加的p_id作為Primary Key  
- Primary key: p_id (auto increment)  
- Table: purchases  

|p_id|p_date|loc|item|count|
|-|-|-|-|-|
