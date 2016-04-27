from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Mike'},
            'body': 'Boondocks is good!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Breathing is natural!'
        },
        {
            'author': {'nickname': 'James'},
            'body': 'Sleep is for the Meek!'
        },
        {
            'author': {'nickname': 'Sarah'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
