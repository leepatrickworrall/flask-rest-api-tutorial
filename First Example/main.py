from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "lee": {"Age": 24, "Gender": "Male"},
    "lisa": {"Age": 33, "Gender": "Female"}
}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)