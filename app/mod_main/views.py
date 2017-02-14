from flask import Blueprint, render_template, request
from app import mongo
from bson import ObjectId
mod_main = Blueprint('main', __name__)


@mod_main.route('/')
def index():

	return render_template("layout.html")

@mod_main.route('/form', methods=['GET','POST'])
def form():
	db = mongo.db.arkep
	if request.method == 'GET':
		emri = "Filan Fistek Filani"
		return render_template("form.html", emri=emri)
	elif request.method == 'POST':
		form_data = request.form.to_dict()
		data = {
          "nderrmarja":{
            "emri": form_data['emri_ndermarrjes'],
            "numri_regjistrimi":form_data['nr_regjistrimit'],
            "adresa":form_data['adresa'],
            "personi_kontaktues":form_data['personi_kontaktues'],
            "telefoni":form_data['telefoni'],
            "email":form_data['email']
            }
        }

		db = mongo.db.arkep
		db.insert(data)
		return render_template("form.html", mesazhi="Faleminderit, forma u insertua")
	else:
		return "Go home, you are drunk"

@mod_main.route('/list', methods=['GET'])
def list():
    db = mongo.db.arkep
    rekordet = db.find()
    return render_template('list.html', rekordet=rekordet)

@mod_main.route('/remove', methods=['POST'])
def remove():
	return render_template('list.html')

@mod_main.route('/raporti/<string:report_id>')
def raporti(report_id):
	db = mongo.db.arkep
	report = db.find_one({ "_id" : ObjectId(report_id) })
	return render_template('raporti.html',report=report)
