# Vendetta-Banco-de-Dados - Sistema de avaliação de professores
Projeto final da disciplina de Bancos de Dados, 2023.1.

## Preparação do ambiente

O projeto foi feito utilizando o banco de dados MySQL. Para o uso do banco de dados, é necessário executar os scripts SQL disponibilizados.

Execute o script `criaBD.sql` para criar o Banco `mydb`.

Antes de executar a população do banco, existem dados binários BLOBL que devem ser inseridos. Para isso, insera as imagens na pasta segura disponibilizada pelo seu SGBD.
Para isso rode o script `SELECT @@secure_file_priv;` o que disponibilizará o path da pasta segura para inserção dos binários(imagens). AVISO: windows precisa de duas barras de escapes.
Exemplo: `C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pineapple.jpg`. <-- Windows.

As imagens estão na pasta `images`, pegue as imagens nesta pasta e transfira para a pasta segura.

Após a criação do banco e encontro da pasta do SGBD, execute o script `populaBD.sql`. Mas antes, altere o `<coloque aquui o path, retire os <> e coloque mais um escape \ caso Windows>` do script para o da pasta segura
encontrada.

## Executando o projeto

O site foi feito utilizando Flask. Para executá-lo, é necessário primeiro alterar o arquivo `config.py`. Tal arquivo configura a conexão com o banco MySQL.
Altere o `MYSQL_USER` para o seu usuário.
Altere o `MYSQL_PASSWORD` para a sua senha.


Assim, há dois meio de executar o programa. Assumindo que o caminho do seu terminal aponte para a pasta anterior de app.

`
python .\app\avalia.py
`
ou 
`
flask --app .\app\avalia.py run --debug
`

O site poderá ser acessado através da URL: `http://127.0.0.1:5000/`.

## Interface com usuário


<p align="center"><img src="(https://imgur.com/gallery/GECScfm)" style="width:55%;"/></p>


## Usuários de teste

O banco possui 3 usuários populados para teste, mas os administradores possuem certas funcionalidades especiais:

```
matricula: 123456789
Senha: admin123
```

```
matricula: 202006368
Senha: 123
```
