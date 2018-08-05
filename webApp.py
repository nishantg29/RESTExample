from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Default method is bbbb %s" % request.method

@app.route("/abc", methods=["GET", "POST"])
def abc():
    if request.method == "POST":
        return " method is post"
    else:
        return " method is GET"

if __name__ == "__main__":
    app.run()
