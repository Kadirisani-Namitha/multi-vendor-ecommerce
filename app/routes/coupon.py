# app/routes/coupon.py

from flask import Blueprint, jsonify, request
from app.utils.db import mongo

coupon_bp = Blueprint("coupon", __name__)

@coupon_bp.route("/api/coupons", methods=["GET"])
def get_all_coupons():
    coupons = list(mongo.db.coupons.find({}, {"_id": 0}))
    return jsonify(coupons), 200
