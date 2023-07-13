from flask_mysqldb import MySQL
import os
#db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
        #cursor = db.cursor()


""" class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'
    MYSQL_DB = 'mydb' """

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = ''
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'mydb'


config = {
    'development': DevelopmentConfig
}