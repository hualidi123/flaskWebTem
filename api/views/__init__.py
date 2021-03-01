import os
from flask import Blueprint
from flask_restful import Api

from api.resource import register_resources

HERE = os.path.abspath(os.path.dirname(__file__))


# test
blueprint_test = Blueprint("alertMsg", __name__, url_prefix="/api")
test_rest = Api(blueprint_test)
register_resources(os.path.join(HERE, "alertMsg"), test_rest)
