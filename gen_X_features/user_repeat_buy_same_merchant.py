"""
用户维度:用户在同一家店购买不同商品的次数
描述:用户是否有重复购买某个商家的行为
"""
from gen_X_features import fromDate, toDate, fromDateTest, toDateTest

featureName = 'repeat_buy_same_merchant'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT user_id,COUNT(*) as count FROM(
    SELECT user_id,merchant_id,COUNT(*) as count
    FROM item_repeat_buy
    GROUP BY user_id,merchant_id
    )item_merchant
    WHERE  item_merchant.count >=2
    GROUP BY user_id;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDate, toDate, 'user_%s' % featureName))
