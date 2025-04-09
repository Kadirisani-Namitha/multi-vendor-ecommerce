from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.db import mongo
from flask_jwt_extended import create_access_token
import datetime

auth_bp = Blueprint("auth", __name__)

# User Registration
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "password", "role")):
        return jsonify({"error": "Missing required fields"}), 400

    existing_user = mongo.db.users.find_one({"username": data["username"]})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = generate_password_hash(data["password"])
    user = {
        "username": data["username"],
        "password": hashed_pw,
        "role": data["role"],
        "createdAt": datetime.datetime.utcnow()
    }
    mongo.db.users.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    user = mongo.db.users.find_one({"username": data["username"]})
    if user and check_password_hash(user["password"], data["password"]):
        token = create_access_token(
            identity={"username": user["username"], "role": user["role"]},
            expires_delta=datetime.timedelta(hours=24)
        )
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
