import sqlite3  
  
con = sqlite3.connect("database.db")  
print("Database opened successfully")  
  
con.execute("create table if not exists users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, lastNme TEXT, city TEXT,country TEXT)")  
con.execute("create table saves(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")  
print("Table created successfully")  
  
con.close()  