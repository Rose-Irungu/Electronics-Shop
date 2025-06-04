 🛍️ Electronics Shop - Product Listing App

 📌 Project Purpose

This Django-based web application allows users to manage an inventory of electronics products. It supports creating, viewing, editing, and deleting products. The app is designed as a simple inventory interface for demonstration and learning purposes, showcasing CRUD operations and basic web development with Django.

 🧱 Tech Stack Used

- **Backend:** Django (Python Web Framework)
- **Frontend:** HTML, CSS (Bootstrap for styling)
- **Database:** SQLite (default Django database)
- **Media:** ImageField for product images

 ✅ Features

- Add new electronic products using a form
- View products displayed as cards on the home page
- Edit existing product details
- Delete products from the database
- About page with details about the shop
- Clean black & white themed UI for a modern appearance

Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rose-Irungu/Electronics-Shop.git
   cd electronics]
2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate]

3. Install dependencies
    pip install -r requirements.txt
4.  Run migrations
    python manage.py makemigrations
    Python manage.py migrate
5. Run the development server
    python manage.py runserver

 6. Access the app
      Visit http://127.0.0.1:8000 in your browser.
    

🗂️ Folder Structure
    D]JANGOPROJECT1
│
├── electronics/             # App for managing products
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── product.html
│   │   └── edit_product.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── DJANGOPROJECT1/        # Django project config
│   ├── settings.py
│   ├── urls.py
│
├── media/                   # Uploaded images
├── db.sqlite3               # SQLite database
├── manage.py
└── README.md
    
 👨‍💻 Author
Rose Irungu   
"Improved documentation." 
