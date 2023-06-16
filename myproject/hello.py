from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route("/<name>")
# def hello(name):
# # El escape escapa lo que está dentro para que no se puedan producir inyecciones de código
#     return f'Hello, {escape(name)}!'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello/coca')
def mongo():
    return 'Mongolo'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Unique URLs / Redirection Behavior