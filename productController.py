from endpoints import Controller, CorsMixin
import sqlite3
from datetime import datetime

conn = sqlite3.connect('CIUK.db')
cur = conn.cursor()

class Default(Controller, CorsMixin):
  def GET(self):
    return "CIUK"

  def POST(self, **kwargs):
    return '{}, {}, {}'.format(kwargs['title'], kwargs['desc'], kwargs['price'])

class Products(Controller, CorsMixin):
  def GET(self):
    cur.execute("select * from products")
    return cur.fetchall()

class Product(Controller, CorsMixin):
  def GET(self, id):
    cur.execute("select * from products where id=?", (id,))
    return cur.fetchone()

  def POST(self, **kwargs):
    row =[kwargs['title'], kwargs['desc'], kwargs['price'], datetime.now(), datetime.now()]
    cur.execute("insert into products values (null, ?, ?, ?, ?, ?);", (row))
    conn.commit()
    return "New product added!"

  def PUT(self, id, **kwargs):
    row =[kwargs['title'], kwargs['desc'], kwargs['price'], datetime.now(), id]
    cur.execute("update products set title=?, description=?, price=?, created_at=? where id=?", (row))
    conn.commit()
    return "Product updated!"

  def DELETE(self, id):
    cur.execute("delete from products where id=?", (id,))
    conn.commit()
    return "Product deleted!"
