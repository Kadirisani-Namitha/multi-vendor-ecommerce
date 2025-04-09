from flask import Blueprint, request, jsonify, current_app
from app.utils.db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# ✅ Blueprint first
customer_bp = Blueprint("customer", __name__)

# ✅ Registration Route
@customer_bp.route("/register", methods=["POST"])
def register_customer():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    existing_user = mongo.db.customers.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "Customer already exists"}), 409

    hashed_pw = generate_password_hash(password)
    mongo.db.customers.insert_one({"email": email, "password": hashed_pw})

    return jsonify({"message": "Customer registered successfully"}), 201

# ✅ Login Route (after declaring customer_bp)
@customer_bp.route("/login", methods=["POST"])
def login_customer():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = mongo.db.customers.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        "email": user["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, current_app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token}), 200
