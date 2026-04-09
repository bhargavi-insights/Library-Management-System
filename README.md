<h1>📚 Library Management System<h1>

A simple Library Management System built using Python and Streamlit, with JSON-based storage. This project allows users to manage books, members, and borrowing operations through an interactive UI.

🚀 Features
📖 Add new books to the library
📋 View list of available books
👤 Add library members
👥 View member details
🔄 Borrow books
✅ Return books
💾 Persistent storage using JSON file

🛠️ Tech Stack
Python
Streamlit
JSON (for database storage)

📂 Project Structure
├── app.py                # Main Streamlit application
├── library.json         # Database file (auto-created)
└── README.md            # Project documentation
⚙️ Installation & Setup

Clone the repository:
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

Install dependencies:
pip install streamlit

Run the app:
streamlit run app.py

📊 How It Works
The system stores all data in a JSON file (library.json)
Each book and member has a unique ID generated automatically
Borrowing a book:
Decreases available copies
Adds entry to member’s borrowed list
Returning a book:
Increases available copies
Removes entry from member’s borrowed list
🧾 Sample Data

Example structure of stored data:

{
  "books": [
    {
      "id": "B-7M4Z9",
      "Title": "Sita: The Warrior",
      "Author": "Amish",
      "Total_copies": 15,
      "Avalibale_copies": 14
    }
  ],
  "members": [
    {
      "id": "M-S5LOO",
      "Name": "Avi Joshi",
      "borrowed": [
        {
          "book_id": "B-7M4Z9",
          "title": "Sita: The Warrior"
        }
      ]
    }
  ]
}

🧠 Key Concepts Used
Object-Oriented Programming (OOP)
File handling (JSON)
Unique ID generation
State management in Streamlit

⚠️ Known Issues / Improvements
No validation for duplicate books or members
No authentication system
UI can be improved with better styling
Search & filter features can be added

🌱 Future Enhancements
🔍 Search books by title/author
📊 Dashboard with analytics
🔐 Login system (Admin/User roles)
☁️ Database integration (MongoDB / MySQL)
📱 Better UI/UX design

🙌 Acknowledgment

This project is a great beginner-friendly implementation of a CRUD-based system using Python and Streamlit.

📎 Additional Version (CLI)

This repository also includes a Command-Line Interface (CLI) version of the system:


⭐ Show Your Support

If you like this project:

⭐ Star the repo
🍴 Fork it
📢 Share it
