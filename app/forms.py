from flask.ext.wtf import Form
from wtforms import StringFiled, BooleanField
form wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
