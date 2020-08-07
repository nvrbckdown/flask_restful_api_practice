from flask import request, jsonify
from flask_restful import Resource

class Say_hello(Resource):
    def get(self):
        return Calculations.response("Hello World", 200)


class Repeater(Resource):
    def post(self):
        coming_data = request.get_json()
        res = Responses()
        if self.message_field_validation(coming_data) == 301:
            return res.response("Missing value", 301)
        else:
            return res.response(coming_data["Message"], 200)

    def message_field_validation(self):
        if "Message" not in coming_data:
            return 301
        else:
            return 200


class Arithmetic_operation(Resource):
    """Arithmetic operation handler"""
    def post(self):
        data_from_user = request.get_json()
        math_operations = Calculations(data=data_from_user)
        return math_operations.arithmetic_operation()


class Calculations():
    """Main logic of App"""
    coming_data = {}

    def __init__(self, data):
        self.coming_data = data

    def arithmetic_operation(self):
        res = Responses()
        validation = self.data_validation()
        if validation == 301:
            return res.response("Missing value", 301)
        elif validation == 405:
            return res.response("Method not allowed", 405)
        else:
            return res.response(self.calculate(), 200)

    def calculate(self):
        operation = self.coming_data['operation']
        x = self.coming_data['var_x']
        y = self.coming_data['var_y']
        if operation == "Add":
            z = int(x) + int(y)
        elif operation == "Subtract":
            z = int(x) - int(y)
        elif operation == "Divide":
            z = int(x) / int(y)
        elif operation == "Multiply":
            z = int(x) * int(y)
        else:
            return "Incorrect Operation!"
        return z

    def data_validation(self):
        if "var_x" not in self.coming_data or "var_y" not in self.coming_data:
            return 301
        elif "var_y" == 0:
            return 405
        else:
            return 200


class Responses():
    message = "Success!"
    status_code = 200

    def response(self, message, status_code):
        resJSON = {
            "Message": message,
            "StatusCode": status_code
        }
        return jsonify(resJSON)
