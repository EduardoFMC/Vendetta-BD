""" CREATE TABLE mydb.Disciplina(
	disciplina_id int NOT NULL AUTO_INCREMENT,
    disciplina_nome varchar(150) NOT NULL,
	PRIMARY KEY (disciplina_id),
    disciplina_dep int NOT NULL,
	FOREIGN KEY (disciplina_dep)
			REFERENCES Departamento(departamento_id)
); """

class Disciplina():
    def __init__(self, disciplina_id, disciplina_nome, disciplina_dep):
        self.disciplina_id = disciplina_id
        self.disciplina_nome = disciplina_nome
        self.disciplina_dep = disciplina_dep
        

class DisciplinaDAO():

    def __init__(self):
        pass

    def get_all_disciplinas(self, cursor):
        try:
            sql_command = "SELECT * FROM Disciplina"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            disciplinas = [Disciplina(*row) for row in result]
            return disciplinas

        except Exception as e:
            print(e)
    
    def get_disciplina_by_id(self, cursor, disciplina_id):
        try:
            sql_command = "SELECT * FROM Disciplina WHERE disciplina_id = {}".format(disciplina_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Disciplina(*result)

        except Exception as e:
            print(e)
    
    def add(self, cursor, disciplina):
        try:
            sql_command = "INSERT INTO Disciplina (disciplina_nome, disciplina_dep) VALUES (%(disciplina_nome)s, %(disciplina_dep)s)"
            data_insert = {"disciplina_nome": disciplina.disciplina_nome, "disciplina_dep": disciplina.disciplina_dep}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def update(self, cursor, disciplina):
        try:
            sql_command = "UPDATE Disciplina SET disciplina_nome = %(disciplina_nome)s, disciplina_dep = %(disciplina_dep)s WHERE disciplina_id = %(disciplina_id)s"
            data_update = {"disciplina_nome": disciplina.disciplina_nome, "disciplina_dep": disciplina.disciplina_dep}
            cursor.execute(sql_command, data_update)
        except Exception as e:
            print(e)
    
    def delete(self, cursor, disciplina_id):
        try:
            sql_command = "DELETE FROM Disciplina WHERE disciplina_id = {}".format(disciplina_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)