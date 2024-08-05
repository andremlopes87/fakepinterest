# criar a estrutura do banco de dados
from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario): # Funcao obrigatoria quando houver uma estrutura de login
    return Usuario.query.get(int(id_usuario)) # buscar no banco de dados o id do usuario


class Usuario(database.Model, UserMixin): # UserMixin vai definir qual a classe vai gerenciar o login (Usuario)
    id = database.Column(database.Integer, primary_key=True)
    # primary_key = indice
    username = database.Column(database.String, nullable=False)
    # nullable nao pode ser nulo
    email = database.Column(database.String, nullable=False, unique=True)
    # unique nao podem ter dois iguais
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref='usuario', lazy=True)
    # busca eficiente no banco de dados


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)