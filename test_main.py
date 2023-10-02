import unittest
import sqlite3
from mylib.query import Query1, Query2, Query3


class testFDBFunctions(unittest.TestCase):
    def setUp(self):
        print("Setting up for the test")
        self.conn = sqlite3.connect("GroceryDB_test.db")
        self.conn.close()

    def clean(self):
        """Clean up the test database after tests"""
        self.conn = sqlite3.connect("GroceryDB_test.db")
        self.conn.close()

    def test_Query1(self):
        result = Query1()
        self.assertEqual(result, "Success", "Failed to fetch the top 5 rows")

    def test_Query2(self):
        result = Query2()
        self.assertEqual(
            result,
            "Update success",
            "Failed to update count_products of arabica coffee",
        )

    def test_Query3(self):
        result = Query3()
        self.assertEqual(
            result,
            "Delete success",
            "Failed to delete the row containing arabica coffee",
        )


if __name__ == "__main__":
    unittest.main()