from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///NOM.db', echo = True)
meta = MetaData()

departments = Table(
   'departments',
   meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('number', String),
   Column('death', Integer),
   Column('icu_occupation', Integer),
   Column('vaccination', Integer),
   Column('positivity_rate', Integer)
)


addresses = Table(
   'department_list', meta,
   Column('id', Integer, primary_key = True),
   Column('dpt_id', Integer, ForeignKey('departments.id')),
   Column('dpt_number', String),
   Column('region', String))

meta.create_all(engine)

conn = engine.connect()
s = departments.select()
conn.execute(s).fetchall()
