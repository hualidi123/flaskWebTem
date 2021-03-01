# _*_ coding:utf-8 _*_

from api.resource import APIView
from api.modules.db_pool import DB

from flask import current_app
import json


class AppRank(APIView):
    url_prefix = "/apprank"

    def __init__(self):
        super(APIView, self).__init__()

    def get(self):
        conf = current_app.config
        db = DB(DBname="XBOPS", conf=conf)
        connect, coursor = db.get_connection()

        sql = "select DATE_FORMAT(currenttime,'%Y-%m-%d') as time,project,projectManager,count(1) as count from alarm_rank where currenttime>\"2021-01-11 00:00:00\" group by time,project,projectManager;"
        coursor.execute(sql)
        data = coursor.fetchall()
        print(data)

        db.close_connection(connect, coursor)
        return self.jsonify(data)


class ProjectRank(APIView):
    url_prefix = "/projectrank"

    def __init__(self):
        super(APIView, self).__init__()

    def get(self):
        conf = current_app.config
        db = DB(DBname="XBOPS", conf=conf)
        connect, coursor = db.get_connection()

        sql = "select DATE_FORMAT(currenttime,'%Y-%m-%d') as time,app,projectManager,count(1) as count from alarm_rank where currenttime>\"2021-01-11 00:00:00\" group by time,app,projectManager;"
        coursor.execute(sql)
        data = coursor.fetchall()
        print(data)

        db.close_connection(connect, coursor)
        return self.jsonify(data)
