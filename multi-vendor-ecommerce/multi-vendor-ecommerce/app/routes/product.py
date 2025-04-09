# In app/routes/product.py
from flask import Blueprint, jsonify

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/", methods=["GET"])
def get_products():
    # Example products data, can be fetched from MongoDB if needed
    products = [
        {
            "id": "1",
            "name": "Sneakers",
            "price": 59.99,
            "description": "Stylish and comfortable sneakers for daily wear.",
            "imageUrl": "https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "2",
            "name": "Smart Watch",
            "price": 129.99,
            "description": "Track your fitness and stay connected on the go.",
            "imageUrl": "https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "3",
            "name": "Backpack",
            "price": 49.99,
            "description": "Durable and spacious backpack for school or travel.",
            "imageUrl": "https://images.pexels.com/photos/3731256/pexels-photo-3731256.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "4",
            "name": "Headphones",
            "price": 89.99,
            "description": "Noise-cancelling headphones with rich sound quality.",
            "imageUrl": "https://images.pexels.com/photos/815494/pexels-photo-815494.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "5",
            "name": "Sunglasses",
            "price": 19.99,
            "description": "Protect your eyes in style with polarized sunglasses.",
            "imageUrl": "https://images.pexels.com/photos/701877/pexels-photo-701877.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "6",
            "name": "Jacket",
            "price": 79.99,
            "description": "Warm and stylish winter jacket for cold weather.",
            "imageUrl": "https://images.pexels.com/photos/887898/pexels-photo-887898.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "7",
            "name": "Backpack",
            "price": 49.99,
            "description": "Durable and spacious backpack for school or travel.",
            "imageUrl": "https://images.pexels.com/photos/3731256/pexels-photo-3731256.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "8",
            "name": "Backpack",
            "price": 49.99,
            "description": "Durable and spacious backpack for school or travel.",
            "imageUrl": "https://images.pexels.com/photos/3731256/pexels-photo-3731256.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "9",
            "name": "Smart Watch",
            "price": 129.99,
            "description": "Track your fitness and stay connected on the go.",
            "imageUrl": "https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "10",
            "name": "Smart Watch",
            "price": 129.99,
            "description": "Track your fitness and stay connected on the go.",
            "imageUrl": "https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "11",
            "name": "Smart Watch",
            "price": 129.99,
            "description": "Track your fitness and stay connected on the go.",
            "imageUrl": "https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "id": "12",
            "name": "Smart Watch",
            "price": 129.99,
            "description": "Track your fitness and stay connected on the go.",
            "imageUrl": "https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
    ]
    return jsonify({"products": products})
