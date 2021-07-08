from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)

#Setup DB
DATABASE = "database.db"
conn = sqlite3.connect('database.db')

c = conn.cursor()

#Create tables
c.execute('''CREATE TABLE IF NOT EXISTS Person (Firstname TEXT, Lastname TEXT, Pid PRIMARY KEY)''')
c.execute('''CREATE TABLE IF NOT EXISTS Person_Interests (Hobby NCHAR, Pid INT, FOREIGN KEY (Pid) REFERENCES Person(Pid))''')

#Gather user information || To change user you simply change the Pid value (Personal ID)
user_interests = c.execute('''SELECT * FROM Person_Interests WHERE Pid=1''').fetchall()
user_name = c.execute('''SELECT firstname FROM Person WHERE Pid=1''').fetchall()

#Set up items in the market
market_items = {'Furniture', 'Movies', 'Books', 'Gym', 'Food', 'Tailoring', 'Fishing', 'Engineering', 'Blacksmith'}

conn.commit()
conn.close()


@app.route("/")
def index():

    return  render_template("layout.html", interests=user_interests, market_items=market_items, user_name=user_name)

if __name__=="__main__":
    app.run()