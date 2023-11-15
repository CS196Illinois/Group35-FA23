from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("lessons.html")

@app.route("/lessons", methods=["POST", "GET"])
def lessonsfn():
    if request.method == "POST":
        x = str(request.form.get("lesson_type"))
        print(x + "lessons")
    return render_template("lessons.html")

@app.route("/practice", methods=["POST", "GET"])
def practicefn():
    if request.method == "POST":
        x = str(request.form.get("lesson_type"))
        print(x + "practice")
    return render_template("practice.html")

if __name__ == "__main__":
    app.run()