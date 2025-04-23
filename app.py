from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)

# Use your actual database and collection names
db = client["Students"]
students_collection = db["StudentScheduleInfo"]

app = Flask(__name__)

@app.route("/")
def home():
    students = list(students_collection.find({}, {"_id": 0}))  # Exclude MongoDB _id field
    return render_template("index.html", students=students)

@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.json
    students_collection.insert_one(data)
    return jsonify({"msg": "Student added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
