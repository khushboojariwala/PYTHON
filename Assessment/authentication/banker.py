import mysql.connector
from db_connection import *

def update_all_customers():
    try:
        n=input("Enter The Name: ")
        pw=input("Enter Your Password: ")
        db=input("Enter Your Date Of Birth: ")
        add=input("Enter Your Address: ")
        cn=input("Enter Your Contact Number: ")
        ob=input("Enter Your Openning Balance: ")
        ac=input("Enter Your Account Number: ")
    
        update_query = 'UPDATE account SET name=%s, password=%s, DOB=%s, address=%s, contactno=%s, openningbal=%s WHERE accno=%s'
        data = (n,pw,db,add,cn,ob,ac)
        cursor = mydb.cursor()
        cursor.execute(update_query, data)
        mydb.commit()
        print("Customers updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    

def view_all_customers():
    try:
        if mydb.is_connected():
           select_query = 'SELECT * FROM account'
           cursor = mydb.cursor()
           cursor.execute(select_query)
           result = cursor.fetchall()
           for row in result:
               print(row)           
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    


def delete_all_customers():
    try:
        delete_query1 = 'DELETE FROM account'
        delete_query2 = 'DELETE FROM amount'
        cursor = mydb.cursor()
        cursor.execute(delete_query1)
        cursor.execute(delete_query2)
        mydb.commit()
        print("All customers deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    # finally:
    #     if 'mydb' in locals() or 'mydb' in globals():
    #         mydb.close()