from flask import Flask, jsonify, request
import pandas as pd
app = Flask(__name__)

data = pd.read_csv('data.csv').to_dict(orient='records')

@app.route("/data", methods=["GET"])
def index():
    return jsonify({"data":data})

@app.route("/data/<int:id>", methods=["GET"])
def details(id):
    for property in data:
      if property.get("ID") == id:
        return jsonify(property)
    return jsonify({"error": "Property not found"}), 404

# @app.route("/data/search", methods=["GET"])
# def search():
#     location = request.args.get('location','').lower()
#     property_name = request.args.get('property_name','').lower()
#     for property in data:
#       if (not location or property.get("Location").lower() == location)\
#           and (not property_name or property.get("Property_Name").lower() == property_name):
#         return jsonify(property)
#     return jsonify({"error": "Property not found"}), 404



@app.route("/data/search", methods=["GET"])
def search():
    location = request.args.get('location','').lower()
    property_name = request.args.get('property_name','').lower()

    filtered_data = [item for item in data if (not location or item["Location"].lower() == location) and (not property_name or item["Property_Name"].lower() == property_name)]

    if not filtered_data:
        return jsonify({"error": "Properties not found"}), 404

    return jsonify({"result":filtered_data})

if __name__ == '__main__':
    app.run(debug=True)