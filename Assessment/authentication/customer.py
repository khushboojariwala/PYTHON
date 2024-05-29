import mysql.connector
from db_connection import *

def deposit_amount():
    try:
        n = input("Enter The Name: ")
        pw = input("Enter The Password: ")
        amount = input("Enter The Amount You Want To Deposit: ")

        # Fetch the current balance from the 'amount' table
        select_query = 'SELECT Balance FROM amount WHERE name=%s'
        cursor = mydb.cursor()
        cursor.execute(select_query, (n,))
        result = cursor.fetchone()

        if result:
            current_balance = result[0]

            # Fetch the opening balance from the 'account' table
            account_query = 'SELECT OpenningBal FROM account WHERE Password=%s'
            cursor.execute(account_query, (pw,))
            opening_balance_result = cursor.fetchone()

            if opening_balance_result:
                opening_balance = opening_balance_result[0]
                new_balance = current_balance + int(amount)

                # Update the 'amount' table with the new balance
                update_query = 'UPDATE amount SET Balance = %s WHERE Password = %s AND Name = %s'
                data = (new_balance, pw, n)
                cursor.execute(update_query, data)
                mydb.commit()

                # Fetch the updated balance for display
                cursor.execute(select_query, (n,))
                updated_balance_result = cursor.fetchone()
                updated_balance = updated_balance_result[0]

                print(f"Deposit successful. New balance: {updated_balance}")
            else:
                print("Account not found in the 'account' table.")
        else:
            print("Account not found in the 'amount' table.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

def withdraw_amount():
    n=input("Enter The Name: ")
    pw=input("Enter The Password: ")
    amount=float(input("Enter The Amount You Want To Withdraw: "))
    
    a='SELECT Balance FROM amount WHERE Password=%s'
    data=(pw,)

    try:
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        
        if result:
            current_balance = float(result[0]) 
            new_balance = current_balance - amount

            if new_balance >= 0:
                sql = 'UPDATE amount SET balance = %s WHERE Password= %s'
                d = (new_balance,pw)
                x.execute(sql, d)
                mydb.commit()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Account not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def view_balance():
    try:
        n=input("Enter The Name: ")
        pw=input("Enter The Password: ")
        select_query = 'SELECT Balance FROM amount WHERE Password=%s'
        data = (pw,)
        cursor = mydb.cursor()
        cursor.execute(select_query, data)
        result = cursor.fetchone()
        
        if result:
            print(f"Balance for Account {n} is {result[0]}")
        else:
            print("Account not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


