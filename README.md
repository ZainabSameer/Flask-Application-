# Flask-Application-
## Real Estate Investment API

# Overview
The Real Estate Investment API is a Flask application that allows users to access and search property data stored in a CSV file. The API provides endpoints to retrieve all properties, get details of a specific property by ID, and search for properties based on location and name.

# Getting Started
## Prerequisites
Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)

## Install Required Packages
< pip install Flask pandas >

" Make sure you have your data.csv file placed in the same directory as the application. This file should contain the property data structured as outlined in the provided CSV format. "

## Run the Application
< python app.py >

## Get all properties
- URL: /data
- Method: GET
- Response: JSON array of all property records.
  #### GET http://127.0.0.1:5000/data

## Get property by ID
- URL: /data/<int:id>
- Method: GET
- Response: JSON object of the specified property or an error message if not found.
  ### GET http://127.0.0.1:5000/data/1

## Search for properties
- URL: /data/search
- Method: GET
- Query Parameters:
  - location: (optional) Filter properties by location.
  - property_name: (optional) Filter properties by name.
- Response: JSON array of matching properties or an error message if none found.
  ### GET http://127.0.0.1:5000/data/search?location=miami&property_name=beachfront%20condo

### Technologies Used
- Python: The primary programming language used for developing the application.
- Flask: A lightweight web framework for building web applications in Python. Flask is used to create the API endpoints and handle HTTP requests.
- Pandas: A powerful data manipulation and analysis library for Python, used to read and process the CSV file containing property data.
- CSV: The data format used to store property information, allowing for easy data manipulation and access.

