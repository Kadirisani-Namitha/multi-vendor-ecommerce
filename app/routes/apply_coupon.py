from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.db import mongo

apply_coupon_bp = Blueprint("apply_coupon", __name__)

@apply_coupon_bp.route("/api/cart/apply-coupon", methods=["POST"])
@jwt_required()
def apply_coupon():
    data = request.get_json()
    
    if not data or "coupon_code" not in data or "total_amount" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    coupon_code = data["coupon_code"]
    total_amount = data["total_amount"]

    coupon = mongo.db.coupons.find_one({"code": coupon_code})
    if not coupon:
        return jsonify({"error": "Invalid coupon code"}), 404

    if total_amount < coupon["min_amount"]:
        return jsonify({"error": "Minimum amount not met"}), 400

    discount = coupon["discount"]
    final_amount = total_amount - discount

    return jsonify({
        "success": True,
        "original_amount": total_amount,
        "discount": discount,
        "final_amount": final_amount
    }), 200
