import os
from flask import Flask
app = Flask(_name_)


@app.route("/")
def main():
    return "Welcome!"


@aap.route('/how are you')
def main():
    return 'I am good, how about you?'


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
