# 🛒 Shopping Cart Web App

A simple, full-stack Shopping Cart app built with **Flask (Python)** as the backend and **HTML/CSS/JS** as the frontend.

> 🚀 My first web app project — built from scratch to sharpen my backend logic and API design skills, with a working frontend to simulate a real-world e-commerce experience.

---

## 📸 Preview

![screenshot](https://github.com/hemz19-05/Project---Shopping-Cart-Web-App/issues/1)

---

## 🧰 Tech Stack

| Layer     | Tools Used         |
|-----------|--------------------|
| Backend   | Python, Flask, REST APIs |
| Frontend  | HTML, CSS, JS |
| Testing   | Postman (for API testing) |
| Deployment  | Render (backend), Vercel (frontend) |

---

## ✅ Features

- 🔄 Add items to cart
- ❌ Remove items from cart
- 👀 View current cart contents
- 💵 Calculate total price
- 🧹 Clear the cart
- 🧪 Testable API endpoints with Postman
- 🌐 Simple and interactive frontend connected to the backend

---

## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/shopping-cart-app.git
cd shopping-cart-app

### 2. Set Up Python Environment
pip install flask flask-cors

### 3. Run Flask Backend
python app.py

### 4. Open Frontend
- Simply open index.html in your browser.
- Make sure it's connected to the Flask API

📬 API ENDPOINTS
| Method | Endpoint  | Description        |
| ------ | --------- | ------------------ |
| POST   | `/add`    | Add item to cart   |
| DELETE | `/remove` | Remove item        |
| GET    | `/view`   | View cart contents |
| GET    | `/total`  | Calculate total    |
| DELETE | `/clear`  | Clear the cart     |

Example :
POST /add
{
  "name": "Apple",
  "price": 2.5,
  "quantity": 3
}


🙌 Why I Built This
As someone transitioning into tech from a non-coding background, I built this project to:
- Practice object-oriented programming and backend logic in Python
- Learn how to build REST APIs with Flask
- Connect a frontend to a backend using basic web technologies
- Gain confidence in building full-stack mini-projects


🧠 What I Learned
- How to design and structure Flask routes
- Managing state in-memory (with Python dictionaries)
- Communicating between frontend and backend
- Testing APIs with Postman
- How to break down a real-world use case into code logic

📌 Future Improvements
- Add user login/authentication
- Store data in a real database using SQLAlchemy
- Improve frontend with React or Bootstrap
