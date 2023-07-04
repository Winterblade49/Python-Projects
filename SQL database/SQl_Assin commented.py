

import sqlite3 #importing sqlite3

def Connect(Connection_Query, Connection_Query2, values):  #def Connect along with values
    conn = sqlite3.connect('test.db')      #connecting to database the database is test.db
    with conn: #stating with connection 
        cur = conn.cursor() #start cursor
        cur.execute(Connection_Query) #exicute connection_Query
        cur.executemany(Connection_Query2, values)  #exicute connection_Query2 with these values(values)
        conn.commit() #commits changes
    conn.close() #closes connection

filelist = ('information.dox','Hello.txt','myImage.png','myMovie.png','World.txt','data.pdf','myPhoto.jpg') #list to commit to database
values = [(file,) for file in filelist]    #creates several tuples with a single value in each and passes each to values1

Connect(Connection_Query="CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filelist TEXT)", #creates table if its not there names tbl_files initiates col_filelist
        Connection_Query2="INSERT INTO tbl_files(col_filelist) VALUES (?)", #inserts values into tbl_files(col_filelist)  VALUES = tuple(values)
        values=values) # values = values1
            