from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>привет, мир!</h1><p>это мой первый сайт на python!</h1>"

@app.route("/about")
def about():
    return "<p>это страница 'О сайте'</p>"

if __name__ == "__main__":
    app.run(debug=True)






