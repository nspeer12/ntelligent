from flask import Flask, render_template, request, send_from_directory, redirect, url_for, request
import yaml
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    with open("static/yaml/resume.yaml") as f:
        resume = yaml.load(f, Loader=yaml.FullLoader)

    me_imgs = os.scandir("static/assets/img/me")

    with open("static/yaml/projects.yaml") as f:
        projects = yaml.load(f, Loader=yaml.FullLoader)

    featured_project = None
    for p in projects:
        if p["featured"] == True:
            featured_project = p
            projects.remove(p)
            featured_img = featured_project["img"]

    for p in range(len(projects)):
        if p % 2 == 0:
            projects[p]["classes"] = "project-text w-100 my-auto text-center text-lg-right"
            projects[p]["col_classes"] = "col-lg-6 order-lg-first"
        else:
            projects[p]["classes"] = "project-text w-100 my-auto text-center text-lg-left"
            projects[p]["col_classes"] = "col-lg-6"

    return render_template("index.html", **locals())


@app.route("/cyber.html")
def cyber():
    return render_template("cyber.html")


if __name__=="__main__":
    app.run(host='127.0.0.1', debug=False, port=int(os.environ.get('PORT', 8080)))
