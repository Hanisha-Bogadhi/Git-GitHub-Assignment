from flask import Flask, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

app = Flask(__name__)


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["todo_db"]
collection = db["todo_items"]

# API route
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    data = {
        "itemName": item_name,
        "itemDescription": item_desc
    }

    collection.insert_one(data)

    return "Item saved successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)