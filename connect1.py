import pymysql
class connect2:
    def conn(self):
        con = pymysql.connect(host='localhost',user='root',password='',db='bankdb',charset='utf8mb4')
        return con

'''
pymysql ->It is a predefined package/module
connect() ->It is also a predefined method used to cretea a connection
        between python to mysql.It takes following arguments
        1)Server name ->name of the server where mysql is installed
                    here localhost.
        2)username -> root
        3)password ->""
        4)database name ->fribankdb
'''
        
