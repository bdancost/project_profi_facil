from . import db

class Profissional(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100), nullable=False)
  especialidade = db.Column(db.String(100), nullable=False)
  telefone = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  endereco = db.Column(db.String(100), nullable=False)
  preco_medio = db.Column(db.Float, nullable=False)
  avaliacao = db.Column(db.Float, default=0.0)
  descricao = db.Column(db.String(1000), nullable=True)

  def __repr__(self):
    return f"<Profissional {self.nome}>"