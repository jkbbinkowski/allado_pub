from flask import Flask

# create app
app = Flask(__name__, instance_relative_config=True, static_url_path='/')

# configure app
app.config['TESTING'] = False
app.config['DEBUG'] = False
app.config['FLASK_ENV'] = 'production'
app.config['SECRET_KEY'] = 'y7i2ehfdpqmvvaic7232ba6ffb65568a224y7fsy7fc7wqrci7mfspqwqh7823nf'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
