from flask import Blueprint, Flask, render_template, request, session, url_for, flash, redirect
from forms import ResgistrationForm, LoginForm, AvaliacaoTextForm
from flask_mysqldb import MySQL
from config import config
from website.models.user_dao import UserDAO, User
from website.models.turma_dao import TurmaDAO, Turma
from website.models.professor_dao import ProfessorDAO, Professor
from website.models.disciplina_dao import DisciplinaDAO, Disciplina
from website.models.avaliacao_dao import AvaliacaoDAO, Avaliacao
from website.models.denuncia_dao import DenunciaDAO, Denuncia
from website.decorators.auth import is_authenticated, admin_permission
from website import app, mysql

denuncias = Blueprint('denuncias', __name__)

@denuncias.route("/denuncias", methods=['GET', 'POST'])
@is_authenticated
@admin_permission
def admin_denuncias():
    user_profile = UserDAO().find_by_matricula(mysql.connection.cursor(), session['user_matricula'])
    
    cursor = mysql.connection.cursor()
    denuncias = DenunciaDAO().get_all_denuncias(cursor)
    
    denuncias_info = []
    for denuncia in denuncias:
        cursor.callproc('GetDenunciaInfo', [denuncia.denuncia_id])
        result = cursor.fetchone()
        denuncia_info = {
            'turma_id': result[0],
            'turma_periodo': result[1],
            'professor_nome': result[2],
            'disciplina_nome': result[3],
            'departamento_nome': result[4],
            'denuncia_denunciado_user_matricula': result[5],
            'denunciado_user_name': result[6],
            'avaliacao_descricao': result[7],
            'denuncia_num_reports': result[8],
            'denuncia_id': denuncia.denuncia_id,
            'avaliacao_id': denuncia.denuncia_avaliacao_id
        }
        denuncias_info.append(denuncia_info)
        cursor.nextset()
        
    return render_template('denuncias.html', session=session, profile=False, user_profile=user_profile, denuncias=denuncias_info)

@denuncias.route("/denuncias/<int:denuncia_id>/delete", methods=['GET', 'POST'])
@is_authenticated
@admin_permission
def delete_denuncia(denuncia_id):

    cursor = mysql.connection.cursor()
    DenunciaDAO().delete(cursor, denuncia_id)
    mysql.connection.commit()
    flash('Denúncia removida.', category='success')

    return redirect(url_for('denuncias.admin_denuncias'))

@denuncias.route("/denuncias/<int:denuncia_id>/delete/<int:avaliacao_id>", methods=['GET', 'POST'])
@is_authenticated
@admin_permission
def delete_avaliacao_by_denuncia(denuncia_id, avaliacao_id):
    print(avaliacao_id)

    cursor = mysql.connection.cursor()
    DenunciaDAO().delete(cursor, denuncia_id)
    mysql.connection.commit()

    cursor = mysql.connection.cursor()
    AvaliacaoDAO().delete(cursor, avaliacao_id)
    mysql.connection.commit()

    flash('Avaliação removida.', category='success')

    return redirect(url_for('denuncias.admin_denuncias'))