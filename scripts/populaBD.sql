USE mydb;

-- Image
-- TROCAR O PATH PARA SUA PASTA SEGURA. COLOQUE AS IMAGENS TBM.
-- EXEMPLO: C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pineapple.jpg
-- INSERT INTO mydb.Image(data, file_name, mime_type)
-- VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\default_picture.jpg'), 'default_picture.jpg', 'image/jpg');
-- INSERT INTO mydb.Image(data, file_name, mime_type)
-- VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\carrot.jpg'), 'carrot.jpg', 'image/jpg');
-- INSERT INTO mydb.Image(data, file_name, mime_type)
-- VALUES (LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pineapple.jpg'), 'pineapple.jpg', 'image/jpg');

INSERT INTO mydb.Image(data, file_name, mime_type)
VALUES (LOAD_FILE('<coloque aquui o path, retire os <> e coloque mais um escape \ caso Windows>\default_picture.jpg'), 'default_picture.jpg', 'image/jpg');
INSERT INTO mydb.Image(data, file_name, mime_type)
VALUES (LOAD_FILE('<coloque aquui o path, retire os <> e coloque mais um escape \ caso Windows>\carrot.jpg'), 'carrot.jpg', 'image/jpg');
INSERT INTO mydb.Image(data, file_name, mime_type)
VALUES (LOAD_FILE('<coloque aquui o path, retire os <> e coloque mais um escape \ caso Windows>\pineapple.jpg'), 'pineapple.jpg', 'image/jpg');

-- users --
INSERT INTO User (matricula, user_email, password, user_name, curso_aluno, is_admin, profile_picture)
VALUES (123456789, "admin1@hotmail.com", "admin123", "Ademir", "História", True, 1);
INSERT INTO User (matricula, user_email, password, user_name, curso_aluno, is_admin, profile_picture)
VALUES (202006368, "eduardo@hotmail.com", "123", "Eduardo", "Computação", False, 2);
INSERT INTO User (matricula, user_email, password, user_name, curso_aluno, is_admin, profile_picture)
VALUES (202006161, "maycon@hotmail.com", "1234", "Maycon", "Geografia", False, 3);

-- Departamento

INSERT INTO Departamento(departamento_nome) VALUES ("DEPTO CIÊNCIAS DA COMPUTAÇÃO");
INSERT INTO Departamento(departamento_nome) VALUES ("DEPTO MATEMÁTICA");
INSERT INTO Departamento(departamento_nome) VALUES ("INSTITUTO DE FÍSICA");

-- Professor

INSERT INTO Professor(professor_name, professor_dep) VALUES ("Pedro García", 1);
INSERT INTO Professor(professor_name, professor_dep) VALUES ("Vinicius Lamar", 1);
INSERT INTO Professor(professor_name, professor_dep) VALUES ("Flávio Cavalcante", 1);

INSERT INTO Professor(professor_name, professor_dep) VALUES ("Carlos Carrion", 2);
INSERT INTO Professor(professor_name, professor_dep) VALUES ("Lucas Seco", 2);

INSERT INTO Professor(professor_name, professor_dep) VALUES ("Clóvis Achy", 3);

INSERT INTO Professor(professor_name, professor_dep) VALUES ("Jacobi Pezzuol", 1); -- 7

-- Disciplina

INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Banco de dados", 1);
INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Organização e Arquitetura de Computadores", 1);
INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Lógica Computacional 1", 1);

INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Cálculo Numérico", 2); -- 4
INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Cálculo 1", 2); -- 5

INSERT INTO Disciplina(disciplina_nome, disciplina_dep) VALUES ("Física 1", 3); -- 6

-- Turma

INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2023.1", 1, 1, 1); -- 1
INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2023.1", 2, 2, 1); -- 2
INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2023.1", 7, 2, 1); -- 7
INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2023.1", 3, 3, 1); -- 3

INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2023.1", 4, 4, 2); -- 4
INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2022.1", 5, 5, 2); -- 5

INSERT INTO Turma(turma_periodo, turma_prof, turma_disciplina, turma_dep) VALUES ("2021.2", 6, 6, 3); -- 6

-- Avaliacao

INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 1
VALUES ("Muito bom, recomendo. ótima didática", 1, 202006368);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 2
VALUES ("Péssimo, bla bla bla", 1, 202006368);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 3
VALUES ("ah Mangoe Joe!", 2, 123456789);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 4
VALUES ("Não sabe dar aula, fica enrolando demais", 2, 202006161);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 5
VALUES ("Muito bom, porém dá sono", 3, 202006161);

INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 6
VALUES ("Coisas obscenas", 4, 202006161);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 7
VALUES ("BLA BLA BLA BLA", 4, 123456789);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 8
VALUES ("COmo que entende um cara DESSE!", 5, 202006368);
INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 9
VALUES ("Pode melhorar, se ele entendesse pedagogia.", 5, 123456789);

INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 10 11
VALUES ("SEILA SEILA BLA BLA BLA", 6, 123456789);

INSERT INTO Avaliacao(avaliacao_descricao, avaliacao_turma_id, avaliacao_user_matricula) -- 12
VALUES ("Reprovei com esse, prefiro o outro", 7, 202006368);

-- Denuncia

INSERT INTO Denuncia (denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula) 
VALUES (1, 3, 2, 123456789);
INSERT INTO Denuncia (denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula) 
VALUES (3, 6, 4, 202006161);
INSERT INTO Denuncia (denuncia_num_reports, denuncia_avaliacao_id, denuncia_turma_id, denuncia_denunciado_user_matricula) 
VALUES (2, 11, 7, 202006368)