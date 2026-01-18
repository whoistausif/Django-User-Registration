# 🧑‍💻 Django User Registration System

A simple and secure Django-based user registration and authentication system, designed for easy learning and scalable web applications.

🔗 **GitHub Repository:**  
https://github.com/whoistausif/Django-User-Registration

---

## 📌 Features

- User Registration (Signup)
- User Login & Logout
- Secure Password Hashing
- Django Built-in Authentication System
- Form Validation
- Clean & Beginner-Friendly Structure
- Easy to Extend and Customize

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (Django Templates)  
- **Database:** SQLite  
- **Authentication:** Django Auth Framework  

---
```
Django-User-Registration/
│
├── manage.py
├── db.sqlite3
├── project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── users/
│ ├── migrations/
│ ├── templates/
│ ├── forms.py
│ ├── views.py
│ ├── models.py
│ └── urls.py
│
└── README.md

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/whoistausif/Django-User-Registration.git
cd Django-User-Registration
```
### 2️⃣ Create Virtual Environment
```
python -m venv venv
```

## Activate it:

### Windows
```
venv\Scripts\activate
```

### Linux / macOS
```
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```
pip install django
```
### 4️⃣ Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Run Development Server
```
python manage.py runserver
```

## Visit in browser:
```
http://127.0.0.1:8000/
```
### 🔐 Authentication Workflow

- User registers via signup form
- Passwords are securely hashed
- User logs in with credentials
- Session-based authentication handled by Django

### 🚀 Future Improvements

- Email Verification
- Password Reset via Email
- User Profile Management
- Role-Based Access Control
- Bootstrap / Tailwind UI
- REST API Support (DRF)

### 🤝 Contributing

- Contributions are welcome!
- Fork the repository
- Create a new branch
- Commit your changes
- Submit a Pull Request

### 📄 License

This project is licensed under the MIT License.

👨‍💻 Author
```
Mohd Tausif
GitHub: https://github.com/whoistausif
```
### ⭐ If you find this project useful, please give it a star!

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Django-4.x-success?logo=django"/>
  <img src="https://img.shields.io/github/license/whoistausif/Django-User-Registration"/>
  <img src="https://img.shields.io/github/stars/whoistausif/Django-User-Registration?style=social"/>
  <img src="https://img.shields.io/github/forks/whoistausif/Django-User-Registration?style=social"/>
</p>

Just say 👍

---
