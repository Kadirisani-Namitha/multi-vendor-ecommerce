﻿# multi-vendor-ecommerce
# 🛒 Multi-Vendor E-Commerce Platform

This is a full-stack E-Commerce platform where:
- 📦 Vendors can manage products and view orders.
- 🛍️ Customers can browse products, add to cart, apply coupons, and track orders.

---

## 🚀 Features

### 🔐 User Authentication
- JWT-based login & registration
- Two roles: **Vendor** & **Customer**

### 👨‍💼 Vendor Dashboard
- Add, Edit, Delete products (name, price, stock, images, category)
- View orders placed for their products
- Track sales and stock

### 🧍‍♀️ Customer Features
- Browse products by category
- Add to Cart, Remove from Cart, Checkout
- Apply Coupons
- Track Order History (Pending, Shipped, Delivered)

### 🧪 Dummy Payment
- Simulated payment flow (no real transactions)

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Backend:** Flask (Python) - REST APIs
- **Database:** MongoDB Atlas
- **Auth:** JWT (JSON Web Tokens)

---

## 💻 How to Run Locally

### 🔙 Backend
```bash
cd backend
pip install -r requirements.txt
python main.py

🎨 Frontend
Open frontend/index.html in your browser directly or using Live Server.

🧪 Dummy Test Users
🛍️ Customer
Username: customer1

Password: 1234

🧑‍💼 Vendor
Username: vendor1

Password: 1234


