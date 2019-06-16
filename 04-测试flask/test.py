from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("code.html")


@app.route("/c")
def c():
    with open("./test.py", "r", encoding="UTF-8") as f:
        file_data = f.read()

    return jsonify({"data": file_data})


if __name__ == '__main__':
    app.run(debug=True)
