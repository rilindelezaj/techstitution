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


        #   "nderrmarja":{
        #     "emri": form_data['emri_ndermarrjes'],
        #     "numri_regjistrimi":form_data['nr_regjistrimit'],
        #     "adresa":form_data['adresa'],
        #     "personi_kontaktues":form_data['personi_kontaktues'],
        #     "telefoni":form_data['telefoni'],
        #     "email":form_data['email']
        #     }
		{
	"pyetsori_tel_mobile": {
		"kompania": {
			"emri_ndermarrjes": form_data['emri_ndermarrjes'],
			"nr_regjistrimit": form_data['nr_regjistrimit'],
			"adresa": form_data['adresa'],
			"personi_kontaktues": form_data['personi_kontaktues'],
			"telefoni": form_data['telefoni'],
			"email_adresa": form_data['email_adresa']
		},
		"infrastruktura": {
			"mbulueshmeria": {
				"popullsise": {
					"gsm": form_data['mbulushmeria_popullsise_gsm'],
					"umts": form_data['mbulushmeria_popullsise_umts'],
					"lte": form_data['mbulushmeria_popullsise_lte'],
					"komente": form_data['mbulushmeria_popullsise_komenti']
				},
				"territori": {
					"gsm": form_data['mbulushmeria_territorit_gsm'],
					"umts": form_data['mbulushmeria_territorit_umts'],
					"lte": form_data['mbulushmeria_territorit_lte'],
					"komente": form_data['mbulushmeria_territorit_komenti']
				}
			},
			"elemente_rrjeti": {
				"qendrat_centraleve_mobile": {
					"gsm": form_data['qendrat_centrale_mobile_gsm'],
					"umts": form_data['qendrat_centrale_mobile_umts'],
					"lte": form_data['qendrat_centrale_mobile_lte'],
					"komente": form_data['qendrat_centrale_mobile_komenti']
				},
				"portat_qendrat_centraleve_mobile": {
					"gsm": form_data['portat_qendrat_centrale_mobile_gsm'],
					"umts": form_data['portat_qendrat_centrale_mobile_umts'],
					"lte": form_data['portat_qendrat_centrale_mobile_lte'],
					"komente": form_data['portat_qendrat_centrale_mobile_komenti']
				},
				"kontrollues_stacione_baze": {
					"gsm": form_data['kontrollues_stacion_baz_gsm'],
					"umts": form_data['kontrollues_stacion_baz_umts'],
					"lte": form_data['kontrollues_stacion_baz_lte'],
					"komente": form_data['kontrollues_stacion_baz_komenti']
				},
				"stacionet_baze": {
					"gsm": form_data['stacionet_baze_gsm'],
					"umts": form_data['stacionet_baze_umts'],
					"lte": form_data['stacionet_baze_lte'],
					"komente": form_data['stacionet_baze_komenti']
				}
			},
			"kapaciteti": {
				"kapaciteti_total_ne_rrjet": {
					"gsm": form_data['kapaciteti_total_rrjet_gsm'],
					"umts": form_data['kapaciteti_total_rrjet_umts'],
					"lte": form_data['kapaciteti_total_rrjet_lte'],
					"komente": form_data['kapaciteti_total_rrjet_komenti']
				},
				"trafiku_peak": {
					"gsm": form_data['trafiku_peak_gsm'],
					"umts": form_data['trafiku_peak_umts'],
					"lte": form_data['trafiku_peak_lte'],
					"komente": form_data['trafiku_peak_komenti']
				},
				"trafiku_off_peak": {
					"gsm": form_data['trafiku_offpeak_gsm'],
					"umts": form_data['trafiku_offpeak_umts'],
					"lte": form_data['trafiku_offpeak_lte'],
					"komente": form_data['trafiku_offpeak_komenti']
				}
			}
		},
		"perdoruesit_dhe_ndarja": {
			"totali_perdoruesve_aktiv": {
				"sherbimet_zeri_pako_interneti": {
					"parapagim_dhe_kontrate": {
						"parapagim": {
							"numri_perdoruesve": form_data['perdoruesit_parapagim_numri'],
							"te_hyrat_000s": form_data['perdoruesit_parapagim_hyrat_000s'],
							"komente": form_data['perdoruesit_parapagim_komenti']
						},
						"kontrate": {
							"numri_perdoruesve": form_data['perdoruesit_kontrate_numri'],
							"te_hyrat_000s": form_data['perdoruesit_kontrate_000s'],
							"komente": form_data['perdoruesit_kontrate_komenti']
						}
					},
					"biznese": {
						"parapagim": {
							"numri_perdoruesve": form_data['biznes_perdorues_parapagim_numri'],
							"te_hyrat_000s": form_data['biznes_perdorues_parapagim_000s'],
							"komente": form_data['biznes_perdorues_parapagim_komenti']
						},
						"kontrate": {
							"numri_perdoruesve": form_data['biznes_perdorues_kontrate_numri'],
							"te_hyrat_000s": form_data['biznes_perdorues_kontrate_000s'],
							"komente": form_data['biznes_perdorues_kontrate_komenti']
						}
					},
					"qasje_internet": {
						"individual": {
							"GSM": {
								"Prepaid": form_data['internet_individual_gsm_prepaid'],
								"Postpaid": form_data['internet_individual_gsm_postpid']
							},
							"UMTS": {
								"Prepaid": form_data['internet_individual_umts_prepaid'],
								"Postpaid": form_data['internet_individual_umts_postpaid']
							},
							"LTE": {
								"Prepaid": form_data['internet_individual_lte_prepaid'],
								"Postpaid": form_data['internet_individual_lte_postpaid']
							},
							"Te_hyrat_000s": {
								"Prepaid": form_data['internet_individual_000s_prepaid'],
								"Postpaid": form_data['internet_individual_000s_postpaid']
							},
							"komente": form_data['internet_individual_komenti']
						},
						"biznese": {
							"GSM": {
								"Prepaid": form_data['internet_biznes_gsm_prepaid'],
								"Postpaid": form_data['internet_biznes_gsm_postpaid']
							},
							"UMTS": {
								"Prepaid": form_data['internet_biznes_umts_prepaid'],
								"Postpaid": form_data['internet_biznes_umts_postpaid']
							},
							"LTE": {
								"Prepaid": form_data['internet_biznes_lte_prepaid'],
								"Postpaid": form_data['internet_biznes_lte_postpaid']
							},
							"Te_hyrat_000s": {
								"Prepaid": form_data['internet_biznes_000s_prepaid'],
								"Postpaid": form_data['internet_biznes_000s_postpaid']
							},
							"komente": form_data['internet_biznes_komenti']
						}
					}
				},
				"qasje_vetem_interneti": {
					"Individual": {
						"GSM": {
							"Prepaid": form_data['vetem_internet_individual_gsm_prepaid'],
							"Postpaid": form_data['vetem_internet_individual_gsm_postpid']
						},
						"UMTS": {
							"Prepaid": form_data['vetem_internet_individual_umts_prepaid'],
							"Postpaid": form_data['vetem_internet_individual_umts_postpaid']
						},
						"LTE": {
							"Prepaid": form_data['vetem_internet_individual_lte_prepaid'],
							"Postpaid": form_data['vetem_internet_individual_lte_postpaid']
						},
						"Te_hyrat_000s": {
							"Prepaid": form_data['vetem_internet_individual_000s_prepaid'],
							"Postpaid": form_data['vetem_internet_individual_000s_postpaid']
						},
						"komente": form_data['vetem_internet_individual_komenti']
					},
					"Biznes": {
						"GSM": {
							"Prepaid": form_data['vetem_internet_biznes_gsm_prepaid'],
							"Postpaid": form_data['vetem_internet_biznes_gsm_postpaid']
						},
						"UMTS": {
							"Prepaid": form_data['vetem_internet_biznes_umts_prepaid'],
							"Postpaid": form_data['vetem_internet_biznes_umts_postpaid']
						},
						"LTE": {
							"Prepaid": form_data['vetem_internet_biznes_lte_prepaid'],
							"Postpaid": form_data['vetem_internet_biznes_lte_postpaid']
						},
						"Te_hyrat_000s": {
							"Prepaid": form_data['vetem_internet_biznes_000s_prepaid'],
							"Postpaid": form_data['vetem_internet_biznes_000s_postpaid']
						},
						"komente": form_data['vetem_internet_biznes_komenti']
					}
				}
			}
		},
		"trafiku_te_hyrat_origjinimi_i_thirrjeve": {
			"trafiku_total_i_perdoruesve_postpaid": {
				"individual": {
					"nr_min_ne_000": form_data['trafiku_kontrate_individual_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_kontrate_individual_hyrat'],
					"komente": form_data['trafiku_kontrate_individual_komenti']
				},
				"biznesit": {
					"nr_min_ne_000": form_data['trafiku_kontrate_biznes_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_kontrate_biznes_hyrat'],
					"komente": form_data['trafiku_kontrate_biznes_komenti']
				}
			},
			"trafiku_total_i_perdoruesve_prepaid": {
				"individual": {
					"nr_min_ne_000": form_data['trafiku_parapagim_individual_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_parapagim_individual_hyrat'],
					"komente": form_data['trafiku_parapagim_individual_komenti']
				},
				"biznesit": {
					"nr_min_ne_000": form_data['trafiku_parapagim_biznes_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_parapagim_biznes_hyrat'],
					"komente": form_data['trafiku_parapagim_biznes_komenti']
				}
			},
			"Trafiku_sipas_destinacionit": {
				"brenda_rrjetit_on-net": {
					"nr_min_ne_000": form_data['trafiku_distinacioni_brenda_rrjetit_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_distinacioni_brenda_rrjetit_hyrat'],
					"komente": form_data['trafiku_distinacioni_brenda_rrjetit_komenti']
				},
				"rrjetat_mobile_(off-net)": {
					"nr_min_ne_000": form_data['trafiku_distinacioni_jashte_rrjetit_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_distinacioni_jashte_rrjetit_hyrat'],
					"komente": form_data['trafiku_distinacioni_jashte_rrjetit_komenti']
				},
				"operatori1": {
					"emri": form_data['trafiku_distinacioni_jashte_rrjetit_operatori1_emri'],
					"nr_min_ne_000": form_data['trafiku_distinacioni_jashte_rrjetit_operatori1_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_distinacioni_jashte_rrjetit_operatori1_hyrat'],
					"komente": form_data['trafiku_distinacioni_jashte_rrjetit_operatori1_komenti']
				}
			},
			"drejt_rrjetave_fikse": {
				"operatori1": {
					"emri": form_data['rrjete_fikse_operatori1_minuta'],
					"nr_min_ne_000": form_data['rrjete_fikse_operatori1_minuta'],
					"te_hyrat_ne_000s": form_data['rrjete_fikse_operatori1_hyrat'],
					"komente": form_data['rrjete_fikse_operatori1_komenti']
				}
			},
			"drejt_rrjetave_nderkombetare": {
				"shqiperi": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_shqiperi_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_shqiperi_hyrat'],
					"komente": form_data['trafiku_nderkombtar_shqiperi_komenti']
				},
				"maqedoni": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_maqedoni_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_maqedoni_hyrat'],
					"komente": form_data['trafiku_nderkombtar_maqedoni_komenti']
				},
				"mali_i_zi": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_malizi_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_malizi_hyrat'],
					"komente": form_data['trafiku_nderkombtar_malizi_komenti']
				},
				"serbi": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_serbi_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_serbi_hyrat'],
					"komente": form_data['trafiku_nderkombtar_serbi_komenti']
				},
				"kroaci": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_kroaci_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_kroaci_hyrat'],
					"komente": form_data['trafiku_nderkombtar_kroaci_komenti']
				},
				"bosne_dhe_hercegovine": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_bonse_hercegovine_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_bonse_hercegovine_hyrat'],
					"komente": form_data['trafiku_nderkombtar_bonse_hercegovine_komenti']
				},
				"turqi": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_turqi_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_turqi_hyrat'],
					"komente": form_data['trafiku_nderkombtar_turqi_komenti']
				},
				"gjermani": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_gjermani_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_gjermani_hyrat'],
					"komente": form_data['trafiku_nderkombtar_gjermani_komenti']
				},
				"itali": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_itali_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_itali_hyrat'],
					"komente": form_data['trafiku_nderkombtar_itali_komenti']
				},
				"france": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_france_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_france_hyrat'],
					"komente": form_data['trafiku_nderkombtar_france_komenti']
				},
				"zvicer": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_zvicerr_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_zvicerr_hyrat'],
					"komente": form_data['trafiku_nderkombtar_zvicerr_komenti']
				},
				"mbreteri_e_bashkuar": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_britani_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_britani_hyrat'],
					"komente": form_data['trafiku_nderkombtar_britani_komenti']
				},
				"shba": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_shba_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_shba_hyrat'],
					"komente": form_data['trafiku_nderkombtar_shba_komenti']
				},
				"kanade": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_kanade_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_kanade_hyrat'],
					"komente": form_data['trafiku_nderkombtar_kanade_komenti']
				},
				"totali_i_te_trafikut_dhe_te_hyrave_drejt_shteteve": {
					"nr_min_ne_000": form_data['trafiku_nderkombtar_total_shteteve_minuta'],
					"te_hyrat_ne_000s": form_data['trafiku_nderkombtar_total_shteteve_hyrat'],
					"komente": form_data['trafiku_nderkombtar_total_shteteve_komenti']
				}
			}
		}
	}
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
