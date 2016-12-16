"""
商家维度:商家重复购买用户的商品的数量
描述:商家是不是有 某些商品 容易被用户重复购买
优化点:数量值差距比较大(0-3000), 最好处理下
"""
from gen_X_features import fromDate, toDate, fromDateTest, toDateTest

featureName = 'sell_repeat_item'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT merchant_id,COUNT(*) as count FROM(
    SELECT user_id,merchant_id,COUNT(*) as count
    FROM item_repeat_buy
    GROUP BY user_id,merchant_id
    )item_merchant
    WHERE  item_merchant.count >=2
    GROUP BY merchant_id;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`merchant_id`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDate, toDate, 'merchant_%s' % featureName))

