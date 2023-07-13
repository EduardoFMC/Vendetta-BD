""" CREATE TABLE mydb.Professor (
	professor_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (professor_id),
    professor_name varchar(150) NOT NULL,
    professor_dep int NOT NULL,
    FOREIGN KEY (professor_dep)
			REFERENCES Departamento(departamento_id)
); """

class Professor():
    def __init__(self, professor_id, professor_name, professor_dep):
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.professor_dep = professor_dep

class ProfessorDAO():

    def __init__(self):
        pass

    def get_all_professores(self, cursor):
        try:
            sql_command = "SELECT * FROM Professor"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            professores = [Professor(*row) for row in result]
            return professores

        except Exception as e:
            print(e)
    
    def get_professor_by_id(self, cursor, professor_id):
        try:
            sql_command = "SELECT * FROM Professor WHERE professor_id = {}".format(professor_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Professor(*result)

        except Exception as e:
            print(e)
    
    def add(self, cursor, professor):
        try:
            sql_command = "INSERT INTO Professor (professor_name, professor_dep) VALUES (%(professor_name)s, %(professor_dep)s)"
            data_insert = {"professor_name": professor.professor_name, "professor_dep": professor.professor_dep}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def update(self, cursor, professor):
        try:
            sql_command = "UPDATE Professor SET professor_name = %(professor_name)s, professor_dep = %(professor_dep)s WHERE professor_id = %(professor_id)s"
            data_update = {"professor_name": professor.professor_name, "professor_dep": professor.professor_dep}
            cursor.execute(sql_command, data_update)
        except Exception as e:
            print(e)
    
    def delete(self, cursor, professor_id):
        try:
            sql_command = "DELETE FROM Professor WHERE professor_id = {}".format(professor_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)