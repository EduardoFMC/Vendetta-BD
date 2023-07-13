from flask import Blueprint, Flask, render_template, request, session, url_for, flash, redirect
from forms import ResgistrationForm, UpdateAvaliacao
from flask_mysqldb import MySQL
from config import config
from website.models.user_dao import UserDAO, User
from website.models.turma_dao import TurmaDAO, Turma
from website.models.professor_dao import ProfessorDAO, Professor
from website.models.disciplina_dao import DisciplinaDAO, Disciplina
from website.models.avaliacao_dao import AvaliacaoDAO, Avaliacao
from website.models.denuncia_dao import DenunciaDAO, Denuncia
from website.decorators.auth import is_authenticated
from website import app, mysql

avaliacao_selected = Blueprint('avaliacao_selected', __name__)

@avaliacao_selected.route("/avaliacao/<int:avaliacao_id>", methods=['GET', 'POST'])
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

        return redirect(url_for("turma_selected.turma", turma_id=avaliacao[2], profile=False))
    
    return render_template('avaliacao_selected.html', form=form, profile=False, avaliacao=avaliacao, user_profile=user_profile)

@avaliacao_selected.route("/avaliacao/<int:avaliacao_id>/delete", methods=['GET', 'POST'])
@is_authenticated
def delete_avaliacao(avaliacao_id):
    
    #user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])
   
    cursor = mysql.connection.cursor()
    avaliacao = AvaliacaoDAO().get_avaliacao_by_id(cursor, avaliacao_id)
    turma_id = avaliacao[2]

    AvaliacaoDAO().delete(cursor, avaliacao_id)
    mysql.connection.commit()

    flash('Avaliação Deletada Com Sucesso.', category='success')
    
    return redirect(url_for("turma_selected.turma", turma_id=turma_id, profile=False))

@avaliacao_selected.route("/avaliacao/<int:avaliacao_id>/denuncia", methods=['GET', 'POST'])
@is_authenticated
def denunciar_avaliacao(avaliacao_id):
    
    #user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])
   
    cursor = mysql.connection.cursor()
    avaliacao = AvaliacaoDAO().get_avaliacao_by_id(cursor, avaliacao_id)
    #print(avaliacao)
    turma_id = avaliacao[2]
    
    denuncia = DenunciaDAO().get_denuncia_by_avaliacao_id(cursor, avaliacao_id)
    print(denuncia)

    if denuncia :

        DenunciaDAO().update(cursor, denuncia.denuncia_id)
        mysql.connection.commit()
        
        return redirect(url_for("turma_selected.turma", turma_id=turma_id, profile=False))
    else:
        #denuncia_id, denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula

        new_denuncia = Denuncia(denuncia_id=None, denuncia_num_reports=1, denuncia_avaliacao_id=avaliacao[0], denuncia_turma_id=avaliacao[2], denuncia_denunciado_user_matricula=avaliacao[3])
        DenunciaDAO().add(cursor, new_denuncia)
        mysql.connection.commit()

        return redirect(url_for("turma_selected.turma", turma_id=turma_id, profile=False))