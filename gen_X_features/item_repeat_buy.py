
from gen_X_features import fromDate, toDate, fromDateTest, toDateTest

featureName = 'repeat_buy'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT user_id,merchant_id,item_id,cat_id,brand_id,COUNT(*) as count FROM user_log
    WHERE time_stamp >= '{from_date}' AND time_stamp <= '{to_date}' AND action_type='2'
    GROUP BY user_id,item_id,merchant_id;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`, `merchant_id`, `item_id`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDate, toDate, 'item_%s' % featureName))
