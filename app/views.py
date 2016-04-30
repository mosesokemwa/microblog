from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


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


@app.route('/nnn')
def nnn():
    user = {'nickname': 'Mike'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    return render_template('nnn.html',
                           title='nnn',
                           user=user,
                           posts=posts)
