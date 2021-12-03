import pymysql
import collections

class dbConnection:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="localhost", user="root", password="hello", db="books_data")
        except Exception as e:
            print(e)

    def insert(self, data):
        sql = """INSERT INTO book(name, isbn, authors, country, number_of_pages, publisher, release_date) VALUES 
                 ('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(data.get("name"), data.get("isbn"), 
                 ",".join(data.get("authors")), data.get("country"), data.get("number_of_pages"), data.get("publisher"), 
                 data.get("release_date"))
        print(sql)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            return "success"
        except Exception as e:
            print(e)
            return e
        
    def select(self, book_id=None):
        sql = "SELECT * FROM book"
        if book_id:
            sql = "SELECT * FROM book WHERE id = {}".format(book_id)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            headers = list(map(lambda x: x[0], cur.description))
            data = []
            for value in cur.fetchall():
                book_dict = collections.OrderedDict(zip(headers, value))
                book_dict['authors'] = book_dict['authors'].split(",")
                data.append(book_dict)
            if book_id and data:
                return data[0]
            return data
        except Exception as e:
            print(e)

    def update(self, data, book_id):
        temp = ", ".join(["{} = '{}'".format(key, data[key]) for key in data ])
        sql = """UPDATE book SET {} WHERE id = {}""".format(temp, book_id)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            return "success"
        except Exception as e:
            print(e)
            return e

    def delete(self, book_id):
        sql = "DELETE FROM book WHERE id = {}".format(book_id)
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            return "success"
        except Exception as e:
            print(e)
            return e        

    def db_close(self):
        self.conn.close()
