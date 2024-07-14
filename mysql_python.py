# this project i can use mysql and python and both are connect by using python code
from tabulate import tabulate #this is tabulate package and show data in table structure
import mysql.connector #connect mysql
con=mysql.connector.connect(host="localhost",user="root",password="#MP567890@@??",database="muthudb") #connect database
if con.is_connected():
    print("connected")
else:
    print("not connected")
    
def insert(ID,NAME,AGE,CITY,DEPT):#insert data into table
    res=con.cursor()#it is pointing
    sql="insert into users (ID,NAME,AGE,CITY,DEPT) values (%s,%s,%s,%s,%s)" # it is query sql query
    user=(ID,NAME,AGE,CITY,DEPT)
    res.execute(sql,user)
    con.commit()
    print("data insert sucess")
   
def update(ID,NAME,AGE,CITY,DEPT):#update table
    res=con.cursor()
    sql="update users set ID=%s,NAME=%s,AGE=%s,CITY=%s where DEPT=%s"
    user=(ID,NAME,AGE,CITY,DEPT)
    res.execute(sql,user)
    con.commit()
    print("data update sucess")

def select():#this function for select table data for database
    res=con.cursor()
    sql="select ID,NAME,AGE,CITY,DEPT from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY","DEPT"]))
    

def delete(ID):
    res=con.cursor()
    sql="delete from users where ID=%s"
    user=(ID,)
    res.execute(sql,user)
    con.commit()
    print("data delete sucess")
while True:#use while for ask opyion to usert for multiple times
    print("1.Insert data")
    print("2.Update data")
    print("3.select data")
    print("4.deletedata")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ID=input("Enter your id:")
        NAME=input("Enter your name:")
        AGE=input("Enter your age:")
        CITY=input("Enter your city:")
        DEPT=input("Enter your dept:")
        insert(ID,NAME,AGE,CITY,DEPT)
        
    elif choice==2:
        ID=input("Enter your id:")
        NAME=input("Enter your name:")
        AGE=input("Enter your age:")
        CITY=input("Enter your city:")
        DEPT=input("Enter your dept:")
       
        update(ID,NAME,AGE,CITY,DEPT)
        
        
    elif choice==3:
        select()
    elif choice==4:
       ID=input("Enter your  delete id:")
       delete(ID)
    elif choice==5:
        quit()
    else:
        print("invalid selection,PLEASE TRY AGAIN")
        
        
    
        
    
