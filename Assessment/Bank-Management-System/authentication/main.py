import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root",password="root",database="BANK_MANAGEMENT")

def OpenAcc():
    try:
        n=input("Enter The Name: ")
        ac=input("Enter Your Account Number: ")
        db=input("Enter Your Date Of Birth: ")
        add=input("Enter Your Address: ")
        cn=input("Enter Your Contact Number: ")
        ob=input("Enter Your Openning Balance: ")
    
        data1=(n,ac,db,add,cn,ob)
        data2=(n,ac,ob)
    
        sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
        sql2=('insert into amount value (%s,%s,%s)')
    
        x=mydb.cursor()
        x.execute(sql1,data1)
        x.execute(sql2,data2)
        mydb.commit()
    
        print("data Enter Successfully..")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() or 'mydb' in globals():
            mydb.close()

def deposit_amount():
    try:
        amount = input("Enter The Amount You Want To Deposit: ")
        ac = input("Enter Your Account Number: ")

        select_query = 'SELECT Balance FROM amount WHERE AccNo=%s'
        data = (ac,)
        cursor = mydb.cursor()
        cursor.execute(select_query, data)
        result = cursor.fetchone()

        if result:
            current_balance = result[0]
            account_query = 'SELECT OpenningBal FROM account WHERE AccNo=%s'
            cursor.execute(account_query, data)
            opening_balance_result = cursor.fetchone()

            if opening_balance_result:
                opening_balance = opening_balance_result[0]
                new_balance = current_balance + int(amount)
                # Update the 'amount' table with the new balance
                update_query = 'UPDATE amount SET Balance=%s WHERE AccNo=%s'
                data = (new_balance, ac)
                cursor.execute(update_query, data)
                mydb.commit()
                print("Deposit successful.")
            else:
                print("Account not found in the 'account' table.")
        else:
            print("Account not found in the 'amount' table.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() or 'mydb' in globals():
            mydb.close()

    
def withdraw_amount():
    amount=float(input("Enter The Amount You Want To Withdraw: "))
    ac=input("Enter Your Account Number: ")
        
    a='SELECT Balance FROM amount WHERE AccNo=%s'
    data=(ac,)

    try:
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        
        if result:
            current_balance = float(result[0]) 
            new_balance = current_balance - amount

            if new_balance >= 0:
                sql = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
                d = (new_balance, ac)
                x.execute(sql, d)
                mydb.commit()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Account not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in globals():
            mydb.close()

def balance_enquiry():
    try:
        ac = input("Enter The Account Number: ")
        select_query = 'SELECT Balance FROM amount WHERE AccNo=%s'
        data = (ac,)
        cursor = mydb.cursor()
        cursor.execute(select_query, data)
        result = cursor.fetchone()
        
        if result:
            print(f"Balance for Account {ac} is {result[0]}")
        else:
            print("Account not found.")
        main()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() or 'mydb' in globals():
            mydb.close()

def display_details():
    try:
        ac = input("Enter The Account Number: ")

        # Fetching account name
        name_query = 'SELECT name FROM account WHERE AccNo=%s'
        data = (ac,)
        cursor = mydb.cursor()
        cursor.execute(name_query, data)
        name_result = cursor.fetchone()

        if name_result:
            account_name = name_result[0]

            balance_query = 'SELECT Balance FROM amount WHERE AccNo=%s'
            cursor.execute(balance_query, data)
            balance_result = cursor.fetchone()

            if balance_result:
                account_balance = balance_result[0]
                print(f"Name: {account_name}, Balance: {account_balance}")
            else:
                print("Account balance not found.")
        else:
            print("Account name not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() or 'mydb' in globals():
            mydb.close()



def CloseAcc():
    try:
        ac=input("Enter The Account Number: ")
        sql1='delete from account where AccNo=%s'
        sql2='delete from amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        x.execute(sql1,data)
        x.execute(sql2,data)
        mydb.commit()
        print("Account Close Successfully..")
        main()
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'mydb' in locals() or 'mydb' in globals():
            mydb.close()

def main():
    print('''
            1.OPEN NEW ACCOUNT
            2.DEPOSITE AMOUNT
            3.WITHDRAWAL AMOUNT
            4.BALANCE ENQUIRY
            5.DISPLAY CUSTOMER DETAILS
            6.CLOSE AN ACCOUNTs''')
    
    choice=input("Enter The Task You Perform: ")

    if (choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        deposit_amount()
    elif(choice=='3'):
        withdraw_amount()
    elif(choice=='4'):
        balance_enquiry()
    elif(choice=='5'):
        display_details()
    elif(choice=='6'):
        CloseAcc()
    else:
        print("INVALID CHOICE")


main()







