import pymysql
from dbutils.pooled_db import PooledDB

# pymysql + 连接池 替代sqlachemy


class DB(object):
    __pool = None

    def __init__(self, DBname, conf):
        self.pool = DB.__get_conn_pool(DBname, conf)

    @staticmethod
    def __get_conn_pool(DBname, conf):
        if DB.__pool is None:
            try:
                DB.__pool = PooledDB(creator=pymysql, host=conf.get(DBname).get("host"), port=int(conf.get(DBname).get("port")),
                                     user=conf.get(DBname).get("user"), passwd=conf.get(DBname).get("password"),
                                     db=conf.get(DBname).get("db"), charset=conf.get(DBname).get("charset"))
            except Exception as e:
                print(e)
        return DB.__pool

    def get_connection(self):
        conn = self.pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def close_connection(self, conn, cursor):
        if cursor:
            cursor.close()
        if conn:
            conn.close()
