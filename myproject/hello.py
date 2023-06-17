from __future__ import annotations
from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape


app = Flask(__name__)

# @app.route("/<name>")
# def hello(name):
# # El escape escapa lo que está dentro para que no se puedan producir inyecciones de código
#     return f'Hello, {escape(name)}!'

@app.route('/')
def index():
    return 'index'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# # @app.route('/login')
# # def login():
# #     return 'login'

# @app.route('/hello/DB')
# def mongo():
#     return 'Mongo'

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

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('show_user_profile', username='Dimas Abrante'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Métodos HTTP GET y POST

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     return show_the_login_form()



# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password'])
#             return log_the_user_in(request.form['username'])
#         else: 
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)