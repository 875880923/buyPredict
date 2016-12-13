from buildData import testDataCount


def gen(table_name=None):
    sql_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} AS
    SELECT * FROM train_and_test_data
    limit 0,{testDataCount};
    ALTER TABLE {table_name} ADD PRIMARY KEY  (`user_id`, `merchant_id`);
    """
    return sql_template.format(table_name=table_name, testDataCount=testDataCount)

if __name__ == '__main__':
    print(gen('test_data'))
