""" CREATE TABLE mydb.Denuncia (
	denuncia_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (denuncia_id),
	
    denuncia_num_reports int NOT NULL,
    
    denuncia_avaliacao_id int NOT NULL,
    FOREIGN KEY (denuncia_avaliacao_id) REFERENCES Avaliacao(avaliacao_id),
    
    denuncia_turma_id int NOT NULL,
    FOREIGN KEY (denuncia_turma_id) REFERENCES Turma(turma_id),
    
    denuncia_denunciado_user_matricula int NOT NULL,
    FOREIGN KEY(denuncia_denunciado_user_matricula) REFERENCES User(matricula)
); """

class Denuncia():

    def __init__(self, denuncia_id, denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula):
        self.denuncia_id = denuncia_id
        self.denuncia_num_reports = denuncia_num_reports
        self.denuncia_avaliacao_id = denuncia_avaliacao_id
        self.denuncia_turma_id = denuncia_turma_id
        self.denuncia_denunciado_user_matricula = denuncia_denunciado_user_matricula

class DenunciaDAO():

    def __init__(self):
        pass

    def get_all_denuncias(self, cursor):
        try:
            sql_command = "SELECT * FROM Denuncia"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            denuncias = [Denuncia(*row) for row in result]
            return denuncias

        except Exception as e:
            print(e)
    
    def get_denuncia_by_id(self, cursor, denuncia_id):
        try:
            sql_command = "SELECT * FROM Denuncia WHERE denuncia_id = {}".format(denuncia_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Denuncia(*result)

        except Exception as e:
            print(e)
    
    def get_denuncia_by_avaliacao_id(self, cursor, denuncia_avaliacao_id):
        try:
            sql_command = "SELECT * FROM Denuncia WHERE denuncia_avaliacao_id = {}".format(denuncia_avaliacao_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Denuncia(*result)

        except Exception as e:
            print(e)
    
    def add(self, cursor, denuncia):
        try:
            sql_command = "INSERT INTO Denuncia (denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula) VALUES (%(denuncia_num_reports)s, %(denuncia_avaliacao_id)s, %(denuncia_turma_id)s, %(denuncia_denunciado_user_matricula)s)"
            data_insert = {"denuncia_num_reports": denuncia.denuncia_num_reports, "denuncia_avaliacao_id": denuncia.denuncia_avaliacao_id, "denuncia_turma_id": denuncia.denuncia_turma_id, "denuncia_denunciado_user_matricula": denuncia.denuncia_denunciado_user_matricula}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def update(self, cursor, denuncia_id):

        try:
            sql_command = "UPDATE Denuncia SET denuncia_num_reports = denuncia_num_reports + 1 WHERE denuncia_id = {}".format(denuncia_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)
    
    def delete(self, cursor, denuncia_id):
        try:
            sql_command = "DELETE FROM Denuncia WHERE denuncia_id = {}".format(denuncia_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)
