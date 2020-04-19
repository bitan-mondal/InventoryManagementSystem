import string
import random
import mysql.connector
import pyfiglet


def genID():
    """ 
    Descripton: 
        This method generates Item_ID through random function whenever we need to insert a new row in the Database
    Input Parameters:
        NA
    Output: 
        Item ID
    """

    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(10)))


def get_db_connection():
    """ 
    Descripton: 
        This method establishes Database connection using the User Name and Password
    Input Parameters:
        NA
    Output:
        Returns touple of Database connections and its curser
    """

    db = mysql.connector.connect(host="localhost",user="Bitan",passwd='Bitan987',database="test")
    return db, db.cursor()


def decorative_text(word):
    """ 
    Descripton: 
        This method is used to is used to Format Text
    Input Parameters:
        Takes input as normal text
    Output: 
        Returns formated text
    """

    print(pyfiglet.figlet_format(word))