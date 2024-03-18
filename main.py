from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

con = sqlite3.connect('cafe.db')
cur = con.cursor()

if __name__ == '__main__':
    app.run()