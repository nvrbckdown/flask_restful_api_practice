from flask import Flask
from flask_restful import Api
from resources import Say_hello, Repeater, Arithmetic_operation


app = Flask(__name__)
api = Api(app=app)


api.add_resource(Say_hello, "/")
api.add_resource(Repeater, "/repeat")
api.add_resource(Arithmetic_operation, "/math")


if __name__ == "__main__":
    app.run()
