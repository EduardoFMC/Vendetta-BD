""" CREATE TABLE mydb.Avaliacao (
	avaliacao_id int NOT NULL auto_increment,
	avaliacao_descricao  varchar(500) NOT NULL,
	
    PRIMARY KEY (avaliacao_id),
    
	avaliacao_turma_id int NOT NULL,
    FOREIGN KEY (avaliacao_turma_id)
			REFERENCES Turma(turma_id),
            
	avaliacao_user_matricula int NOT NULL,
    FOREIGN KEY (avaliacao_user_matricula)
			REFERENCES User(matricula)
); """

class Avaliacao():

    def __init__(self, avaliacao_id, avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula):
        self.avaliacao_id = avaliacao_id
        self.avaliacao_descricao = avaliacao_descricao
        self.avaliacao_turma_id = avaliacao_turma_id
        self.avaliacao_user_matricula = avaliacao_user_matricula

class AvaliacaoDAO():

    def __init__(self):
        pass
    
    def get_avaliacao_by_id(self, cursor, avaliacao_id):
        cursor.execute("SELECT * FROM Avaliacao WHERE avaliacao_id = {}".format(avaliacao_id))
        avaliacao = cursor.fetchone()
        return avaliacao
    
    def get_all_avaliacoes(self, cursor):
        cursor.execute("SELECT * FROM Avaliacao")
        avaliacoes = cursor.fetchall()
        return avaliacoes
    
    def get_all_avaliacoes_by_turma_id(self, cursor, avaliacao_turma_id):
        cursor.execute("SELECT * FROM Avaliacao WHERE avaliacao_turma_id = {}".format(avaliacao_turma_id))
        avaliacoes = cursor.fetchall()
        return avaliacoes
    
    def add(self, cursor, avaliacao):
        try:
            sql_command = "INSERT INTO Avaliacao (avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) VALUES (%(avaliacao_descricao)s, %(avaliacao_turma_id)s, %(avaliacao_user_matricula)s)"
            data_insert = {"avaliacao_descricao": avaliacao.avaliacao_descricao, "avaliacao_turma_id": avaliacao.avaliacao_turma_id, "avaliacao_user_matricula": avaliacao.avaliacao_user_matricula}
            cursor.execute(sql_command, data_insert)
        except Exception as e:
            print(e)
    
    # update só na ddescrição. faz sentido dar update em tudo?
    def update(self, cursor, avaliacao):
        try:
            sql_command = "UPDATE Avaliacao SET avaliacao_descricao = %(avaliacao_descricao)s WHERE avaliacao_id = %(avaliacao_id)s"
            data_update = {"avaliacao_id": avaliacao.avaliacao_id ,"avaliacao_descricao": avaliacao.avaliacao_descricao}
            cursor.execute(sql_command, data_update)
        except Exception as e:
            print(e)
    
    def delete(self, cursor, avaliacao_id):
        try:
            sql_command = "DELETE FROM Avaliacao WHERE avaliacao_id = {}".format(avaliacao_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)