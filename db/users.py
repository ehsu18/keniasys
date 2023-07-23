import sqlite3


class Database:
    def __init__(self, db='db/DataBase.db'):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS
        users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username text, password text, type integer, nombre text, apellido text)""")  # TODO check this
        self.connection.commit()

    def check(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return self.cursor.fetchall()

    # def get(self, id):
    #     self.cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    #     return self.cursor.fetchall()

    # def get_all(self):
    #     self.cursor.execute("SELECT * FROM products")
    #     return self.cursor.fetchall()

    # def insert(self, name, price, t, provider, description):
    #     self.cursor.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?)",
    #                         (name, price, t, provider, description))
    #     self.connection.commit()

    # def remove(self, identifier):
    #     self.cursor.execute("DELETE FROM products WHERE id=?", (identifier,))
    #     self.connection.commit()

    # def update(self, identifier, name, price, t, provider, description):
    #     self.cursor.execute(
    #         "UPDATE products SET name = ?, price = ?, type = ?, provider = ?, description = ? WHERE id = ?",
    #         (name, price, t, provider, description, identifier))
    #     self.connection.commit()

    # def search(self, query):
    #     query = str(query).lower()
    #     products = self.get_all()
    #     result = []
    #     for product in products:
    #         if query == str(product[0]) or query == str(product[1]) or query == str(product[5]):
    #             result.append(product)
    #     return result

    def __del__(self):
        self.connection.close()
