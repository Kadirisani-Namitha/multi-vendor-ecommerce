// config/config.js
module.exports = {
    JWT_SECRET: process.env.JWT_SECRET || 'yourSecretKeyHere',
    MONGO_URI: process.env.MONGODB_URI || 'mongodb://localhost:27017/ecommerce',
  };
  