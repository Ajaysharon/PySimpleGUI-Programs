import sqlite3

def execute_query(sql_query):
    with sqlite3.connect('mydb') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result

#sql_query="""INSERT INTO STUDENT (NAME,DEPARTMENT) VALUES('%s','%s') """ %('aJAY','AD')

sql_query="""SELECT * FROM STUDENT"""
RESULT=execute_query(sql_query)
print(RESULT.fetchall())