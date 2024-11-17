from flask import render_template, request, redirect, url_for, Blueprint
from . import app, db
from .models import Profissional

bp = Blueprint('main', __name__)

@app.route('/')
def index():
  profissionais = Profissional.query.all()
  return render_template('index.html', profissionais=profissionais)

@app.route('/profissional/<int:id>')
def profissional(id):
  profissional = Profissional.query.get_or_404(id)
  return render_template('profissional.html', profissional=profissional)