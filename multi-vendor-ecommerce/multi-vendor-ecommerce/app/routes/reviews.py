from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from app.utils.db import mongo
import datetime

reviews_bp = Blueprint("reviews", __name__)

# POST: Customer adds a review
@reviews_bp.route("/reviews/<product_id>", methods=["POST"])
@jwt_required()
def add_review(product_id):
    data = request.get_json()
    rating = data.get("rating")
    comment = data.get("comment")
    customer_id = get_jwt_identity()

    if not rating or not comment:
        return jsonify({"error": "Rating and comment are required"}), 400

    review = {
        "product_id": product_id,
        "customer_id": customer_id,
        "rating": rating,
        "comment": comment,
        "created_at": datetime.datetime.utcnow()
    }

    mongo.db.reviews.insert_one(review)
    return jsonify({"message": "Review added successfully"}), 201

# GET: Fetch reviews for a product
@reviews_bp.route("/reviews/<product_id>", methods=["GET"])
def get_reviews(product_id):
    reviews = list(mongo.db.reviews.find({"product_id": product_id}))
    for review in reviews:
        review["_id"] = str(review["_id"])
        review["customer_id"] = str(review["customer_id"])
    return jsonify({"reviews": reviews}), 200
