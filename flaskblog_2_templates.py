from flask import Flask, render_template
from flask import url_for  # Eta URL resolve korte kaaje ashe, in Jinja
app = Flask(__name__)

# Creating a dummy dataset jeta ideally DB theke aana uchit
my_posts = [
    {
        "title": "My first post",
        "author": "@suryashekharc",
        "date_posted": "2020-01-03",
        "content": "Aar ki khobor dada ra, didi ra?"
    },
    {
        "title": "My second post",
        "author": "@suryashekharc",
        "date_posted": "2020-01-04",
        "content": "Shobai bhalo achhen toh? Baah khub bhalo."
    }
]

@app.route("/home_slow")
def home_slow():
    """
    Ei bhabe HTML page return kora ta slow karon prottek baar code er
    moddhe HTML er lomba code likhte hobe. Ei jonno amra Template use kori.
    "Template" bole ekta folder create kore tate amra HTML gulo dhokabo.
    """
    return """
    <!doctype html>
    <html>
        <h1>Home page</h1>
    </html>
    """

# Improvement: Use a template!
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=my_posts, title="My Home")
    # ja khushi variable ebhabe pathano jaye. "posts" ei khetre keyword noy.

# Duto function er same name thake ei error ta hoy:
# AssertionError: View function mapping is overwriting an existing endpoint function
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
