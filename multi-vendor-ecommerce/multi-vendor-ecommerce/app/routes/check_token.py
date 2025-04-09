from flask import Blueprint, jsonify, request
import jwt
import os

check_token_bp = Blueprint("check_token", __name__)

@check_token_bp.route("/check-token", methods=["GET"])
def check_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"valid": False, "error": "Missing token"}), 401

    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        return jsonify({"valid": True, "decoded": decoded})
    except jwt.ExpiredSignatureError:
        return jsonify({"valid": False, "error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"valid": False, "error": "Invalid token"}), 401
