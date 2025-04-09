from flask_pymongo import PyMongo

mongo = PyMongo()

def connect_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/multivendor_db"
    mongo.init_app(app)
