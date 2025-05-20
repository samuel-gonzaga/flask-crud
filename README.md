# 🧑‍🎓 Flask CRUD App - Student Management

Este é um sistema de CRUD (Create, Read, Update, Delete) de alunos desenvolvido com Python Flask, utilizando PostgreSQL como banco de dados, SQLAlchemy para ORM, Bootstrap 5.3 para o front-end responsivo e DataTables para exibir os dados com paginação, busca e ordenação.

## 📸 Demonstração

![image](https://github.com/user-attachments/assets/7e6196f7-f26b-4913-bb5b-e80737bea3d4)

![image](https://github.com/user-attachments/assets/40f84fcc-7229-4b56-904d-e9f31c06a886)

![image](https://github.com/user-attachments/assets/a11ae720-6af4-4f6c-9f3c-607581034937)

![image](https://github.com/user-attachments/assets/d3e88c79-1bed-4933-adc8-6d5982ce92f2)


## 🚀 Funcionalidades
- Adicionar novos alunos
- Listar alunos em tabela interativa
- Editar dados dos alunos
- Remover alunos com confirmação
- Feedback visual com mensagens flash
- Front-end responsivo com Bootstrap 5.3

## ⚙️ Tecnologias Usadas
Python 3.x

- Flask
- PostgreSQL
- SQLAlchemy
- psycopg2
- Bootstrap 5.3

## 📦 Instalação

1. Clone o repositório
```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie e ative um ambiente virtual
```
python -m venv venv
```

3. Instale as dependências
```
pip install -r requirements.txt
```

4. Configure seu banco PostgreSQL
Crie um banco no PostgreSQL e atualize a string de conexão em `app/config.py`:
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost/nome_do_banco'
```

5. Execute o app
```
python main.py
```
Abra o navegador em http://localhost:8000

## ✅ To-do

- [ ]  Adicionar autenticação (login)
- [ ]  Melhorar responsividade da tabela em telas menores
- [ ]  Adicionar paginação com Flask
- [ ]  Exportar dados da tabela (CSV/Excel)

## ☁️ Sistema Online
O sistema também está disponível em produção:
🔗 https://flask-crud-production-f102.up.railway.app

⚠️ Atenção:
- Este sistema não possui autenticação de usuário.
- Não insira dados pessoais.
- O foco deste projeto é demonstrar conhecimentos técnicos com Flask e PostgreSQL, não segurança.
