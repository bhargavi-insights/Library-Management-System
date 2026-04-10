<!-- Banner Image -->
<h1 align="center">📚 Library Management System</h1>

<p align="center">
A simple yet powerful <b>Library Management System</b> built using <b>Python & Streamlit</b> with JSON-based storage.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

---

## 🚀 Overview

> A data-driven system to manage books, members, and borrowing operations in a structured and efficient way.

✔ Supports book tracking  
✔ Manages members  
✔ Handles borrow & return flow  
✔ Stores data using JSON  

---

## ✨ Features

- 📖 Add new books  
- 📋 View all books  
- 👤 Add members  
- 👥 View members  
- 🔄 Borrow books  
- ✅ Return books  
- 💾 Persistent storage  

---

## 🖼️ Preview

<p align="center">
  <img width="1910" height="1033" alt="Screenshot 2026-04-10 162404" src="https://github.com/user-attachments/assets/2fc64880-bb4a-4211-b795-f84c07df2337" />
  <img width="1908" height="1035" alt="Screenshot 2026-04-10 162417" src="https://github.com/user-attachments/assets/1ea62c88-4d21-402f-80e9-56682f0803c7" />
  <img width="1912" height="1036" alt="Screenshot 2026-04-10 162445" src="https://github.com/user-attachments/assets/a0b08ad2-5802-4caf-93b6-7f414d9fe1e2" />
</p>

---

## 🛠️ Tech Stack

| Technology | Role |
|----------|------|
| 🐍 Python | Core logic |
| 🎨 Streamlit | UI |
| 📁 JSON | Database |

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
pip install streamlit
streamlit run app.py

```

## Sample Data

```
{
  "books": [
    {
      "id": "B-7M4Z9",
      "Title": "Sita: The Warrior",
      "Author": "Amish"
    }
  ]
}
```

## 🧠 Concepts Used

-OOP (Object-Oriented Programming)
-JSON File Handling
-CRUD Operations
-Streamlit UI

---


##📊 How It Works
-Each book & member has a unique ID
-Borrowing → decreases available copies
-Returning → increases available copies
-Data stored in library.json

---

##🌱 Future Improvements

-🔍 Search system
-🔐 Authentication
-📊 Dashboard
-☁️ Database integration

---

##⭐ Support

If you like this project:

-⭐ Star the repo
-🍴 Fork it
-🚀 Share it

---
