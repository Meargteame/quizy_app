from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_cors import CORS
db = SQLAlchemy(app)
CORS(app)



@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Quiz App Backend!"})

if __name__ == "__main__":
    app.run(debug=True)
