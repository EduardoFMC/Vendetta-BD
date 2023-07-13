-- Utilize como Visualização

use mydb;

SELECT * FROM TurmaView;

SELECT * FROM Image;

SELECT * FROM User;

SELECT * FROM Departamento;

SELECT * FROM Professor;

SELECT * FROM Disciplina;

SELECT * FROM Turma;

SELECT * FROM Avaliacao;

SELECT * FROM Denuncia;

SELECT @@secure_file_priv;

-- Use ess procedure apenas se tiver certeza que tem certo usuário com essa matrícula
-- CALL GetUserAvaliacoes(123456789);
