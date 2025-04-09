from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from app.utils.db import mongo
import datetime

order_bp = Blueprint("order", __name__)

# POST: Place an order
@order_bp.route("/orders/checkout", methods=["POST"])
@jwt_required()
def place_order():
    data = request.get_json()
    customer_id = get_jwt_identity()

    cart_items = data.get("cart_items", [])
    total_amount = data.get("total_amount", 0)
    if not cart_items:
        return jsonify({"message": "Cart is empty"}), 400

    order = {
        "customer_id": customer_id,
        "items": cart_items,
        "total_amount": total_amount,
        "status": "Pending",
        "created_at": datetime.datetime.utcnow()
    }

    mongo.db.orders.insert_one(order)
    return jsonify({"message": "Order placed successfully"}), 201

# GET: Customer order history
@order_bp.route("/orders/history", methods=["GET"])
@jwt_required()
def order_history():
    customer_id = get_jwt_identity()
    orders = list(mongo.db.orders.find({"customer_id": customer_id}))
    for order in orders:
        order["_id"] = str(order["_id"])
    return jsonify({"orders": orders}), 200

# PATCH: Vendor updates order status
@order_bp.route("/orders/<order_id>/status", methods=["PATCH"])
@jwt_required()
def update_order_status(order_id):
    new_status = request.json.get("status")
    if new_status not in ["Pending", "Shipped", "Delivered"]:
        return jsonify({"message": "Invalid status"}), 400

    result = mongo.db.orders.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": new_status}}
    )

    if result.modified_count == 0:
        return jsonify({"message": "Order not found"}), 404

    return jsonify({"message": f"Order marked as {new_status}"}), 200

# (Optional) GET: Vendor sees orders containing their products
@order_bp.route("/orders/vendor/<vendor_id>", methods=["GET"])
@jwt_required()
def vendor_orders(vendor_id):
    orders = list(mongo.db.orders.find({
        "items": {"$elemMatch": {"vendor_id": vendor_id}}
    }))
    for order in orders:
        order["_id"] = str(order["_id"])
    return jsonify({"orders": orders}), 200
