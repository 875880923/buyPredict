"""
用户维度:用户收藏同一家店商品的数目
描述:收藏了更有可能再买
"""
from gen_X_features import fromDate, toDate, fromDateTest, toDateTest

featureName = 'add_favourite_merchant'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT user_id,merchant_id,COUNT(*) as count
    FROM user_log
    WHERE action_type=3
    GROUP BY user_id,merchant_id;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`, `merchant_id`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDate, toDate, 'user_%s' % featureName))
