# -*- coding:utf-8 -*-

import os
import sys
from inspect import getmembers, isclass

import six
from flask import jsonify
from flask_restful import Resource


class APIView(Resource):
    def __init__(self):
        super(APIView, self).__init__()

    @staticmethod
    def jsonify(*args, **kwargs):
        return jsonify(*args, **kwargs)


HERE = os.path.abspath(os.path.dirname(__file__))
# API_PACKAGE = os.path.join(HERE, "api")


def register_resources(resource_path, rest_api):
    for root, _, files in os.walk(os.path.join(resource_path)):
        for filename in files:
            if not filename.startswith("__") and filename.endswith(".py"):
                module_path = os.path.join(HERE, root[root.index("views"):])
                if module_path not in sys.path:
                    sys.path.insert(1, module_path)
                view = __import__(os.path.splitext(filename)[0])
                resource_list = [i[0] for i in getmembers(
                    view) if isclass(i[1]) and issubclass(i[1], Resource) and i[0] != "APIView"]
                for resource_cls_name in resource_list:
                    resource_cls = getattr(view, resource_cls_name)
                    if not hasattr(resource_cls, "url_prefix"):
                        setattr(resource_cls, "url_prefix", ("",))
                    if isinstance(resource_cls.url_prefix, six.string_types):
                        resource_cls.url_prefix = (resource_cls.url_prefix,)
                    rest_api.add_resource(
                        resource_cls, *resource_cls.url_prefix)
