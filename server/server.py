from flask import Flask, render_template, jsonify
import dao

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/getTasks")
def getTasks():
    return jsonify(dao.main())

if __name__ == "__main__":
    app.run()   