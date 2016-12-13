import pymysql as dB
from evaluate import connect


def cal_auc():
    cur = connect.cursor()
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    print("Database version : %s " % data)

if __name__ == '__main__':
    cal_auc()
    if connect:
        connect.close()

