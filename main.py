from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Blueprint imports
from app.routes.auth import auth_bp
from app.routes.customer import customer_bp
from app.routes.vendor import vendor_bp
from app.routes.product import product_bp
from app.routes.vendor_login import vendor_login_bp
from app.routes.cart import cart_bp
from app.routes.order import order_bp
from app.routes.coupon import coupon_bp
from app.routes.check_token import check_token_bp
from app.routes.apply_coupon import apply_coupon_bp
from app.routes.reviews import reviews_bp

# MongoDB init
from app.utils.db import mongo

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ✅ CORS FIX for frontend ports (5173 & 5174)
CORS(
 app,
 origins="*",
 supports_credentials=True,
 allow_headers=["*"],
 methods=["*"]
)


# ✅ Flask Config
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET", "your-default-secret-key")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET", "your-default-secret-key")
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_HEADER_NAME"] = "Authorization"
app.config["JWT_HEADER_TYPE"] = "Bearer"

# ✅ Initialize DB and JWT
mongo.init_app(app)
jwt = JWTManager(app)

# ✅ Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(customer_bp, url_prefix="/api/customer")
app.register_blueprint(vendor_bp, url_prefix="/api/vendor")
app.register_blueprint(product_bp, url_prefix="/api/products")
app.register_blueprint(vendor_login_bp, url_prefix="/api/vendors")
app.register_blueprint(cart_bp, url_prefix="/api/cart")
app.register_blueprint(order_bp, url_prefix="/api/orders")
app.register_blueprint(coupon_bp, url_prefix="/api/coupons")
app.register_blueprint(check_token_bp, url_prefix="/api")
app.register_blueprint(apply_coupon_bp)
app.register_blueprint(reviews_bp, url_prefix="/api")

# ✅ Root Route
@app.route("/")
def home():
    return {"message": "🚀 Multi-Vendor E-Commerce Backend Running ✅"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
