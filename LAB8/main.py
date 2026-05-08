import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="messi1010"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS StudentDatabase")
cursor.execute("USE StudentDatabase")
cursor.execute("""
               CREATE TABLE IF NOT EXISTS Students
               (
                   ID
                   INT
                   AUTO_INCREMENT
                   PRIMARY
                   KEY,
                   Name
                   VARCHAR
               (
                   255
               ),
                   Score INT
                   )
               """)
db.commit()


def update_table(query="SELECT * FROM Students", params=None):
    for row in tree.get_children():
        tree.delete(row)

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def add_student():
    name = entry_name.get()
    score = entry_score.get()
    cursor.execute("INSERT INTO Students (Name, Score) VALUES (%s, %s)", (name, score))
    db.commit()
    update_table()


def filter_students():
    min_score = entry_filter.get()
    update_table("SELECT * FROM Students WHERE Score > %s", (min_score,))


root = tk.Tk()
root.title("Lab 9 - Student Database")

tk.Label(root, text="Student Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Student Score:").pack()
entry_score = tk.Entry(root)
entry_score.pack()

tk.Button(root, text="Insert Student", command=add_student).pack()

tk.Label(root, text="-----------------------------------").pack()

tk.Label(root, text="Fetch Students with Score Higher Than:").pack()
entry_filter = tk.Entry(root)
entry_filter.pack()

tk.Button(root, text="Filter (Fetch)", command=filter_students).pack()

tree = ttk.Treeview(root, columns=("ID", "Name", "Score"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Score", text="Score")
tree.pack()

update_table()

root.mainloop()
