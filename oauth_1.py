import os
from flask import Flask
from flask import url_for, render_template, redirect, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key=os.environ.get("FLASK_APP_SECRET")  # random hex saved in bash_profile
oauth = OAuth(app)


# client_id aar secret pete https://console.cloud.google.com/apis/credentials
goog = oauth.register(
    name="google",
    client_id=os.environ.get("GOOG_CLIENT_ID"),
    client_secret=os.environ.get("GOOG_CLIENT_SECRET"),
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    api_base_url="https://www.googleapis.com/oauth2/v1",
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

@app.route("/")  # initial home screen
def hello_world():
    email = dict(session).get("email", None)
    return f"Welcome here, {email}"


@app.route('/login')
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    # porer line e token ta na specify korleo scope theke dhore nite pare
    resp = google.get('userinfo', token=token)  # probably ekhane jhamela hochhe
    user_info = resp.json()
    session['email'] = user_info['email']
    # do something with the token and profile
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)