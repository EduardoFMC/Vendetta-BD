from flask import Flask
from flask_mysqldb import MySQL
from config import DevelopmentConfig

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave' 
app.config.from_object(DevelopmentConfig)
mysql = MySQL(app)

from website.controllers.profile import profile
from website.controllers.avaliacoes import avaliacoes
from website.controllers.turma_selected import turma_selected
from website.controllers.avaliacao_selected import avaliacao_selected
from website.controllers.denuncias import denuncias

app.register_blueprint(profile, url_prefix='/')
app.register_blueprint(avaliacoes, url_prefix='/')
app.register_blueprint(turma_selected, url_prefix='/')
app.register_blueprint(denuncias, url_prefix='/')
app.register_blueprint(avaliacao_selected, url_prefix='/')
