import sqlite3
from prettytable import PrettyTable

def Query1():
    '''Query the top 5 rows of the GroceryDB table'''
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5 OFFSET 1")

    column_names = [description[0] for description in cursor.description]

    table = PrettyTable(column_names) # initialize table with column names

    for row in cursor.fetchall():
        table.add_row(row) # fetch rows and add them to the table

    print(table)

    conn.close()

    return "Success"

def Query2():
    '''Update count_products of Arabica Coffee in GroceryDB table'''
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()

    # new count_products value
    new_count_products = 100
    item_name = "arabica coffee"

    cursor.execute("UPDATE GroceryDB SET count_products = ? WHERE general_name = ?", (new_count_products, item_name))
    conn.commit()
    conn.close()

    Query1()
    
    return "Update success"

def Query3():
    '''Delete the row containing arabica coffee from GroceryDB table'''
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()

    # define the item_name to delete
    item_name = "arabica coffee"

    cursor.execute("DELETE FROM GroceryDB WHERE general_name = ?", (item_name, ))
    conn.commit()

    Query1()

    return "Delete success"