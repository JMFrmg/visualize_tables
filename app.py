from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/dataviz/all-data")
def all_data_dataviz():
    """
    Route avec le merge des quatre tables.
    """
    connexion = sqlite3.connect("data.db")  # Connexion à la base de données sqlite
    cursor = connexion.cursor()  # Création de l'objet crusor pour envoyer des requêtes sql
    
    sql_request = f"""SELECT country, invoice_nb, invoice_date, quantity, description, price
                        FROM  customer ta
                        INNER JOIN customer_order tb ON ta.id = tb.customer_id
                        INNER JOIN order_detail tc ON tb.id = tc.order_id
                        INNER JOIN product td ON tc.product_id = td.id
                        LIMIT 50"""
    data = cursor.execute(sql_request).fetchall()  # Récupération des données
    column_names = [description[0] for description in cursor.description]  # Récupération des noms des colonnes
    connexion.close()
    
    return render_template("dataviz.html", data=data, 
                           column_names=column_names)

@app.route("/dataviz/detail/<table>")
def table_dataviz(table):
    """
    Route pour affiche rles données par table.
    """
    connexion = sqlite3.connect("data.db")  # Connexion à la base de données sqlite
    cursor = connexion.cursor()  # Création de l'objet crusor pour envoyer des requêtes sql
    sql_request = f"SELECT * FROM {table} LIMIT 50"
    data = cursor.execute(sql_request).fetchall()  # Récupération des données
    column_names = [description[0] for description in cursor.description]  # Récupération des noms des colonnes
    connexion.close()
    
    return render_template("dataviz.html", data=data, 
                           column_names=column_names)



@app.route("/")
def hello():
    return "<div>Hello World</div>"