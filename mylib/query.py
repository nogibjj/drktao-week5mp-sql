import sqlite3
from prettytable import PrettyTable

def create_db():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS GroceryDB
                      (grocery name INTEGER PRIMARY KEY
                      count_products INTEGER
                      ingred_FPro FLOAT
                      avg_FPro_products FLOAT
                      avg_distance_root FLOAT
                      ingred_normalization_term	FLOAT
                      semantic_tree_name CHAR
                      semantic_tree_node CHAR)"""
    )
    conn.commit()
    print("Table created")
    return conn

def read_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("Table read")

def update_db(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE GroceryDB SET semantic_tree_name = 'coffee' WHERE general name = 'arabica coffee'")
    conn.commit()
    print("Table updated")

def delete_tb():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(
        "DROP TABLE IF EXISTS GroceryDB"
    )
    conn.commit()
    conn.close()
    print("Table dropped")

def Query1():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB WHERE CONTAINS(general name, 'coffee')")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("rows retrieved")

def Query2():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT general name FROM GroceryDB WHERE count_products>20")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("rows retrieved")