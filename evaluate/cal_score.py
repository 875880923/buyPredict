from evaluate import connect
import numpy as np
from sklearn import metrics


def cal_auc():
    cur = connect.cursor()
    cur.execute("SELECT * FROM train_data")
    rows = cur.fetchall()
    data = np.array(rows, dtype='float')
    label = data[:, 2:3]
    prob = data[:, 3:4]
    result = metrics.auc(label, prob, True)
    print("%.4f" % result)


if __name__ == '__main__':
    cal_auc()
    if connect:
        connect.close()

