import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bank_db")

def register():
    try:
        n=input("Enter The Name: ")
        pw=input("Enter Your Password: ")
        ac=input("Enter Your Account Number: ")
        db=input("Enter Your Date Of Birth: ")
        add=input("Enter Your Address: ")
        cn=input("Enter Your Contact Number: ")
        ob=input("Enter Your Openning Balance: ")
    
        data1=(n,pw,ac,db,add,cn,ob)
        data2=(n,pw,ac,ob)
    
        sql1=('INSERT INTO account values (%s,%s,%s,%s,%s,%s,%s)')
        sql2=('INSERT INTO amount value (%s,%s,%s,%s)')
    
        x=mydb.cursor()
        x.execute(sql1,data1)
        x.execute(sql2,data2)
        mydb.commit()

        print("data Enter Successfully..")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def login():
    try:
        n = input("Enter The Name: ")
        pw = input("Enter The Password: ")
    
        # Fetch user details from the database to verify login
        cursor = mydb.cursor()
        select_query = 'SELECT * FROM account WHERE name = %s AND password = %s'
        cursor.execute(select_query, (n, pw))
        result = cursor.fetchone()

        if result:
            print("Login Successful!")
        else:
            print("Invalid credentials. Login failed.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

        
