import os
from flask import Flask, jsonify, abort, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = os.getenv('DEBUG')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(405)
def method_not_allow(e):
    return jsonify({"error": "Method not allow"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Error Interno del Servidor"}), 500

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():

    #abort(500)
    response = {
        "message": "Server running successfully"
    }
    
    return jsonify(response)


@app.route('/name/<name>/<lastname>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def show_name(name, lastname):
    response = {
        "name": name,
        "lastname": lastname
    }
    
    return jsonify(response)

@app.route('/test-post', methods=['POST', 'PUT'])
def get_info_by_form_data():

    query_data = request.args

    form_data = request.form

    response = {
        "name": form_data["name"],
        "lastname": form_data["lastname"],
        "limit": query_data.get('limit')
    }
    
    return jsonify(response)

@app.route('/test-json-data', methods=['POST', 'PUT'])
def get_info_by_json_data():

    json_data = request.json

    response = {
        "name": json_data["name"],
        "lastname": json_data["lastname"]
    }
    
    return jsonify(response)




if __name__ == '__main__':
    app.run()