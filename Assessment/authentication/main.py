import mysql.connector
from db_connection import *
from customer import *
from banker import *


while True:
    print("\nA.banker\nB.customer\n")
    choice = input("Enter your choice:")

    if choice.lower() == "a":
        print('''
                1.OPEN NEW ACCOUNT
                2.LOGIN ACCOUNT
                3.UPDATE CUSTOMER
                4.VIEW CUSTOMER
                5.DELETE CUSTOMER''')
        
        choice=input("Enter The Task You Perform: ")
    
        if (choice=='1'):
            register()
        elif(choice=='2'):
            login()
        elif(choice=='3'):
            update_all_customers()
        elif(choice=='4'):
            view_all_customers()
        elif(choice=='5'):
            delete_all_customers()
        else:
            print("INVALID CHOICE")
    
    if choice.lower() == "b":
        print('''
                1.OPEN NEW ACCOUNT
                2.LOGIN ACCOUNT
                3.DEPOSITE AMOUNT
                4.WITHDRAW AMOUNT
                5.VIEW BALANCE''')
        
        choice=input("Enter The Task You Perform: ")
    
        if (choice=='1'):
            register()
        elif(choice=='2'):
            login()
        elif(choice=='3'):
            deposit_amount()
        elif(choice=='4'):
            withdraw_amount()
        elif(choice=='5'):
            view_balance()
        else:
            print("INVALID CHOICE")
    
    
main()
    