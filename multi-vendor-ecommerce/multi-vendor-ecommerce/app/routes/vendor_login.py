from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.utils.db import mongo
from flask_jwt_extended import create_access_token
import datetime

vendor_login_bp = Blueprint("vendor_login", __name__)

@vendor_login_bp.route("/login", methods=["POST"])
def vendor_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    vendor = mongo.db.vendors.find_one({"email": email})

    if not vendor or not check_password_hash(vendor["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity={"vendor_id": str(vendor["_id"]), "role": "vendor"},
        expires_delta=datetime.timedelta(hours=24)
    )

    return jsonify({
        "token": token,
        "vendor_name": vendor.get("name")
    }), 200
