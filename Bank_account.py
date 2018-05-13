#Assignment - Bank Account
#In this assignment you are going to test your knowledge of class composition.
#Your task is to create a class which represent a "Bank Account".
#The Bank Account will have the following properties.

#Bank Account:
    #- First Name
    #- Last Name
    #- Middle Name
    #- Account Type
    #- Balance
    #- Status (Opened/Closed/Freeze)

 #Here are the features that needs to be implement:

#- A user should be able to open a bank account provided they have the initial balance of $100
#- User should be able to transfer money from one bank account to another
#- A user should be able to withdraw money from the bank account
#- The app should charge $-35 fees if the bank account is below $0

import os
import time
import sys
from random import *

class Bank_account:
    def __init__(self, first_name, middle_name, last_name, account_num, balance,
    status):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_num = account_num
        self.balance = balance
        self.status = status

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def greetings(self):
        print ("Welcome to Bank Digital")
        time.sleep(3)
        self.menu()

    def menu(self):
        self.clear()
        print ("Please make your selection.")
        print ("[A] to sign up for an account.")
        print ("[B] to make a deposit.")
        print ("[C] to make a withdrawl.")
        print ("[D] to check for balance.")
        print ("[E] to make a bank transfer.")
        option = input("Hi what would you like to do?").lower()
        if option == "a":
            self.open_account()

        elif option == "b" or option == 'c':
            self.deposit_withdrawl(option)
        elif option == "d":
            self.account_status()
        elif option == 'e':
            self.bank_transfer()



    def task_done(self):
        choice = input("Enter [m] to go to menu [q] to quit")
        if choice == 'm':
            self.menu()
        else:
            sys.exit()

    def open_account(self):
        print("Thanks for choosing Digital Bank!")
        print("$100 is needed to open an account.")
        enough = input("Do you have enough? please enter [y] or [n]")
        if enough == 'n':
            print("You don't have enought to start an ccount.")
            self.greetings()
        else:
            first_deposit = int(input("Enter your first deposit. "))
            if first_deposit < 100:
                print ("Sorry you did not enter enough to open an account!")
                self.task_done()

        self.first_name = input ("Please enter your first name")
        self.middle_name = input("Please enter your middle_ name.")
        self.last_name = input("Please enter your last name.")
        self.account_number = random.randint(1,10)
        self.task_done()



    def deposit_withdrawl(self, option):
        amt = int(input("Please enter amount."))
        if option == 'b':
            self.balance += amt
        else:
            self.balance -= amt
        self.account_status()




    def bank_transfer(self):
        self.clear()
        receiver_name = input("Enter receiver account name.")
        receiver_account = int(input("Enter receiver account number."))
        transfer_amt = int(input("Enter amount you would like to transfer."))
        self.balance -= transfer_amt
        print(f"An amount of {transfer_amt} has been transfered to {receiver_name}")
        self.task_done()


    def account_status(self):
        self.clear()
        #self.account_num = input("Please enter your 1 digit account number.")
        print(f"Your account status is {self.status}")
        print(f"Your account balance is {self.balance}")
        if self.balance < 0:
            print("Warning you have a negative balance!!!")
            print("You will be charged $35!")
        self.task_done()

bank_account = Bank_account("Azote", "Currela", "Tirillas", 5, 200, "open")
bank_account.greetings()
bank_account.account_status()
