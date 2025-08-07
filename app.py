from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, test to google cloud!"

if __name__ == "__main__":
    app.run(debug=True)
