print("********welcome to devi cinima`s")
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movie_ticket_book"
)
mycursor=mydb.cursor()
def insert_data():
    sql="insert into ticketbook(s_no,moviename,howmany_ticket,gst,total)values(%s,%s,%s,%s,%s)"
    s_no=int(input("enter your s.no:"))
    moviename=input("enter your movie name:")
    howmany_ticket=int(input("how ticket you want:"))
    gst=float(input("enter your gst:"))
    total=int(input("enter your taotal bill:"))
    
    val=(s_no,moviename,howmany_ticket,gst,total)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data successfully stored")
insert_data()

import datetime
f=open("movie.txt","w")
# print(f.read())
x=datetime.datetime.now()
f.write(f"{x}\n")
def movie():
    day_spcial=["rajarani","mugavari"]
    rajarani=150
    mugavari=150
    movie=input("enter your movie name:")
    how_many=int(input(f"how many ticket you want {movie}:"))
    if movie=="rajarani":
        total=rajarani*how_many
    if movie=="mugavari":
        total=mugavari*how_many
        gst=float(input("enter your GST%:"))
        gstamt=total*gst/100
        f=open("movie.txt","w")
        f.write(f"yeahh its avaliable movie today {movie}\n")
        f.write(f"ticket book succesfully\n")
        f.write(f"your total bill with GST {gstamt+total}")
        print("bill success")
movie()
def email_sending():
    try:
        receiver_mail=["bhavatharani81@gmail.com","harishinipalanisamy@gmail.com"]
        for i in receiver_mail:
            otp_number=random.randint(0000,9999)
            print(i,otp_number)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("harishiniharishini850@gmail.com","fcuq mvar ornc qmgj")
            message=f"your otp number is {otp_number}\n"
            message=("thanks forbooking devi cinima's")
            s.sendmail("harishiniharishini850@gmail.com",i,message)
            s.quit()
            print("mail send succesfully")
    except:   
        print("mail not send")
email_sending()
