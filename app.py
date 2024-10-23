from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/all-data")
def dataviz():
    connexion = sqlite3.connect("data.db")
    cursor = connexion.cursor()
    sql_request = f"""SELECT * FROM  customer ta
                        INNER JOIN customer_order tb ON ta.id = tb.customer_id
                        INNER JOIN order_detail tc ON tb.id = tc.order_id
                        INNER JOIN product td ON tc.product_id = td.id
                        LIMIT 50"""
    data = cursor.execute(sql_request).fetchall()
    column_names = [description[0] for description in cursor.description]
    connexion.close()
    
    return render_template("dataviz.html", data=data, 
                           column_names=column_names)

@app.route("/dataviz/<table>")
def table_dataviz(table):
    connexion = sqlite3.connect("data.db")
    cursor = connexion.cursor()
    sql_request = f"SELECT * FROM {table} LIMIT 50"
    data = cursor.execute(sql_request).fetchall()
    column_names = [description[0] for description in cursor.description]
    connexion.close()
    
    return render_template("table_template.html", data=data, 
                           column_names=column_names)

@app.route("/")
def hello():
    return "<div>Hello World</div>"