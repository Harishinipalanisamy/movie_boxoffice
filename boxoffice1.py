import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="box_office"
)
mycursor=mydb.cursor()
def insert_data():
    sql="insert into box collection(DIRECTOR) values (%s)"
    director=input("enter your director name:")
    val=[director]
    mycursor.execute(sql,val)
    mydb.commit()
insert_data()
import pandas
df=pandas.read_excel('C:\\Users\\ELCOT\\Desktop\\pthon intermidiate\\data.csv.xlsx')
data=pandas.DataFrame(df,columns=['DIRECTOR'])
print(data)



