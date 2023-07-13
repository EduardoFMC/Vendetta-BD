""" CREATE TABLE mydb.Turma (
	turma_id int NOT NULL AUTO_INCREMENT,
    turma_periodo varchar(150) NOT NULL,
    
    turma_prof int NOT NULL,
    FOREIGN KEY (turma_prof)
			REFERENCES Professor(professor_id),
	turma_disciplina int NOT NULL,
	FOREIGN KEY (turma_disciplina)
			REFERENCES Disciplina(disciplina_id),
	turma_dep int NOT NULL,
    FOREIGN KEY (turma_dep)
			REFERENCES Departamento(departamento_id),
	PRIMARY KEY(turma_id)
    
); """

class Turma():
    def __init__(self, turma_id, turma_periodo, turma_prof, turma_disciplina, turma_dep):
        self.turma_id = turma_id
        self.turma_periodo = turma_periodo
        self.turma_prof = turma_prof
        self.turma_disciplina = turma_disciplina
        self.turma_dep = turma_dep

class TurmaDAO():

    def __init__(self):
        pass

    def get_all_turmas(self, cursor):
        try:
            sql_command = "SELECT * FROM Turma"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            turmas = [Turma(*row) for row in result]
            return turmas

        except Exception as e:
            print(e)
    
    def get_turma_by_id(self, cursor, turma_id):
        try:
            sql_command = "SELECT * FROM Turma WHERE turma_id = {}".format(turma_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Turma(*result)

        except Exception as e:
            print(e)
    
    def add(self, cursor, turma):
        try:
            sql_command = "INSERT INTO Turma (turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES (%(turma_periodo)s, %(turma_prof)s, %(turma_disciplina)s, %(turma_dep)s)"
            data_insert = {"turma_periodo": turma.turma_periodo, "turma_prof": turma.turma_prof, "turma_disciplina": turma.turma_disciplina, "turma_dep": turma.turma_dep}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def update(self, cursor, turma):
        try:
            sql_command = "UPDATE Turma SET turma_periodo = %(turma_periodo)s, turma_prof = %(turma_prof)s, turma_disciplina = %(turma_disciplina)s, turma_dep = %(turma_dep) WHERE turma_id = %(turma_id)s"
            data_update = {"turma_periodo": turma.turma_periodo, "turma_prof": turma.turma_prof, "turma_disciplina": turma.turma_disciplina, "turma_dep": turma.turma_dep}
            cursor.execute(sql_command, data_update)
        except Exception as e:
            print(e)

    def delete(self, cursor, turma_id):
        try:
            sql_command = "DELETE FROM Turma WHERE turma_id = {}".format(turma_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)