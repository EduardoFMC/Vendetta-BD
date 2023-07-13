from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from werkzeug.utils import secure_filename

class ResgistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(min=2, max=20)])
    matricula = StringField('Matrícula', validators=[DataRequired(), Length(min=9, max=9)])
    curso_aluno = StringField('Curso', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()]) 
    confirm_password = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('password')])
    profile_picture = FileField('Foto de perfil')
    submit = SubmitField('Sign Up')
#123456789
class LoginForm(FlaskForm):
    
    matricula = StringField('Matrícula', validators=[DataRequired(), Length(min=9, max=9)])
    password = PasswordField('Senha', validators=[DataRequired()]) 
    remember = BooleanField('Lembrar conta')
    submit = SubmitField('Login')

class AvaliacaoTextForm(FlaskForm):

    text = TextAreaField('Avaliação', validators=[Length(min=2, max=1000)], id="inputField")
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    username = StringField('Novo Nome de usuário', validators=[Length(min=2, max=20)])
    curso_aluno = StringField('Atualize seu curso', validators=[Length(min=2, max=20)])
    email = StringField('Novo Email', validators= [ Email()])
    password = PasswordField('Nova Senha') 
    confirm_password = PasswordField('Confirme a Senha', validators=[EqualTo('password')])
    profile_picture = FileField('Nova Foto de perfil')
    submit = SubmitField('Submit')

class UpdateAvaliacao(FlaskForm):

    text = TextAreaField('Atualize a Avaliação', validators=[Length(min=2, max=1000)], id="inputField")
    submit = SubmitField('Submit')
