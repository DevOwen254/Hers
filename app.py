from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "echoes_of_you_secret"

USER = "myissy"
PASS = "her2301"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USER and request.form["password"] == PASS:
            session["auth"] = True
            return redirect("/intro")
        return render_template("login.html", error="Wrong access 💔")
    return render_template("login.html")


@app.route("/intro")
def intro():
    if not session.get("auth"):
        return redirect("/")
    return render_template("intro.html")


@app.route("/story")
def story():
    if not session.get("auth"):
        return redirect("/")
    return render_template("story.html")


@app.route("/secret")
def secret():
    if not session.get("auth"):
        return redirect("/")
    return render_template("secret.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)