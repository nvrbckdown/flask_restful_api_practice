from flask import request, jsonify
from flask_restful import Resource

class Say_hello(Resource):
    def get(self):
        return Validation_and_Response.response("Hello World", 200)


class Repeater(Resource):
    def post(self):
        validate = Validation_and_Response()
        coming_data = request.get_json()
        if validate.message_field_validation(data_from_user) == 301:
            return validate.response("Missing value", 301)
        else:
            return validate.response(data_from_user["Message"], 200)


class Arithmetic_operation(Resource):
    """Arithmetic operation handler"""
    def post(self):
        data_from_user = request.get_json()
        math_operations = Validation_and_Response(data=data_from_user)
        return math_operations.arithmetic_operation()


class Validation_and_Response():
    """Main logic of App"""
    coming_data = {}

    def __init__(self, data):
        self.coming_data = data

    def arithmetic_operation(self):
        operation = self.coming_data['operation']
        validation = self.data_validation()
        if validation == 301:
            return self.response("Missing value", 301)
        elif validation == 405:
            return self.response("Method not allowed", 405)
        else:
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
                return self.response("Incorrect Operation!", 405)
            return self.response(z, 200)

    def message_field_validation(self):
        if "Message" not in self.coming_data:
            return 301
        else:
            return 200

    def data_validation(self):
        if "var_x" not in self.coming_data or "var_y" not in self.coming_data:
            return 301
        elif "var_y" == 0:
            return 405
        else:
            return 200

    def response(self, message, status_code):
        resJSON = {
            "Message": message,
            "StatusCode": status_code
        }
        return jsonify(resJSON)
