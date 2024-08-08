from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class CreateScript(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "Invalid request"}, 400

        script_id = "12345"  # Placeholder for created script ID
        title = data.get("title")

        return jsonify({
            "id": script_id,
            "title": title,
            "message": "Script created successfully"
        })

api.add_resource(CreateScript, '/createScript')

if __name__ == '__main__':
    app.run(debug=True)
