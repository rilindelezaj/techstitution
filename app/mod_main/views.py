from flask import Blueprint, render_template, request
from app import mongo

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	db = mongo.db.arkep
	db.insert({"name" : "arkep"})
	return render_template("index.html")

@mod_main.route('/form', methods=['GET','POST'])
def form():
	if request.method == 'GET':
		return render_template("form.html")
	elif request.method == 'POST':
		db = mongo.db.arkep
		db.insert({"name" : "arkep"})
		return "Form inserted"
	else:
		return "Go home, you are drunk"
