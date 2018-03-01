from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'wes'}
    posts = [
        {
            'author': {'username': 'Author 1'},
            'body': 'This is the post body'
        },
        {
            'author': {'username': 'Author 2'},
            'body': 'Another post'
        },
        {
            'author': {'username': 'Author 3'},
            'body': 'Yet another post'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)