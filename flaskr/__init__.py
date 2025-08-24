from flask import Flask

# create app
app = Flask(__name__, instance_relative_config=True, static_url_path='/')

# configure app
app.config['TESTING'] = False
app.config['DEBUG'] = False
app.config['FLASK_ENV'] = 'production'
