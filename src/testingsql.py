import sqlalchemy as sa

database_file = 'products.db'
table = 'products'

db = sa.create_engine(f'sqlite:///{database_file}')

metadata = sa.MetaData(bind=db)
current_table = sa.Table(table, metadata, autoload=True)
query = current_table.select()
res = db.execute(query)


for elem in current_table.columns:
    print(elem.name)

print([column.name for column in current_table.columns])

item_id = 10
query = current_table.select().where(current_table.columns.id==item_id)
res = db.execute(query)

print(*res)
