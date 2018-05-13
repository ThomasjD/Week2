from Pool_table_manager import Manager
from Pool_table import Tables
import pickle


class Log:

    def__init__(self):
    	self.table = pool_tables


    def write_checkout(self):


    def write_checkin(self):


    def current_state(self):
        print ("This is current availability.")
        for x in pool_tables:
            if x.status == "Available":
                print ("Table #{x.status} is available")
            else:
                print ("Table #{x.status} is unavailable")


    def record_log(self):
        # with open('users.json', 'w') as file:
        #     file.write(json.dumps(pool))

        filename = 'testing.txt'
        outfile = open(filename,'wb')

        pickle.dump(self,outfile)
        outfile.close()



        infile = open(filename,'rb')
        loaded_data = pickle.load(infile)
        infile.close()

        print('this is our saved python we opened', print(loaded_data))
