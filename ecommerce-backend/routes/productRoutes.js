// routes/productRoutes.js
const express = require('express');
const router = express.Router();
const Product = require('../models/Product');
const verifyToken = require('../middleware/verifyToken');

router.post('/', verifyToken, async (req, res) => {
  if (req.user.role !== 'vendor') {
    return res.status(403).json({ msg: 'Access denied. You must be a vendor.' });
  }

  try {
    const { name, description, price, imageUrl } = req.body;
    const newProduct = new Product({
      name,
      description,
      price,
      imageUrl,
      vendorId: req.user.id,
    });

    await newProduct.save();
    res.status(201).json({ msg: 'Product created successfully', product: newProduct });
  } catch (err) {
    res.status(500).json({ msg: 'Server error', error: err.message });
  }
});

module.exports = router;
