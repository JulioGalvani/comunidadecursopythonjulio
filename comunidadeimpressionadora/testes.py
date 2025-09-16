from comunidadeimpressionadora import app
from comunidadeimpressionadora.models import Usuario, Post
from comunidadeimpressionadora import database

with app.app_context():
    database.create_all()  # Cria todas as tabelas definidas nos modelos
    print("Banco de dados e tabelas criados com sucesso!")