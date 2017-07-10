#functions for a ssh mysql connection and a redshift postgres connection
#fill out parameters correctly
#save as sql.py to .../anaconda/lib/python3.6/site-packages/

#examples
'''
import sql
query = 'select * from users limit 1'
sql.mysql(query)
sql.postgres(query)
'''

def mysql(query):
    import pymysql
    import paramiko
    import pandas as pd
    from paramiko import SSHClient
    from sshtunnel import SSHTunnelForwarder

    #parameters
    sql_hostname = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    sql_username = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    sql_password = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    sql_main_database = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    sql_port = 3306
    ssh_host = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    ssh_user = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    ssh_pass = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    ssh_port = 22

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_pass,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data

def postgres(query):
    import psycopg2 as pg
    import pandas.io.sql as psql

    #parameters
    user = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    pasw = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    host = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

    params = {'host': host, 'user': user, 'password': pasw, 'dbname': 'wiw', 'port': '5439'}
    conn = pg.connect(**params)
    data = psql.read_sql(query, conn)
    conn.close()
    return data
