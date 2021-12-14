import os
from flask import Flask, render_template
# What we can do to get around this, is to import 
# the render_template() function from Flask.


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    # Then, instead of returning text, I'm going to return render_template("index.html").

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)