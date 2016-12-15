from evaluate import connect
from train_modle import testDataCount
from gen_X_features.gen_all_features import all_features_table_name, all_features_prediction_table_name
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


def get_data(table_name):
    sql_template = """
    SELECT * FROM {table_name};
    """
    sql_template = sql_template.format(table_name=table_name)
    df = pd.read_sql(sql_template, connect)
    df.fillna(0, inplace=True)
    return df.values


def lr_fit(features, label):
    classifier = LogisticRegression()
    classifier.fit(features, label)
    return classifier


def predict(model):
    data_predict = get_data(all_features_prediction_table_name)
    x_features_predict = data_predict[:, 3:]
    predict_result = model.predict_proba(x_features_predict)
    prob = predict_result[:, 1:2]
    prediction = pd.DataFrame(data_predict[:, 0:2], columns=['user_id', 'merchant_id'], dtype=int)
    prediction['prob'] = prob
    prediction.to_csv("E:/data/prediction.csv", index=False)

if __name__ == '__main__':
    try:
        data = get_data(all_features_table_name)
        test_data = data[:testDataCount, :]
        train_data = data[testDataCount+1:, :]

        y = train_data[:, 2:3]
        X_features = train_data[:, 4:]
        model = lr_fit(X_features, y.ravel())

        label = test_data[:, 2:3]
        x_features_test = test_data[:, 4:]
        result = model.predict_proba(x_features_test)

        prob = result[:, 1:2]
        print(metrics.roc_auc_score(label, prob))

        test_result = pd.DataFrame(test_data[:, 0:3], columns=['user_id', 'merchant_id', 'label'], dtype=int)
        test_result['prob'] = prob
        print(test_result)

        # predict(model)

    finally:
        if connect:
            connect.close()
