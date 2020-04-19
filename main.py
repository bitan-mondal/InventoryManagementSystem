from Services import get_db_connection
from Services import genID
from Services import decorative_text


class Chair:
    def __init__(self, companyName, modelName, hsn, rate):
        self.item_id = genID()
        self.company_name = companyName
        self.model_name = modelName
        self.hsn = hsn
        self.rate = rate
    
    def populate(self,cursor,db):
        sql = 'insert into Stocks values (%s,%s,%s,%s,%s,%s)'
        val = (self.item_id,"Chair",self.company_name,self.model_name,self.hsn,self.rate)
        cursor.execute(sql,val)
        sql = 'select * from Stocks where item_id = %s'
        val = (self.item_id,)
        cursor.execute(sql,val)
        record = cursor.fetchone()
        print('The following data hs been a dded:\n\n   Item ID | Item Name |Company Name| Model|       HSN    |     RATE\n  ')
        print(' {0[0]:15s} {0[1]:10s} {0[2]:10s} {0[3]:10s} {0[4]:10s} {0[5]:10f}'.format(record))
        db.commit()

class Wardrobe:
    def __init__(self, companyName, modelName, hsn, rate):
        self.item_id = genID()
        self.company_name = companyName
        self.model_name = modelName
        self.hsn = hsn
        self.rate = rate
    
    def populate(self,cursor,db):
        sql = 'insert into Stocks values (%s,%s,%s,%s,%s,%s)'
        val = (self.item_id,"Wardrobe",self.company_name,self.model_name,self.hsn,self.rate)
        cursor.execute(sql,val)
        sql = 'select * from Stocks where item_id = %s'
        val = (self.item_id,)
        cursor.execute(sql,val)
        record = cursor.fetchone()
        print('The following data hs been added:\n\n   Item ID | Item Name |Company Name| Model|       HSN    |     RATE\n  ')
        print(' {0[0]:15s} {0[1]:10s} {0[2]:10s} {0[3]:10s} {0[4]:10s} {0[5]:10f}'.format(record))        
        db.commit() 

class Table:
    def __init__(self, companyName, modelName, hsn, rate):
        self.item_id = genID()
        self.company_name = companyName
        self.model_name = modelName
        self.hsn = hsn
        self.rate = rate
    
    def populate(self,cursor,db):
        sql = 'insert into Stocks values (%s,%s,%s,%s,%s,%s)'
        val = (self.item_id,"Table",self.company_name,self.model_name,self.hsn,self.rate)
        cursor.execute(sql,val)
        sql = 'select * from Stocks where item_id = %s'
        val = (self.item_id,)
        cursor.execute(sql,val)
        record = cursor.fetchone()
        print('The following data hs been added:\n\n   Item ID | Item Name |Company Name| Model|       HSN    |     RATE\n  ')
        print(' {0[0]:15s} {0[1]:10s} {0[2]:10s} {0[3]:10s} {0[4]:10s} {0[5]:10f}'.format(record))        
        db.commit() 

class Sofa:
    def __init__(self, companyName, modelName, hsn, rate):
        self.item_id = genID()
        self.company_name = companyName
        self.model_name = modelName
        self.hsn = hsn
        self.rate = rate
    
    def populate(self,cursor,db):
        sql = 'insert into Stocks values (%s,%s,%s,%s,%s,%s)'
        val = (self.item_id,"Sofa",self.company_name,self.model_name,self.hsn,self.rate)
        cursor.execute(sql,val)
        sql = 'select * from Stocks where item_id = %s'
        val = (self.item_id,)
        cursor.execute(sql,val)
        record = cursor.fetchone()
        print('The following data hs been added:\n\n   Item ID | Item Name |Company Name| Model|       HSN    |     RATE\n  ')
        print(' {0[0]:15s} {0[1]:10s} {0[2]:10s} {0[3]:10s} {0[4]:10s} {0[5]:10f}'.format(record))        
        db.commit()

