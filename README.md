# 🛒 Amazon Database Management System (MySQL Project)

## 📌 Project Overview

This project is a **relational database system** designed to simulate the backend of an e-commerce platform like Amazon. It manages core functionalities such as customers, orders, products, payments, and sellers using **MySQL**.

The goal is to demonstrate strong skills in:

* Database design
* SQL queries
* Data relationships
* Real-world business logic

---

## 🚀 Features

* 👤 Customer Management
* 📦 Product Catalog System
* 🛍️ Order Processing
* 💳 Payment Tracking
* 🏪 Seller Management
* 🔗 Proper Foreign Key Relationships
* 📊 Data Retrieval using Advanced SQL Queries

---

## 🧱 Database Schema

### 📋 Tables Included:

1. Customers
2. Products
3. Orders
4. Order_Items
5. Payments
6. Sellers
7. Categories
8. Reviews
9. Shipping
10. Inventory

---

## 🔗 Entity Relationships

* One Customer ➝ Many Orders
* One Order ➝ Many Products (via Order_Items)
* One Seller ➝ Many Products
* One Product ➝ Many Reviews
* One Order ➝ One Payment

---

## 🛠️ Technologies Used

* **Database:** MySQL
* **Language:** SQL
* **Tools:** MySQL Workbench / phpMyAdmin

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/amazon-dbms-project.git
cd amazon-dbms-project
```

### 2️⃣ Import Database

* Open MySQL Workbench
* Create a new schema:

```sql
CREATE DATABASE amazon_db;
USE amazon_db;
```

* Import the `.sql` file:

```sql
SOURCE amazon_db.sql;
```

---

## 📊 Sample Queries

### 🔍 Get All Customers

```sql
SELECT * FROM customers;
```

### 📦 View Orders with Customer Details

```sql
SELECT c.name, o.order_id, o.order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
```

### 💰 Total Sales

```sql
SELECT SUM(amount) AS total_revenue FROM payments;
```

### ⭐ Top Rated Products

```sql
SELECT product_id, AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id
ORDER BY avg_rating DESC;
```

---

## 📈 Advanced Concepts Used

* Joins (INNER, LEFT)
* Subqueries
* Aggregate Functions (SUM, AVG)
* Group By & Having
* Indexing
* Normalization (up to 3NF)

---

## 🧪 Future Improvements

* Add Stored Procedures
* Implement Triggers
* Build Frontend (React / HTML)
* Integrate with Python for Data Analysis
* Add Dashboard using Power BI

---

## 👨‍💻 Author

**Shaikh Abdul Wahab**

* 🎓 BCA Student | Data Analyst Enthusiast
* 💼 Skills: SQL, Power BI, Python

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share with others

---

## 📬 Contact

For any queries or suggestions, feel free to reach out!

---
