""" CREATE TABLE mydb.Departamento (
	departamento_id int NOT NULL AUTO_INCREMENT,
    departamento_nome varchar(150) NOT NULL,
    PRIMARY KEY(departamento_id)
);
 """

class Departamento():
    def __init__(self, departamento_id, departamento_nome):
        self.departamento_id = departamento_id
        self.departamento_nome = departamento_nome


class DepartamentoDAO():

    def __init__(self):
        pass

    def get_all_departamentos(self, cursor):
        try:
            sql_command = "SELECT * FROM Departamento"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            departamentos = [Departamento(*row) for row in result]
            return departamentos

        except Exception as e:
            print(e)

    def get_departamento_by_id(self, cursor, departamento_id):
        try:
            sql_command = "SELECT * FROM Departamento WHERE departamento_id = {}".format(departamento_id)
            cursor.execute(sql_command)
            result = cursor.fetchone()
            return Departamento(*result)

        except Exception as e:
            print(e)

    def add(self, cursor, departamento):
        try:
            sql_command = "INSERT INTO Departamento (departamento_nome) VALUES (%(departamento_nome)s)"
            data_insert = {"departamento_nome": departamento.departamento_nome}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)

    def update(self, cursor, departamento):
        try:
            sql_command = "UPDATE Departamento SET departamento_nome = %(departamento_nome)s WHERE departamento_id = %(departamento_id)s"
            data_update = {"departamento_nome": departamento.departamento_nome}
            cursor.execute(sql_command, data_update)
        except Exception as e:
            print(e) 
    
    def delete(self, cursor, departamento_id):
        try:
            sql_command = "DELETE FROM Departamento WHERE departamento_id = {}".format(departamento_id)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)