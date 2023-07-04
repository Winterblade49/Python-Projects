
import sqlite3 

def Connect(Connection_Query, Connection_Query2, values):  
    conn = sqlite3.connect('test.db')   
    with conn: 
        cur = conn.cursor() 
        cur.execute(Connection_Query) 
        cur.executemany(Connection_Query2, values)  
        conn.commit()
    conn.close() 

filelist = ('information.dox','Hello.txt','myImage.png','myMovie.png','World.txt','data.pdf','myPhoto.jpg') 
values = [(file,) for file in filelist]   

Connect(Connection_Query="CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filelist TEXT)", 
        Connection_Query2="INSERT INTO tbl_files(col_filelist) VALUES (?)",
        values=values) 
