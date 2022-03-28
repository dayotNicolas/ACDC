from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///covid.db', echo=True)
meta = MetaData()

departments = Table(
    'departments',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('number', String),
    Column('death', Integer),
    Column('icu_occupation', Integer),
    Column('vaccination', Integer),
    Column('positivity_rate', Integer)
)

addresses = Table(
    'department_list', meta,
    Column('id', Integer, primary_key=True),
    Column('dpt_id', Integer, ForeignKey('departments.id')),
    Column('dpt_number', String),
    Column('region', String))

ins = departments.insert()
for i in list:
    ins = departments.insert().values(name=f'{i}', number=f'{i}',
                                      death=f'{i}', icu_occupation=f'{i}',
                                      vaccination=f'{i}', positivity_rate=f'{i}')

meta.create_all(engine)

conn = engine.connect()
s = departments.select()
conn.execute(s).fetchall()
