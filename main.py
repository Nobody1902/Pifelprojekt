from flask import Flask, render_template, session, request, redirect, url_for
import translation
import os

app = Flask("Pifelprojekt")
app.secret_key = os.environ.get("SECRET_KEY")

DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "en")


@app.route("/changelang")
def changelang():
    lang = request.args.get("newlang", None)
    if not lang:
        return session.get("lang", DEFAULT_LANG)

    session["lang"] = lang
    return redirect(request.referrer or url_for("index"))


@app.route("/login/", methods=["GET"])
def login():
    if "username" in session:
        return redirect(url_for("index"))
    lang = session.get("lang", DEFAULT_LANG)
    return render_template(
        "login.jinja", LANG=lang, t=lambda x: translation.get(x, lang)
    )


@app.route("/login/", methods=["POST"])
def login_action():
    if "username" in session:
        return redirect(url_for("index"))

    username = request.form.get("username", None)
    password = request.form.get("password", None)

    if not username or not password:
        # TODO: Show error
        return redirect(url_for("login"))

    # TODO: Implement a login system
    print(username, password)

    return redirect(url_for("index"))


@app.route("/")
def index():
    lang = session.get("lang", DEFAULT_LANG)
    return render_template(
        "index.jinja", LANG=lang, t=lambda x: translation.get(x, lang)
    )


if __name__ == "__main__":
    translation.load()
    app.run(debug=True)
