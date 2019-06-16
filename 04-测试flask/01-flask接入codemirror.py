from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("code.html")


@app.route("/c", methods=["GET", "POST"])
def c():
    if request.method == "GET":
        with open("./test.py", "r", encoding="UTF-8") as f:
            file_data = f.read()

        return jsonify({"data": file_data})

    else:
        print(request.form.get("data"))
        return "OK"


if __name__ == '__main__':
    app.run(debug=True)
