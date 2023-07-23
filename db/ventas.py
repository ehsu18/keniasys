import sqlite3
from db import products


class Database:
    def __init__(self, master, db='db/DataBase.db'):
        self.app = master
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        # self.cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS
        #     products (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        #     name text,
        #     buypriceusd real,
        #     sellpriceusd real,
        #     sellpricecop real,
        #     units integer,
        #     dept text,
        #     provider text,
        #     description text,
        #     image text,
        #     barcode text)
        # """)# TODO check this
        # self.connection.commit()

    def get(self, id):
        self.cursor.execute("SELECT * FROM ventas WHERE id=?", (id,))
        return self.cursor.fetchall()[0]

    def get_all(self):
        self.cursor.execute("SELECT * FROM ventas")
        return self.cursor.fetchall()

    def insert(self, product, description, units, total, date, note):
        self.cursor.execute("INSERT INTO ventas VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                            (product, description, units, total, date, note))
        self.connection.commit()

    def update(self, identifier, product, description, units, total, date, note): 
        self.cursor.execute(
            "UPDATE ventas SET product=?, description=?, units=?, total=?, date=?, note=? WHERE id = ?",
            (product, description, units, total, date, note, identifier))
        self.connection.commit()

    def search(self, query):
        query = str(query).lower()
        result = []
        for venta in self.get_all():
            print(venta)
            # TODO normalize accents
            if venta[1] != None: description = self.app.products.get(venta[1])[1]
            else: description = venta[2]

            if query in str(description).lower() or query in str(venta[4]).lower() or query in str(venta[5]).lower() or query in str(venta[6]).lower(): 
                result.append(venta)
            
        return result

    def delete(self, id):
        self.cursor.execute("DELETE FROM ventas WHERE id = ?", (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
