#  E-Commerce Backend

A backend e-commerce application built with Python and Flask for managing users, products, and orders.

##  Features

- User registration and authentication  
- Product creation, updating, and deletion  
- Order creation and management  
- Admin functionality and route access control

##  Tech Stack

- **Python**
- **Flask**
- **SQLAlchemy**
- **SQLite** (for development)
- **dotenv** (for environment config)

## 📁 Project Structure

e-commerce/ ├── admin_routes.py ├── app.py ├── config.py ├── customer_routes.py ├── models.py ├── toolz.py ├── user_routes.py ├── instance/ ├── migrations/ ├── venv/ ├── .env ├── .gitignore


## ⚙️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/queenrashy/e-commerce.git
   cd e-commerce

2. Create and Activate Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Create a .env File
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key

5. Set Up the Database
    flask db init
    flask db migrate
    flask db upgrade

6. Run the Application
    flask run
Visit: http://localhost:5000


Usage
Use tools like Postman to test API endpoints for:
-Users
-Products
-Orders
-Admin routes

🤝 Contributing
Feel free to fork this repo and submit a pull request for improvements or bug fixes.
6. Run the Application
