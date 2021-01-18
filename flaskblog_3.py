# Creating a copy of flaskblog_2_templates jaate forms er kaaj gulo er moddhe dhokano jaye
from flask import Flask, render_template
from flask import url_for, redirect
from flask.helpers import flash
from flaskblog_3_forms import RegistrationForm, LoginForm  # Eta amader banano

app = Flask(__name__)
app.config['SECRET_KEY'] = '33f77ef37fc47e62e02acbe40e4988df' # import secrets;secrets.token_hex(16)


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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=my_posts, title="My Home")


@app.route("/about")
def about():
    return render_template('about.html')

# methods=["blah"] na diley "Method not allowed" bole chellabe
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.", category="success")
        # Flash message likhle hobe na, layout.html e giye bojhate hobe how to render
        return redirect(url_for('home'))  # home stands for fn name, not app.route
    return render_template('register.html', form=form, title="Register")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title="Login")


if __name__ == "__main__":
    app.run(debug=True)