# We have Used Factory Design Pattern and below is the implementation of the same
class Factory():

    def __init__(self):
        """
        Descripton: 
            Below Method establishes connection
        Input: 
            Host, User Name, Password, Database
        Output: 
            Connection to the Database 
        """
        self.db,self.cursor = get_db_connection()

        # It maps the class for checking if the value vatches with the class
        self.localizers = { "chair" : Chair, "wardrobe" : Wardrobe, "table" : Table, "sofa" : Sofa}
    
    def getDBCursor(self):
        return self.cursor

    def getDBConnection(self):
        """
        Descripton: 
            This method gets the Database Connection
        Input: 
            NA
        Output: 
            Return MySQL Database connection
        """
        return self.db

    def insert_db(self,item_name,company_name,model_name,hsn,rate):
        """ 
        Descripton: 
            This method takes input from customer and calls the Populate method to insert data int the Database
        Input Parameters:  
            item_name, company_name, model_name, hsn and rate 
        Output: 
            The above item data will be inserted into the Database 
        """
        return self.localizers[item_name.lower()](company_name,model_name,hsn,rate)

    def delete_db(self,item_id):
        """
        Descripton: 
            This method takes input from customer and delete the data from the Database according to Item ID
        Input Parameters:  
            item_id
        Output: 
            The data of the perticular item_id will be deleted from the Database
        """
        sql = 'delete from Stocks where item_id = %s'
        val = (item_id,)
        self.cursor.execute(sql,val)
        self.db.commit()

    def list_db(self,item_id):
        """
        Descripton: 
            This method takes input from customer and list the data from the Database according to Item ID
        Input Parameters:  
            item_id
        Output: 
            The data of the perticular item_id will be listed from the Database
        """
        sql = 'select * from test.stocks where item_id = %s '
        val = (item_id,)
        self.cursor.execute(sql,val)
        record = self.cursor.fetchone()
        if not record:
            print("Item not found!\n")
        else:
            print("\n   Item ID | Item Name |Company Name| Model|       HSN    |     RATE\n")
            print(' {0[0]:15s} {0[1]:10s} {0[2]:10s} {0[3]:10s} {0[4]:10s} {0[5]:10f}'.format(record)) 
    
    def update_db(self,item_id,new_item_value,to_update):
        """
        Descripton: 
            This method takes input from customer and updates the data from the Database according to Item ID
        Input Parameters:  
            item_id, new_item_value
        Output: 
            The data of the perticular item_id will be updated from the Database
        """
        sql = None
        val = None    
        if to_update == "company_name":
            sql = 'update Stocks set company_name = %s where item_id = %s'
            val = (new_item_value,item_id)
            
        elif to_update == "model_name":
            sql = 'update Stocks set model_name = %s where item_id = %s'
            val = (new_item_value,item_id)

        elif to_update == "hsn":
            sql = 'update Stocks set hsn = %s where item_id = %s'
            val = (new_item_value,item_id)

        elif to_update == "rate":
            sql = 'update Stocks set rate = %s where item_id = %s'
            val = (new_item_value,item_id)

        self.cursor.execute(sql,val)
        self.db.commit()   

    def if_present(self,item_id):
        """ 
        Descripton: 
            This method takes input as Item ID from customer and checks if the Item Id is present in the Database or not
        Input Parameters:
            item_id
        Output: 
            It checks if the Item Id is present or not and returns value in form of '0' or '1'
        """ 
        sql = 'select * from Stocks where item_id = %s'
        val = (item_id,)
        self.cursor.execute(sql,val)
        record = self.cursor.fetchone()
        if not record:
            return 0
        else:
            return 1

if __name__ == "__main__":

    choice = 10
    factoryObj = Factory()
    db_cursor = factoryObj.getDBCursor()
    db_dbConn = factoryObj.getDBConnection()
    
    print("\n\n•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    decorative_text("Welcome to IMS")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

    while True:

        print("\n• Press [1] to List all details of an item \n• Press [2] to Update details of an item\n• Press [3] to Delete an item\n• Press [4] to Add details of an item\n• Press [0] to Exit\n")
        choice = int(input("Enter your choice: "))
        if choice==0:
            break
        
        #-------------------------------- LIST ITEM --------------------------------#
        # Choice [1] : Condition to List details based on Item ID.

        if choice == 1:
            item_id= input("Enter the Item Id: ")
            factoryObj.list_db(item_id)

        #-------------------------------- UPDATE ITEM --------------------------------#
        # Choice [2] : Condition to Update Item details based on Item ID

        elif choice == 2:
            item_id = input("Enter the item ID: ")
            if factoryObj.if_present(item_id):
                print("\n• Press [1] to Enter the Company name \n• Press [2] to Enter the Model name\n• Press [3] to Enter the HSN number\n• Press [4] to Enter the Rate\n")
                updateChoice  = int(input("Enter your choice: "))

                if updateChoice == 1:
                    companyName = input("Enter the Company Name: ")
                    factoryObj.update_db(item_id,companyName,"company_name")
                    print("Company_Name: ",companyName," updated!")
                elif updateChoice == 2:
                    modelName = input("Enter the Model Name: ")
                    factoryObj.update_db(item_id,modelName,"model_name")
                    print("Model Name: ",modelName," updated!")
                elif updateChoice == 3:
                    hsn = input("Enter the HSN Number: ")
                    factoryObj.update_db(item_id,hsn,"hsn")
                    print("HSN: ",hsn," updated!")
                elif updateChoice == 4:
                    rate = float(input("Enter the Rate: "))
                    factoryObj.update_db(item_id,rate,"rate")
                    print("Rate: ",rate," updated!")                
            else:
                print("Item not found! Check Item Id!!!")

        #-------------------------------- DELETE ITEM --------------------------------#
        # Choice [3] : Condition to Delete Item details based on Item ID

        elif choice == 3:
            item_id = input("Enter the Item ID: ")

            if factoryObj.if_present(item_id) is not None:
                factoryObj.delete_db(item_id)
                print("Item Id: ",item_id," deleted!")
            else:
                print("Item not found! Check Item Id!!!")
        
        #-------------------------------- INSERT ITEM --------------------------------#
        # Choice [4] : Condition to Insert Item details. Item ID will be generated automatically

        elif choice == 4:
            m_item_name  = input("Enter thr Item Name : ")
            m_company_name  = input("Ente the Company Name : ")
            m_model_name  = input("Enter the Model Name : ")
            m_hsn  = input("Enter the HSN : ")
            m_rate  = float(input("Enter the Rate : "))

            itemObj = factoryObj.insert_db(m_item_name,m_company_name,m_model_name,m_hsn,m_rate)
            itemObj.populate(factoryObj.getDBCursor(),factoryObj.getDBConnection())
        else:
        # Choice [0] : Condition to Exit from the menu
            break

    print("\nThank you!\n")