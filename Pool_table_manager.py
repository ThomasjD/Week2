from Pool_tables import Tables
#from Pool_table_log import Log
import datetime
import time
import os
import pickle
import sys
import calendar

import time
import random

'''
class Needy_bitches:
    needy_little_bitches = []
    useless_bitch = (x,y)

    bitch_asking_for_help = input(x)

    for x in needy_little_bitches > 5:
        x = needy_bitch_of_the_day
        l
    def James_bitches(self)
'''

def lazy_testing():
    trials = int(input("How many trials would you like to fake?"))
    for x in range(trials):
        year = datetime.datetime.strftime(datetime.datetime(random.randint(2000, 2015),
        random.randint(1, 12), random.randint(1, 28)), '%Y-%m-%d')


def working_hours():
        if datetime.datetime.today().weekday() == True:
            open_time = "09:00"
            close_time = "22:00"
        elif datetime.date.today().strftime("%A") == ("Saturday"):
            open_time = "09:00"
            close_time = "23:00"
        elif datetime.date.today().strftime("%A") == "Sunday":
            open_time = "09:00"
            close_time = "06:00"

        #start_stamp = datetime.datetime.now().strftime("%I:%M %p")
        if closing > start_stamp or start_stamp < "09:00":
            print("can rent")
        else:
            print("can't rent")

def random_time():
        #random start time
        start_stamp = datetime.datetime.strftime(datetime.datetime(random.randint(9, 22), random.randint(1,59), '%H: %m'))
        start_stamp_min = time_to_minutes(start_stamp)
        #total minutes in working day
        #random start time + random rental time
        rental_time = start_stamp_min + random.randint(0,360)


def time_to_minutes():
        #time to minutes
        t1 = datetime.datetime.strptime('13:05:36', '%H:%M:%S')
        t2 = datetime.datetime(1900,1,1)
        print((t1-t2).total_seconds() /60.0)
        return(print((t1-t2).total_seconds() /60.0))

def minutes_to_time():
        minutes = timedelta(minutes=250)
        time = strftime('%H:%M', gmtime(minutes.total_seconds()))
        #minutes = start_time + random.randint(1, 360)

class Manager:
    def __init__(self):
#to store instance of Table()
        self.pool_tables = self.pool_tables = []

    def create_pool_instances(self):
        for index in range(1,13):
            self.pool_table = Tables(index)
            self.pool_tables.append(self.pool_table)
      #print (pool_table.status) #access ass singular instance
      #self.menu()
        self.menu()

    def menu(self):
        print("Press [v] to view availability of tables.")
        print("Press [a] to checkout  a table. ")
        print("Press [d] to checkin a table ")
        print("Press [p] to print out record log. ")
        print("Press [q] to quit. ")
        self.option = input('Enter the letter to choose option.').lower()
        self.clear_screen()


        if self.option == "v":
            #clear_screen()

            self.availability()
            self.menu()

        elif self.option == "a":
            #clear_screen()
            self.availability()
            self.checkout_table()
            self.menu()

        elif self.option == "d":
            #clear_screen()
            self.availability()
            self.checkin_table()
            self.menu()

        elif self.option == "p":
            #clear_screen()
            self.print_record()
            self.menu()

        else:
            sys.exit

    def availability(self):
        print("These are the available tables.")
        for x in range(0,12):
            self.count = x + 1
            if self.pool_tables[x].status == "Available":
                print(f'Table {self.count} is Available')
            else:
                print(f'Table {self.count} is Unavailable')
        return

    def checkout_table(self):
        self.table_checkout = int(input("Enter the table # to checkout: "))
        self.pool_tables[self.table_checkout-1].check_out()
        #time.sleep(2)
        self.menu()
        return

    def checkin_table(self):
        self.table_checkin = int(input("Enter the table # to checkin: "))
        self.pool_tables[self.table_checkin-1].check_in()
        self.menu()
        return

    def print_record(self):
        self.pool_tables[self.table_checkout-1].record_time()

        print(self.pool_tables[self.table_checkout-1].start_stamp)
        print(self.pool_tables[self.table_checkin-1].stop_stamp)
        print(self.pool_tables[self.table_checkout-1].total_time)
        self.menu()
        return

    def clear_screen(self):
        #command = 'cls' if system_name().lower()=='windows' else 'clear'
        os.system('cls' if os.name=='nt' else 'clear')

manager1 = Manager()
manager1.create_pool_instances()
