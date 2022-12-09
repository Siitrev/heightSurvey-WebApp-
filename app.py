from flask import Flask, render_template, request
import sqlalchemy


app = Flask(__name__)

class Data(sqlalchemy)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(request.form)
        return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
