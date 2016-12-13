import pyMsSQL as dB


con = None
try:
    con = dB.connect('localhost', 'root',
                      'root', 'test')
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    print("Database version : %s " % data)
finally:
    if con:
        con.close()
