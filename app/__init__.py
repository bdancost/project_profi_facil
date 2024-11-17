from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  load_dotenv()
  app.secret_key = os.getenv('SECRET_KEY') # Chave para criptografia (Consegui uma)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  db.init_app(app)

  with app.app_context():
    from . import routes # Importa as rotas
    db.create_all() # Cria tabelas no banco, se não existirem
  
  return app