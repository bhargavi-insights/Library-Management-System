import json
import random 
import string 
from pathlib import Path
from datetime import datetime


class Library:
    database="library.json"
    data={"books":[],"members":[]}

    #load existing data in json orcreate your json
    
    if Path(database).exists():
        with open(database,'r') as f:
            content= f.read().strip()
            if content:
                data=json.loads(content)
    else:
        with open(database,'w') as f:
            json.dump(data,f,indent=4)
    
    @staticmethod
    def gen_id(Prefix="B"):
        random_id="" 
        for i in range(5):
            random_id+= random.choice(string.ascii_uppercase+string.digits)
        return Prefix + "-" + random_id
        
    #save data of books and members
    @classmethod   
    def save_data(cls):
        with open(cls.database,'w') as f:
            json.dump(cls.data,f,indent=4,default=str)

    def add_book(self):
        title=input("Enter the title of the book:")
        author= input("enter the author of the book:")
        copies=int(input("enter the total copies of the books:"))

        book={
            "id":Library.gen_id() ,
            "Title":title,
            "Author":author,
            "Total_copies":copies,
            "Avalibale_copies":copies,
            "added_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        Library.data['books'].append(book)
        Library.save_data()

    def list_books(self):
        if not Library.data['books']:
            print("sorry no books found")
            return
        for b in Library.data['books']:
            print(f"{b['id']:12} {b['Title'][:24]:25} {b['Author'][:19]:20} {b['Total_copies']}/{b['Avalibale_copies']:>3}")
        
        print()

    def add_members(self):
        name=input("Entyer your name:")
        email=input("please enter your email:")

        member={
            "id": Library.gen_id("M")    ,
            "Name":name,
            "Email":email,
            "borrowed":[]
        }
        
        Library.data['members'].append(member)
        Library.save_data()
        print("Member added successfully!")

    def list_members(self):
        if not Library.data['members']:
            print("sorry no members found")
            return
        for m in Library.data['members']:
            print(f"{m['id']:12} {m['Name'][:24]:25} {m['Email'][:29]:30}")
            print("this guy has currently")
            print(f"{m['borrowed']}")
        print()  

    def borrowed_books(self): #select
            member_id=input("Enter the your id:").strip()
            members=[m for m in Library.data['members']if m['id']==member_id]
            if not members:
                print("no such id exist")
                return
            member=members[0]

            book_id=input("Enter the book id:")
            books=[b for b in Library.data['books']if b['id']==book_id]
            if not books:
                print("no book id found")
                return
            book=books[0]

            #avaliablecount
            if book['Avalibale_copies']<=0:
                print("sorry no books exist")

            borrow_entry={
                "book_id":book['id'],
                "title":book['Title'],
                "borrow_on":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }    

            member['borrowed'].append(borrow_entry)
            book['Avalibale_copies']-=1
            Library.save_data()
        
    def return_books(self):
        member_id=input("Enter the your id:").strip()
        members=[m for m in Library.data['members']if m['id']==member_id]
        if not members:    
            print("no such id exist")
            return
        
        member=members[0]

        if not member['borrowed']:
            print("no borrowed books")
            return
        
        print("borrowed books")
        for i,b in enumerate(member['borrowed'],start=1):
            print(f"{i}.{b['title']} ({b["book_id"]})")
            
        try:
            choice=int(input("enter the nnumber to return:-"))
            selected=member['borrowed'].pop(choice-1)
        except Exception as err:
            print("invalid value")

        books=[bk for bk in Library.data['books']if bk['id']==selected['book_id']]    
        if books:
            books[0]['Avalibale_copies']+=1
        Library.save_data()     
       
hello=Library()

while True:
 print("="*50)
 print("library Management system")
 print("="*50)
 print("1. Add the books")
 print("2. Lists books")
 print("3. Add members")
 print("4. List members")
 print("5. Borrow books")
 print("6. Return the books")
 print("7. Exist the portal")
 print("-"*50)
 choice=input("enter your choice:")

 if choice=="1":
     hello.add_book()

 if choice=="2":
     hello.list_books()    

 if choice=="3":    
     hello.add_members()

 if choice=="4":
     hello.list_members()

 if choice=="5":
     hello.borrowed_books()

 if choice=="6":
     hello.return_books()    

 if choice=="0":
     exit(0)    