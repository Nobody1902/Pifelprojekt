from flask import Flask, render_template, session, request, redirect, url_for
import translation

app = Flask("Test")

def parse_lang(req):
    l = req.headers.get("Accept-Language", "en").split(",")[0]
    return l

@app.route("/changelang")
def changelang():
    lang = request.args.get("newlang", None)
    if not lang:
        return session.get("lang", parse_lang(request))
    
    session["lang"] = lang
    return redirect(request.referrer or url_for("index"))

@app.route("/login/", methods=["GET"])
def login():
    if "username" in session:
        return redirect(url_for("index"))
    lang = session.get("lang", parse_lang(request))
    return render_template("login.jinja", t=lambda x: translation.get(x, lang))
    


@app.route("/")
def index():
    lang = session.get("lang", parse_lang(request))
    return render_template("index.jinja", t=lambda x: translation.get(x, lang))

if __name__ == "__main__":
    translation.load()
    app.run(debug=True)