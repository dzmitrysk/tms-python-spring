import sqlalchemy as sa


class SQLiteDataBase:
    def __init__(self, database_file: str):
        self.db = sa.create_engine(f'sqlite:///{database_file}')

    def get_all_columns(self, table: str) -> '[]':
        metadata = sa.MetaData(bind=self.db)
        current_table = sa.Table(table, metadata, autoload=True)
        return [column.name for column in current_table.columns]

    def get_all_items(self, table: str) -> '[{}, {}]':
        metadata = sa.MetaData(bind=self.db)
        current_table = sa.Table(table, metadata, autoload=True)
        columns = self.get_all_columns(table)
        query = current_table.select()
        rows = self.db.execute(query)
        all_items = [{column: row[index] for index, column in enumerate(columns)} for row in rows]
        return all_items

    def get_item_by_id(self, table: str, item_id) -> []:
        metadata = sa.MetaData(bind=self.db)
        current_table = sa.Table(table, metadata, autoload=True)
        query = current_table.select().where(current_table.columns.id == item_id)
        item = self.db.execute(query)
        return [elem for elem in item][0]

    def add_item(self, table: str, **attributes):
        columns = self.get_all_columns(table)
        if len(attributes) > len(columns) or not set(attributes.keys()).issubset(columns):
            raise ValueError('Wrong set of attributes for current table!')

        metadata = sa.MetaData(bind=self.db)
        current_table = sa.Table(table, metadata, autoload=True)
        query = current_table.insert().values(attributes)
        self.db.execute(query)

    def update_item_by_id(self, table: str, item_id, **attributes):
        columns = self.get_all_columns(table)
        if len(attributes) > len(columns) or not set(attributes.keys()).issubset(columns):
            raise ValueError('Wrong set of attributes for current table!')

        metadata = sa.MetaData(bind=self.db)
        current_table = sa.Table(table, metadata, autoload=True)
        query = current_table.update().values(attributes)

        query = current_table.update().where(current_table.columns.id == item_id)

        self.db.execute(query)


        # columns = self.get_all_columns(table)
        # if len(attributes) > len(columns) or not set(attributes.keys()).issubset(columns):
        #     raise ValueError('Wrong set of attributes for current table!')
        #
        # self.db.execute(f'''
        #     UPDATE '{table}'
        #     SET {tuple(attributes.keys())} = {tuple(attributes.values())}
        #     WHERE id = '{item_id}'
        #     ''')

    def delete_item_by_id(self, table: str, item_id):
        self.db.execute(f'''
            DELETE FROM '{table}'
            WHERE id = '{item_id}'
            ''')
