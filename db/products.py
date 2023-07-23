import sqlite3


class Database:
    def __init__(self, db='db/DataBase.db'):
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
        self.connection.commit()

    def get(self, id):
        self.cursor.execute("SELECT * FROM products WHERE id=?", (id,))
        return self.cursor.fetchall()[0]

    def get_all(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def insert(self, name, buypriceusd=0, sellpriceusd=0, sellpricecop=0, units=0, dept='', provider='', description='', image='', barcode=''):
        self.cursor.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (name, buypriceusd, sellpriceusd, sellpricecop, units, dept, provider, description, image, barcode))
        self.connection.commit()

    def remove(self, identifier):
        self.cursor.execute("DELETE FROM products WHERE id=?", (identifier,))
        self.connection.commit()

    def update(self, identifier, name, buypriceusd, sellpriceusd, sellpricecop, units, dept, provider, description, image, barcode): 
        self.cursor.execute(
            "UPDATE products SET name=?, buypriceusd=?, sellpriceusd=?, sellpricecop=?, units=?, dept=?, provider=?, description=?, image=?, barcode=? WHERE id = ?",
            (name, buypriceusd, sellpriceusd, sellpricecop, units, dept, provider, description, image, barcode, identifier))
        self.connection.commit()

    def search(self, query):
        query = str(query).lower()
        products = self.get_all()
        result = []
        for product in products:
            # TODO normalize accents
            if query in str(product[1]).lower() or query in str(product[7]).lower() or query in str(product[8]).lower() or query in str(product[9]).lower() or query in str(product[10]).lower(): 
                result.append(product)
        return result

    def delete(self, id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
