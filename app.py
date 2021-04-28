from flask import Flask, render_template, request, send_from_directory, redirect, url_for, request
import yaml
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/cyber.html")
def cyber():
    return render_template("cyber.html")


if __name__=="__main__":
    app.secret_key = '841da66s9xdaq3'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', debug=True, port=8080)
