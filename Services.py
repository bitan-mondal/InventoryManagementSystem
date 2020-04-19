import string
import random
import mysql.connector
import pyfiglet

"""It generates Item_ID through random function whenever we need to insert a new row in the Database"""

def genID():
    print("gen id")
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(10)))

"""It establishes Database connecting using the User Name and Password"""

def get_db_connection():
    db = mysql.connector.connect(host="localhost",user="Bitan",passwd='Bitan987',database="test")
    return db, db.cursor()

"""It is used to Format Text"""

def decorative_text(word):
    print(pyfiglet.figlet_format(word))