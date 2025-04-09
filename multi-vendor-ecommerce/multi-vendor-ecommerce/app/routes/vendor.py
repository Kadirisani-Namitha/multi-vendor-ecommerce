from flask import Blueprint, request, jsonify
from app.utils.db import mongo
from werkzeug.security import generate_password_hash

vendor_bp = Blueprint("vendor", __name__)

# Vendor Registration Route
@vendor_bp.route("/register", methods=["POST"])
def register_vendor():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Check if the email already exists
    if mongo.db.vendors.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 400

    vendor = {
        "username": username,
        "email": email,
        "password": hashed_password
    }

    mongo.db.vendors.insert_one(vendor)
    return jsonify({"message": "Vendor registered successfully!"}), 201
