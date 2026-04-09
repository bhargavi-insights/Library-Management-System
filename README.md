<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }
        h1, h2 {
            color: #38bdf8;
        }
        .card {
            background: #1e293b;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        code {
            background: #020617;
            padding: 8px;
            display: block;
            border-radius: 5px;
            overflow-x: auto;
            color: #22c55e;
        }
        ul {
            padding-left: 20px;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 5px;
            background: #38bdf8;
            color: #000;
            font-weight: bold;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            opacity: 0.7;
        }
    </style>
</head>
<body>

<div class="container">

    <h1>📚 Library Management System</h1>
    <p>
        A simple Library Management System built using <b>Python</b> and <b>Streamlit</b>, 
        with JSON-based storage. This project allows users to manage books, members, 
        and borrowing operations through an interactive UI.
    </p>

    <div>
        <span class="badge">Python</span>
        <span class="badge">Streamlit</span>
        <span class="badge">JSON</span>
    </div>

    <div class="card">
        <h2>🚀 Features</h2>
        <ul>
            <li>📖 Add new books</li>
            <li>📋 View available books</li>
            <li>👤 Add members</li>
            <li>👥 View member details</li>
            <li>🔄 Borrow books</li>
            <li>✅ Return books</li>
            <li>💾 Persistent JSON storage</li>
        </ul>
    </div>

    <div class="card">
        <h2>🛠️ Tech Stack</h2>
        <ul>
            <li>Python</li>
            <li>Streamlit</li>
            <li>JSON</li>
        </ul>
    </div>

    <div class="card">
        <h2>📂 Project Structure</h2>
        <code>
├── app.py<br>
├── library.json<br>
└── README.md
        </code>
    </div>

    <div class="card">
        <h2>⚙️ Installation & Setup</h2>
        <p><b>Clone Repository:</b></p>
        <code>git clone https://github.com/your-username/library-management-system.git</code>

        <p><b>Install Dependencies:</b></p>
        <code>pip install streamlit</code>

        <p><b>Run App:</b></p>
        <code>streamlit run app.py</code>
    </div>

    <div class="card">
        <h2>📊 How It Works</h2>
        <ul>
            <li>Data stored in <b>library.json</b></li>
            <li>Unique ID for books & members</li>
            <li>Borrow → decreases copies</li>
            <li>Return → increases copies</li>
        </ul>
    </div>

    <div class="card">
        <h2>🧾 Sample Data</h2>
        <code>
{
  "books": [
    {
      "id": "B-7M4Z9",
      "Title": "Sita: The Warrior",
      "Author": "Amish"
    }
  ]
}
        </code>
    </div>

    <div class="card">
        <h2>🧠 Key Concepts</h2>
        <ul>
            <li>OOP</li>
            <li>JSON File Handling</li>
            <li>Unique ID Generation</li>
            <li>CRUD Operations</li>
        </ul>
    </div>

    <div class="card">
        <h2>⚠️ Improvements</h2>
        <ul>
            <li>No authentication</li>
            <li>No duplicate validation</li>
            <li>UI improvements needed</li>
        </ul>
    </div>

    <div class="card">
        <h2>🌱 Future Enhancements</h2>
        <ul>
            <li>🔍 Search system</li>
            <li>📊 Analytics dashboard</li>
            <li>🔐 Login system</li>
            <li>☁️ Database integration</li>
        </ul>
    </div>

    <footer>
        ⭐ Star • 🍴 Fork • 🚀 Share
    </footer>

</div>

</body>
</html>
