""" Creates all the tables needed for the game
Expects a database to exist called 'game'
"""

import MySQLdb

def createdb():
    #access database
    db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="", db = "game")
    cur = db.cursor() 
    
    #create the tables
    sql = '''CREATE TABLE game_account (
            ACCOUNT_NAME CHAR(20) NOT NULL,
            ACCOUNT_PASS CHAR(20) NOT NULL,
            ACCOUNT_EMAIL CHAR(40) NOT NULL
        )
        '''
    cur.execute(sql)

if __name__ == "__main__":
   createdb()