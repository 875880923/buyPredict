
from gen_X_features import fromDateTrain, toDateTrain

featureName = 'repeat_buy'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT * FROM (
    SELECT user_id,item_id,merchant_id,COUNT(*) as count FROM user_log
    WHERE time_stamp >= '{from_date}' AND time_stamp <= '{to_date}' AND action_type='2'
    GROUP BY user_id,item_id
    )purchase_count
    WHERE purchase_count.count>0;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`, `item_id`);
    CREATE INDEX count_idx ON {table_name} (`count`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDateTrain, toDateTrain, 'item_%s_train' % featureName))
