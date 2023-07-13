from flask import Blueprint, Flask, Response, render_template, request, session, url_for, flash, redirect
from forms import ResgistrationForm, LoginForm, UpdateProfile
from flask_mysqldb import MySQL
from config import config
from werkzeug.utils import secure_filename
from website.models.user_dao import UserDAO, User
from website.models.image_dao import ImageDAO, Image
from website.decorators.auth import is_authenticated
from website import app, mysql

profile = Blueprint('profile', __name__)

@profile.route("/")
@profile.route("/login", methods=['GET', 'POST'])
def login():
    
    [print(key) for key in list(session.keys())]
    
    form = LoginForm()
    if form.validate_on_submit():

        cursor = mysql.connection.cursor()
        
        matricula = request.form.get('matricula')
        password = request.form.get('password')
        print(matricula, password)
        
        user = UserDAO().find_by_matricula(cursor, matricula)
        print(user)
        if user:
            if user.password == password:
                # TODO login para HOme - mudar
                session['user_matricula'] = user.matricula
                session['user_email'] = user.user_email
                session['user_permission'] = user.is_admin
                print(session)

                flash(f'Bem-vindo!', 'success')
                return redirect(url_for('avaliacoes.home'))
            else:
                flash('Login não realizado. Por favor, verifique matrícula e senha', 'danger')
                
        else:
            flash('Conta não existe.', category='error')
            
        
    return render_template('login.html', title='Login', form=form, profile=False, login_register = True, session=session)

@profile.route('/logout',  methods=['GET', 'POST'])
@is_authenticated
def logout():
    [session.pop(key) for key in list(session.keys())]
    flash('Desconectou-se.', category='success')
    return redirect(url_for('profile.login'))

@profile.route("/register", methods=['GET', 'POST'])
def register():
         
    form = ResgistrationForm()
    if request.method == 'POST':
        
        cursor = mysql.connection.cursor()

        username = request.form.get('username')
        matricula = int(request.form.get('matricula'))

        user_check_matricula = UserDAO().find_by_matricula(cursor, matricula)
        if user_check_matricula:
            flash('Matrícula já cadastrada.', category='error')
            return redirect(url_for('profile.register'))

        curso_aluno = request.form.get('curso_aluno')
        email = request.form.get('email')
        password = request.form.get('password')

        profile_picture = request.files.get('profile_picture')
            

        if profile_picture:
            filename = secure_filename(profile_picture.filename)
            
            # coisa chata, The mônio, bora
            image = Image(image_id=None, data=profile_picture.read(), mime_type = (profile_picture.mimetype), file_name=filename, created_at=None)
            ImageDAO().add(cursor, image)
            mysql.connection.commit()
            profile_picture = cursor.lastrowid
        else:
            profile_picture = 1

        # Criação de Admin deve ser feita pelo banco
        new_user = User(matricula=matricula, user_email=email, password=password, user_name=username, curso_aluno=curso_aluno, profile_picture=profile_picture, 
                        is_admin=False, creation_date=None)
        
        UserDAO().add(cursor, new_user)
        mysql.connection.commit()

        # cookie para autenticação em cada página
        session['user_matricula'] = new_user.matricula
        session['user_email'] = new_user.user_email
        session['user_permission'] = new_user.is_admin

        flash(f'Conta criada para {form.username.data}!', 'success')
        return redirect(url_for('avaliacoes.home'))
    
    return render_template('register.html', title='Register', form=form, login_register = True, profile=False, session=session)

@profile.route('/image/<int:imade_id>')
def get_image(imade_id):
    cursor = mysql.connection.cursor()
    image = ImageDAO().find_by_id(cursor, imade_id)

    return Response(image.data, mimetype=image.mime_type)

@profile.route('/profile/<int:matricula>', methods=['GET', 'POST', 'DELETE'])
@is_authenticated
def get_profile(matricula):
    cursor = mysql.connection.cursor()
    form = UpdateProfile()
    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), matricula)
    
    """ print(type(session['user_matricula']), int(matricula))
    print(session['user_matricula'] == matricula) """
    if request.method == 'POST':
        
        new_name = request.form.get('username')
        #print(new_name)
        new_email = request.form.get('email')
        new_curso = request.form.get('curso_aluno')
        new_password = request.form.get('password')
        new_profile_picture = request.files.get('profile_picture')

        #print(new_profile_picture)

        if new_profile_picture:
            filename = secure_filename(new_profile_picture.filename)
            
            # coisa chata, The mônio, bora
            image = Image(image_id=None, data=new_profile_picture.read(), mime_type = (new_profile_picture.mimetype), file_name=filename, created_at=None)
            ImageDAO().add(cursor, image)
            mysql.connection.commit()
            new_profile_picture = cursor.lastrowid

        else:
            new_profile_picture = user_profile.profile_picture

        if not new_name:
            new_name = user_profile.user_name
        if not new_email:
            new_email = user_profile.user_email
        if not new_curso:
            new_curso = user_profile.curso_aluno
        if not new_password:
            new_password = user_profile.password
        
        updated_user = User(matricula=user_profile.matricula, user_email=new_email, password=new_password, 
                            user_name=new_name, creation_date=user_profile.creation_date, curso_aluno=new_curso, 
                            is_admin=False, profile_picture=new_profile_picture)
        
        print(updated_user.matricula)
        UserDAO().update(cursor, updated_user)
        mysql.connection.commit()
        
        flash('Atualizado Com Sucesso.', category='success')
        return redirect(url_for('profile.get_profile', matricula=updated_user.matricula))
    
            
    return render_template('profile.html', title='Profile', profile=True, session=session, form=form, user_profile=user_profile)

@profile.route('/profile/<int:matricula>/delete', methods=['GET', 'POST', 'DELETE'])
@is_authenticated
def delete_profile(matricula):
    cursor = mysql.connection.cursor()
    
    UserDAO().delete(cursor, matricula)
    mysql.connection.commit()

    if session['user_permission']:
        flash('Conta Deletada Com Sucesso.', category='success')
        return redirect(url_for('denuncias.admin_denuncias'))

    else:
        [session.pop(key) for key in list(session.keys())]

        flash('Conta Deletada Com Sucesso.', category='success')
        return redirect(url_for('profile.login'))