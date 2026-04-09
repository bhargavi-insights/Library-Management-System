import streamlit as st
import json
import random
import string
from pathlib import Path
from datetime import datetime

#  Library Class 
class Library:
    database = "library.json"
    data = {"books": [], "members": []}

    # Load or create database
    if Path(database).exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def gen_id(prefix="B"):
        return prefix + "-" + "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(5)
        )

    @classmethod
    def save_data(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

library = Library()

# Streamlit UI 
st.set_page_config(page_title="Library Management System", layout="centered")
st.title(" Library Management System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Book",
        "List Books",
        "Add Member",
        "List Members",
        "Borrow Book",
        "Return Book",
    ],
)

if menu == "Add Book":
    st.subheader(" Add Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author")
    copies = st.number_input("Total Copies", min_value=1, step=1)

    if st.button("Add Book"):
        book = {
            "id": Library.gen_id(),
            "Title": title,
            "Author": author,
            "Total_copies": copies,
            "Avalibale_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        Library.data["books"].append(book)
        Library.save_data()
        st.success("Book added successfully!")

elif menu == "List Books":
    st.subheader(" Available Books")

    if not Library.data["books"]:
        st.info("No books found")
    else:
        st.table(Library.data["books"])

elif menu == "Add Member":
    st.subheader("👤 Add Member")

    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Add Member"):
        member = {
            "id": Library.gen_id("M"),
            "Name": name,
            "Email": email,
            "borrowed": [],
        }
        Library.data["members"].append(member)
        Library.save_data()
        st.success("Member added successfully!")

elif menu == "List Members":
    st.subheader("👥 Members List")

    if not Library.data["members"]:
        st.info("No members found")
    else:
        st.table(Library.data["members"])

elif menu == "Borrow Book":
    st.subheader(" Borrow Book")

    member_ids = [m["id"] for m in Library.data["members"]]
    book_ids = [
        b["id"]
        for b in Library.data["books"]
        if b["Avalibale_copies"] > 0
    ]

    member_id = st.selectbox("Select Member ID", member_ids)
    book_id = st.selectbox("Select Book ID", book_ids)

    if st.button("Borrow"):
        member = next(m for m in Library.data["members"] if m["id"] == member_id)
        book = next(b for b in Library.data["books"] if b["id"] == book_id)

        borrow_entry = {
            "book_id": book["id"],
            "title": book["Title"],
            "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        member["borrowed"].append(borrow_entry)
        book["Avalibale_copies"] -= 1
        Library.save_data()

        st.success("Book borrowed successfully!")

elif menu == "Return Book":
    st.subheader(" Return Book")

    member_ids = [m["id"] for m in Library.data["members"]]
    member_id = st.selectbox("Select Member ID", member_ids)

    member = next(m for m in Library.data["members"] if m["id"] == member_id)

    if not member["borrowed"]:
        st.info("No borrowed books")
    else:
        book_titles = [
            f'{b["title"]} ({b["book_id"]})' for b in member["borrowed"]
        ]
        selected = st.selectbox("Select Book to Return", book_titles)

        if st.button("Return"):
            index = book_titles.index(selected)
            returned_book = member["borrowed"].pop(index)

            book = next(
                b for b in Library.data["books"]
                if b["id"] == returned_book["book_id"]
            )
            book["Avalibale_copies"] += 1
            Library.save_data()

            st.success("Book returned successfully!")
