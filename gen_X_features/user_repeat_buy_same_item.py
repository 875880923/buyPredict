"""
用户维度:用户在同一家店重复购买一件商品的次数
描述:用户是否有重复购买的习惯
"""
from gen_X_features import fromDate, toDate, fromDateTest, toDateTest

featureName = 'repeat_buy_same_item'


def gen(from_date=None, to_date=None, table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT user_id,COUNT(*) as count FROM item_repeat_buy irb
    WHERE irb.count >= 2
    GROUP BY user_id;
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`);
    """
    return sql_template.format(table_name=table_name, from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    print(gen(fromDate, toDate, 'user_%s' % featureName))
