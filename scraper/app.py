from flask import Flask, request, render_template
import mysql.connector
import config


db = mysql.connector.connect(
    host="aws.connect.psdb.cloud",
    user=config.USER,
    password=config.PASSWORD,
    database="products"
)
mycursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods = ["GET"])
def query():
    user_message = request.args.get('msg')
    mycursor.execute("""SELECT * FROM products1 WHERE brand='XIAOMI'""")
    query_result = mycursor
    print(query_result)

    response = ""
    for row in query_result:
        info = ""
        for val in row:
            info += str(val) + '\n'
        response += str(info) + '\n\n'
    return response

if __name__ == "__main__":
    app.run()









