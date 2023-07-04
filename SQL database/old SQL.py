import sqlite3

def Connect(Connection_Query,Connection_Query2):
    conn = sqlite3.connect('test.db')
    with conn:
        cur = conn.cursor()
        cur.execute(Connection_Query)
        cur.execute(Connection_Query2)
        conn.commit()
    conn.close()


filelist = ('information.dox','Hello.txt','myImage.png','myMovie.png','World.txt,','data.pdf','myPhoto.jpg')
string1 = str(filelist[0])
string2 = str(filelist[1])
string3 = str(filelist[2])
string4 = str(filelist[3])
string5 = str(filelist[4])
string6 = str(filelist[5])
string7 = str(filelist[6])



Connect(Connection_Query=("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_filelist TEXT)"),Connection_Query2=("INSERT INTO tbl_files(col_filelist) VALUES (?,?,?,?,?,?,?)",\
            (string1),\
            (string2),\
            (string3),\
            (string4),\
            (string5),\
            (string6),\
            (string7),))