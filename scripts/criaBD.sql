CREATE DATABASE mydb;

USE mydb;

CREATE TABLE mydb.Image (
	image_id int NOT NULL AUTO_INCREMENT,
	data longblob NOT NULL,
	file_name varchar(250) NOT NULL,
	mime_type varchar(250) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (image_id)
);

CREATE TABLE mydb.User (
	matricula int NOT NULL,
	user_email varchar(300) NOT NULL,
	password varchar(150) NOT NULL,
	user_name varchar(150) NOT NULL,
	creation_date datetime DEFAULT CURRENT_TIMESTAMP,
    curso_aluno varchar(100) NOT NULL,
    is_admin bool not NULL,
    profile_picture int NOT NULL,
	PRIMARY KEY (matricula),
	FOREIGN KEY (profile_picture)
			REFERENCES Image(image_id)
);

CREATE TABLE mydb.Departamento (
	departamento_id int NOT NULL AUTO_INCREMENT,
    departamento_nome varchar(150) NOT NULL,
    PRIMARY KEY(departamento_id)
);

CREATE TABLE mydb.Professor (
	professor_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (professor_id),
    professor_name varchar(150) NOT NULL,
    professor_dep int NOT NULL,
    FOREIGN KEY (professor_dep)
			REFERENCES Departamento(departamento_id)
);

CREATE TABLE mydb.Disciplina(
	disciplina_id int NOT NULL AUTO_INCREMENT,
    disciplina_nome varchar(150) NOT NULL,
	PRIMARY KEY (disciplina_id),
    disciplina_dep int NOT NULL,
	FOREIGN KEY (disciplina_dep)
			REFERENCES Departamento(departamento_id)
);

CREATE TABLE mydb.Turma (
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
    
);

CREATE TABLE mydb.Avaliacao (
	avaliacao_id int NOT NULL AUTO_INCREMENT,
	avaliacao_descricao  varchar(500) NOT NULL,
	
    PRIMARY KEY (avaliacao_id),
    
	avaliacao_turma_id int NOT NULL,
    FOREIGN KEY (avaliacao_turma_id)
			REFERENCES Turma(turma_id),
            
	avaliacao_user_matricula int NOT NULL,
    FOREIGN KEY (avaliacao_user_matricula)
			REFERENCES User(matricula) ON DELETE CASCADE
);

CREATE TABLE mydb.Denuncia (
	denuncia_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (denuncia_id),
	
    denuncia_num_reports int NOT NULL,
    
    denuncia_avaliacao_id int NOT NULL,
    FOREIGN KEY (denuncia_avaliacao_id) REFERENCES Avaliacao(avaliacao_id) ON DELETE CASCADE,
    
    denuncia_turma_id int NOT NULL,
    FOREIGN KEY (denuncia_turma_id) REFERENCES Turma(turma_id),
    
    denuncia_denunciado_user_matricula int NOT NULL,
    FOREIGN KEY(denuncia_denunciado_user_matricula) REFERENCES User(matricula) ON DELETE CASCADE
);


DELIMITER //

CREATE PROCEDURE GetDenunciaInfo(IN denuncia_id INT)
BEGIN
    SELECT D.denuncia_turma_id AS turma_id,
           T.turma_periodo,
           P.professor_name,
           DSC.disciplina_nome,
           DP.departamento_nome,
           D.denuncia_denunciado_user_matricula,
           U.user_name,
           A.avaliacao_descricao,
           D.denuncia_num_reports
    FROM Denuncia D
    INNER JOIN Turma T ON T.turma_id = D.denuncia_turma_id
    INNER JOIN Professor P ON P.professor_id = T.turma_prof
    INNER JOIN Disciplina DSC ON DSC.disciplina_id = T.turma_disciplina
    INNER JOIN Departamento DP ON DP.departamento_id = T.turma_dep
    INNER JOIN Avaliacao A ON A.avaliacao_id = D.denuncia_avaliacao_id
    INNER JOIN User U ON U.matricula = D.denuncia_denunciado_user_matricula
    WHERE D.denuncia_id = denuncia_id;
END //

DELIMITER ;

CREATE VIEW TurmaView AS
SELECT
    Turma.turma_id AS turma_id,
    Turma.turma_periodo AS turma_periodo,
    Professor.professor_name AS professor_name,
    Disciplina.disciplina_nome AS disciplina_nome,
    Departamento.departamento_nome AS departamento_nome
FROM
    Turma
    JOIN Professor ON Turma.turma_prof = Professor.professor_id
    JOIN Disciplina ON Turma.turma_disciplina = Disciplina.disciplina_id
    JOIN Departamento ON Turma.turma_dep = Departamento.departamento_id;

DELIMITER //

CREATE PROCEDURE GetUserAvaliacoes(IN user_matricula INT)
BEGIN
    SELECT
        A.avaliacao_id,
        A.avaliacao_descricao,
        TV.turma_id,
        TV.turma_periodo,
        TV.professor_name,
        TV.disciplina_nome,
        TV.departamento_nome
    FROM
        Avaliacao A
        INNER JOIN TurmaView TV ON A.avaliacao_turma_id = TV.turma_id
        INNER JOIN User U ON A.avaliacao_user_matricula = U.matricula
    WHERE
        U.matricula = user_matricula;
END //

DELIMITER ;

-- SELECT @@secure_file_priv;


