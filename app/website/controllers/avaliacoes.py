from flask import Blueprint, Flask, render_template, request, session, url_for, flash, redirect
from forms import ResgistrationForm, LoginForm, AvaliacaoTextForm, UpdateAvaliacao
from flask_mysqldb import MySQL
from config import config
from website.models.user_dao import UserDAO, User
from website.models.turma_dao import TurmaDAO, Turma
from website.models.professor_dao import ProfessorDAO, Professor
from website.models.disciplina_dao import DisciplinaDAO, Disciplina
from website.models.avaliacao_dao import AvaliacaoDAO, Avaliacao
from website.decorators.auth import is_authenticated, admin_permission
from website import app, mysql

avaliacoes = Blueprint('avaliacoes', __name__)

@avaliacoes.route("/home")
@is_authenticated
def home():
    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TurmaView")
    turmas = cursor.fetchall()
    #print(session)
    return render_template('home.html', turmas=turmas, session=session, user_profile=user_profile)

@avaliacoes.route("/minhas-avaliacoes")
@is_authenticated
def minhas_avaliacoes():
    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])

    cursor = mysql.connection.cursor()
    cursor.callproc('GetUserAvaliacoes', [session['user_matricula']])
    avaliacoes = cursor.fetchall()

    return render_template('my_avaliacoes.html', title='Avalia', session=session, user_profile=user_profile, avaliacoes=avaliacoes)

@avaliacoes.route("/minhas-avaliacoes/<int:avaliacao_id>", methods=['GET', 'POST'])
@is_authenticated
def update_avaliacao(avaliacao_id):

    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])
    cursor = mysql.connection.cursor()
    avaliacao = AvaliacaoDAO().get_avaliacao_by_id(cursor, avaliacao_id)
    form = UpdateAvaliacao()

    if request.method == 'POST':
        new_text = request.form.get('text')

        if not new_text:
            new_text = avaliacao.avaliacao_descricao
        
        new_avaliacao = Avaliacao(avaliacao_id=avaliacao_id, avaliacao_descricao=new_text, avaliacao_turma_id=avaliacao[2], 
                                  avaliacao_user_matricula=avaliacao[3] )
        
        AvaliacaoDAO().update(cursor, new_avaliacao)
        mysql.connection.commit()

        return redirect(url_for("avaliacoes.minhas_avaliacoes", profile=False))
    
    return render_template('avaliacao_selected.html', form=form, profile=False, avaliacao=avaliacao, user_profile=user_profile)

@avaliacoes.route("/minhas-avaliacoes/<int:avaliacao_id>/delete", methods=['GET', 'POST'])
@is_authenticated
def delete_avaliacao(avaliacao_id):
   
    cursor = mysql.connection.cursor()
    AvaliacaoDAO().delete(cursor, avaliacao_id)
    mysql.connection.commit()

    flash('Avaliação Deletada Com Sucesso.', category='success')
    
    return redirect(url_for("avaliacoes.minhas_avaliacoes", profile=False))