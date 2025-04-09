from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

# ✅ Vendor access decorator
def vendor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if identity.get("role") != "vendor":
            return jsonify({"error": "Vendor access only"}), 403
        return fn(*args, **kwargs)
    return wrapper

# ✅ Customer access decorator
def customer_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if identity.get("role") != "customer":
            return jsonify({"error": "Customer access only"}), 403
        return fn(*args, **kwargs)
    return wrapper
