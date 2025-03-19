# Flask-Application-
## Real Estate Investment API

# Overview
The Real Estate Investment API is a Flask application that allows users to access and search property data stored in a CSV file. The API provides endpoints to retrieve all properties, get details of a specific property by ID, and search for properties based on location and name.

# Get all properties
- URL: /data
- Method: GET
- Response: JSON array of all property records.
  ### GET http://127.0.0.1:5000/data

# Get property by ID
- URL: /data/<int:id>
- Method: GET
- Response: JSON object of the specified property or an error message if not found.

# Search for properties
- URL: /data/search
- Method: GET
- Query Parameters:
  - location: (optional) Filter properties by location.
  - property_name: (optional) Filter properties by name.
- Response: JSON array of matching properties or an error message if none found.
