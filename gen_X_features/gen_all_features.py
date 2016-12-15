all_features_table_name = "all_features"
all_features_prediction_table_name = "all_features_prediction"


def gen(train_table=None, tables=None, column_condition=None, table_name=None):
    show_col = ',\n\t'.join([key + '.' + col + ' as ' + key + '_' + col
                             for key in tables.keys()
                             for col in tables[key]
                             if col not in column_condition])

    left_join = '\n\tLEFT JOIN '.join(key + ' on (' + ' and '
                                      .join(['{0}.' + condition + '=' + key + '.' + condition
                                             for condition in column_condition
                                             if condition in tables[key]]) + ')'
                                      for key in tables.keys()).format(train_table)

    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT
    {train_table}.*,
    {show_col}
    FROM
    {train_table} LEFT JOIN {left_join};
    """
    return sql_template.format(table_name=table_name, show_col=show_col, train_table=train_table, left_join=left_join)


if __name__ == '__main__':
    table_dic = {
        'user_repeat_buy_same_item': ['user_id', 'count'],
        'user_repeat_buy_same_merchant': ['user_id', 'count'],
        'user_add_favourite_merchant': ['user_id', 'merchant_id', 'count']
    }
    print(gen('train_and_test_data', table_dic, ['user_id', 'merchant_id'], all_features_table_name))
    print(gen('prediction', table_dic, ['user_id', 'merchant_id'], all_features_prediction_table_name))
