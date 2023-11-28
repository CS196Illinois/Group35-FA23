from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # Handle form submission if needed
        pass
    return render_template("home.html")

@app.route("/lessons", methods=["POST", "GET"])
def lessons():
    if request.method == "POST":
        # Handle form submission if needed
        pass
    return render_template("lessons.html")

@app.route("/practice", methods=["POST", "GET"])
def practice():
    if request.method == "POST":
        # Handle form submission if needed
        pass
    return render_template("practice.html")

@app.route("/lessonsfn", methods=["POST", "GET"])
def lessonsfn():
    if request.method == "POST":
        x = str(request.form.get("lesson_type"))
        print(x + "lessons")
    return render_template("lessons.html")

@app.route("/practicefn", methods=["POST", "GET"])
def practicefn():
    if request.method == "POST":
        x = str(request.form.get("lesson_type"))
        print(x + "practice")
    return render_template("practice.html")

if __name__ == "__main__":
    app.run()