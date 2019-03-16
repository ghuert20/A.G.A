from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Call  of Duty Black OPS III Stats"

if __name__ == "__main__":
    app.run(debug=True, port=5633)