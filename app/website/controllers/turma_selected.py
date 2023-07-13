from flask import Blueprint, Flask, render_template, request, session, url_for, flash, redirect
from forms import ResgistrationForm, LoginForm, AvaliacaoTextForm
from flask_mysqldb import MySQL
from config import config
from website.models.user_dao import UserDAO, User
from website.models.turma_dao import TurmaDAO, Turma
from website.models.professor_dao import ProfessorDAO, Professor
from website.models.disciplina_dao import DisciplinaDAO, Disciplina
from website.models.avaliacao_dao import AvaliacaoDAO, Avaliacao
from website.decorators.auth import is_authenticated
from website import app, mysql

turma_selected = Blueprint('turma_selected', __name__)

@turma_selected.route("/turma/<int:turma_id>", methods=['GET', 'POST'])
@is_authenticated
def turma(turma_id):
    
    form = AvaliacaoTextForm()
    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TurmaView WHERE turma_id = {}".format(turma_id ))
    turma_selected = cursor.fetchone()

    avaliacoes = AvaliacaoDAO().get_all_avaliacoes_by_turma_id(cursor, turma_id)
    
    result = []
    if avaliacoes:
        
        for avaliacao in avaliacoes:
            
            avaliador = UserDAO().find_by_matricula(cursor, avaliacao[3])
            result.append((avaliador.user_name, avaliacao[1], avaliacao[3], avaliacao[0]))
   #print(result)

    session['user_matricula'] = user_profile.matricula
    
    if form.validate_on_submit():

        content = request.form.get('text')
        #print(content)

        avaliacao = Avaliacao(avaliacao_id=None, avaliacao_descricao=content, avaliacao_turma_id = turma_id, avaliacao_user_matricula=session['user_matricula'])
        AvaliacaoDAO().add(mysql.connection.cursor(), avaliacao)
        mysql.connection.commit()

        session['user_matricula'] = user_profile.matricula

        return redirect(url_for("turma_selected.turma", turma_id=turma_id, profile=False, user_profile=user_profile, result=result))
    
    #print(session['user_matricula'])
    
    return render_template('turma_selected.html', turma_selected=turma_selected, result=result, form=form, session=session, profile=False, user_profile=user_profile)