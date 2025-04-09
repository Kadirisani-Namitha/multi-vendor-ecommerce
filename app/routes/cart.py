from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.db import mongo

cart_bp = Blueprint("cart", __name__)

# 📥 Add item to cart
@cart_bp.route("/add", methods=["POST"])
@jwt_required()
def add_to_cart():
    customer_id = get_jwt_identity()
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    if not product_id:
        return jsonify({"message": "Product ID is required"}), 400

    cart = mongo.db.carts.find_one({"customer_id": customer_id})

    if cart:
        for item in cart["items"]:
            if item["product_id"] == product_id:
                item["quantity"] += quantity
                break
        else:
            cart["items"].append({"product_id": product_id, "quantity": quantity})

        mongo.db.carts.update_one(
            {"customer_id": customer_id},
            {"$set": {"items": cart["items"]}}
        )
    else:
        mongo.db.carts.insert_one({
            "customer_id": customer_id,
            "items": [{"product_id": product_id, "quantity": quantity}]
        })

    return jsonify({"message": "Product added to cart ✅"}), 201

# 📤 Get cart for logged-in customer
@cart_bp.route("/", methods=["GET"])
@jwt_required()
def get_cart():
    customer_id = get_jwt_identity()
    cart = mongo.db.carts.find_one({"customer_id": customer_id})

    if not cart:
        return jsonify({"cart": []})

    return jsonify({"cart": cart["items"]})

# ✏️ Update quantity of item in cart
@cart_bp.route("/update/<product_id>", methods=["PUT"])
@jwt_required()
def update_cart_item(product_id):
    customer_id = get_jwt_identity()
    data = request.get_json()
    new_quantity = data.get("quantity")

    if not new_quantity or new_quantity <= 0:
        return jsonify({"message": "Invalid quantity"}), 400

    result = mongo.db.carts.update_one(
        {"customer_id": customer_id, "items.product_id": product_id},
        {"$set": {"items.$.quantity": new_quantity}}
    )

    if result.modified_count == 0:
        return jsonify({"message": "Product not found in cart"}), 404

    return jsonify({"message": "Cart item quantity updated ✅"}), 200

# ❌ Remove item from cart
@cart_bp.route("/remove/<product_id>", methods=["DELETE"])
@jwt_required()
def remove_from_cart(product_id):
    customer_id = get_jwt_identity()

    result = mongo.db.carts.update_one(
        {"customer_id": customer_id},
        {"$pull": {"items": {"product_id": product_id}}}
    )

    if result.modified_count == 0:
        return jsonify({"message": "Product not found in cart"}), 404

    return jsonify({"message": "Product removed from cart ✅"}), 200
