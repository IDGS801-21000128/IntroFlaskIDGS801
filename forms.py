from wtforms import Form
from wtforms import StringField, EmailField, IntegerField

class UserForm(Form):
    nombre = StringField('nombre')
    email = EmailField('email')
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    edad= IntegerField('edad')