from flask import Flask
app = Flask(__name__)  # Eta te module er naam dhorey rakha hoye

@app.route("/")  # Kon page e gele eta dekhabe
@app.route("/home")  # Kon page e gele eta dekhabe
def home():  # Etar jayegaye typically ekta HTML page return kora uchit
    return "<h1>Home page</h1>" # CAREFUL: Eta return korte hobe, not print

@app.route("/about")  # Kon page e gele eta dekhabe
def about():  # Etar jayegaye typically ekta HTML page return kora uchit
    return "<h1>About page</h1>" # CAREFUL: Eta return korte hobe, not print


"""
Er pore command line e giye:
> export FLASK_APP=flaskblog.py
> flask run

Tarpor browser e giye enter:
127.0.0.1:5000
or
localhost:5000

Change kore chalate hole web server ta arekbar chalate hobe.
Etar workaround hochhe debug mode e code ta chalano.

> export FLASK_DEBUG=1
> flask run
"""

# Baar bar jaate envt variable set na korte hoy:
if __name__ == "__main__":
    app.run(debug=True)
