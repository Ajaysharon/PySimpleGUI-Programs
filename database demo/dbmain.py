import sqlite3

sql_query="""create table student(
    id integer primary key,
    name text,
    department text
)"""

db=sqlite3.connect('mydb')
cursor=db.cursor()
cursor.execute(sql_query)
db.commit()