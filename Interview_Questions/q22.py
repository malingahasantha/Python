# importing module
import cx_Oracle

try:
    conStr = "hr/hr@localhost:1521/xe"  #connection string
    conn = cx_Oracle.connect(conStr)    #create connection

except cx_Oracle.DatabaseError as er:
    print('Error while connecting to the database:', er)

else:
    try:
        cur = conn.cursor()
        #cursor() is required to execute a SQL query and to provide results some special object

        # fetchall() is used to fetch all records from result set
        cur.execute('select * from customer')
        rows = cur.fetchall()
        print(rows)

        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        cur.execute('select * from customer')
        rows1 = cur.fetchmany(2)
        print(rows1)

        # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from customer')
        rows2 = cur.fetchone()
        print(rows2)


    except Exception as err:
        print('There is an error in the Oracle database')
        print(err)

    # finally:
    #     if(cur):
    #         cur.close()
    
finally:
    if(cur):
        cur.close()
    if(conn):
        conn.close()
#After all done it is mandatory to close all operations.

print('execution completed!')