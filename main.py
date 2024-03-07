from flask import Flask
import sqlite3

app = Flask(__name__)

con = sqlite3.connect('cafe.db')
cur = con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS product (
#     id      NUMERIC PRIMARY KEY,
#     name    TEXT    NOT NULL,
#     price   NUMERIC NOT NULL,
#     picture TEXT
# );''')