import sqlite3


class Database:
    def __init__(self, db='DataBase.db'):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS items (id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT, name text, price real, provider text, description text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM items")
        return self.cur.fetchall()

    def insert(self, name, price, provider, description):
        self.cur.execute("INSERT INTO items VALUES (NULL, ?, ?, ?, ?)",
                         (name, price, provider, description))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM items WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, price, provider, description):
        self.cur.execute("UPDATE items SET name = ?, price = ?, provider = ?, description = ? WHERE id = ?",
                         (name, price, provider, description, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()