#-*-coding:utf-8-*-
'''
Created on 2017年3月27日

@author: admin
'''
import mysql.connector



def connect():
    config={'host':'127.0.0.1',
                'user':'root',
                'password':'root',
                'port':3306,
                'database':'history',
                'charset':'utf8'
            }
    try:
        conn=mysql.connector.connect(**config)
        return conn
        print("conn is success!")
    except mysql.connector.Error as e:
        print("conn is fails{}".format(e))

def select_table(ip='192.168.153.129'):
    sql_select="select * from history where ip= '%s' " % (ip)
    result=[]
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()#queryset返回列表
        print(result)
        return result
    except mysql.connector.Error as e:
        print("select cursor is faild".format(e))
    conn.close()
        
def update_sql(list_args):
    if (len(list_args)>5):
        return
    print("list_args",list_args)
    sql_insert = "INSERT INTO history(ip,\
       his_id, his_user, his_time, his_command)\
       VALUES ('%s', '%s', '%s', '%s', '%s' )" %\
       (list_args[1], list_args[0], list_args[2], list_args[3], list_args[4])
    print("sql_insert",sql_insert)
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_insert)
        conn.commit()
    except mysql.connector.Error as e:
        print("update cursor is faild".format(e))  
        conn.rollback()
    conn.close()