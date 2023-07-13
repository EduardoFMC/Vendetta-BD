import mysql.connector

class User():
    def __init__(self, matricula, user_email, password, user_name, creation_date, curso_aluno, is_admin, profile_picture):
        self.matricula = matricula
        self.user_email = user_email
        self.password = password
        self.user_name = user_name
        self.creation_date = creation_date
        self.curso_aluno = curso_aluno
        self.is_admin = is_admin
        self.profile_picture = profile_picture
       
       
class UserDAO:
    def __init__(self):
        pass
    
    def get_all_users(self, cursor):
        try:
            sql_command = "SELECT * FROM User"
            cursor.execute(sql_command)
            result = cursor.fetchall()
            users = [User(*row) for row in result]
            return users
        
        except Exception as e:
            print(e)

    def find_by_matricula(self, cursor, matricula):
        try:
            sql_command = "SELECT * FROM User WHERE matricula = {}".format(str(matricula))
            cursor.execute(sql_command)
            result = cursor.fetchone()
            user = User(*result)
            return user
            
        except Exception as e:
            print(e)
    
    def add(self, cursor, user):
        try:
            sql_command = "INSERT INTO User (matricula, user_email, password, user_name, curso_aluno, is_admin, profile_picture) VALUES (%(matricula)s, %(user_email)s, %(password)s, %(user_name)s, %(curso_aluno)s, %(is_admin)s, %(profile_picture)s)"   
            data_insert = {"matricula": user.matricula, "user_email": user.user_email, "password": user.password, "user_name": user.user_name, "curso_aluno": user.curso_aluno, "is_admin": user.is_admin, "profile_picture": user.profile_picture}
            cursor.execute(sql_command, data_insert)

        except Exception as e:
            print(e)
    
    def update(self, cursor, user):
        try:
            sql_command = "UPDATE User SET user_email = %(user_email)s, password = %(password)s, user_name = %(user_name)s, \
            curso_aluno = %(curso_aluno)s, profile_picture = %(profile_picture)s  WHERE matricula = %(matricula)s"
            
            data_update = {"matricula": user.matricula, "user_email": user.user_email, "password": user.password, "user_name": user.user_name, "curso_aluno": user.curso_aluno, "profile_picture": user.profile_picture}
            cursor.execute(sql_command, data_update)
        except Exception as e:

            print(e)
    
    def delete(self, cursor, matricula):    
        try:
            sql_command = "DELETE FROM User WHERE matricula = {}".format(matricula)
            cursor.execute(sql_command)
        except Exception as e:
            print(e)
        

    
   