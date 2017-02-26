from flask import Blueprint, render_template, request
from app import mongo
from bson.json_util import dumps
from bson import ObjectId
mod_main = Blueprint('main', __name__)


@mod_main.route('/')
def index():

	return render_template("index.html")

@mod_main.route('/form', methods=['GET','POST'])
def form():
	db = mongo.db.arkep
	if request.method == 'GET':
		emri = "Filan Fistek Filani"
		return render_template("form.html", emri=emri)
	elif request.method == 'POST':
		form_data = request.form.to_dict()
		data = {
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
		},

# vazhdimi i dimit

		"Trafiku_origjimi_SMS_MMS_Outgoing": {
      "Te_hyrat_total_SMS_origjinuar": {
        "on_net": {
          "nr_sms_000s": form_data['trafiku_Outgoing_on_net_nr'],
          "te_hyrat_000s": form_data['trafiku_Outgoing_on_net_thyrat'],
          "komente": form_data['trafiku_Outgoing_on_net_komente']
        },
        "off_net": {
          "nr_sms_000s": form_data['trafiku_Outgoing_off_net_nr'],
          "te_hyrat_000s": form_data['trafiku_Outgoing_off_net_thyrat'],
          "komente": form_data['trafiku_Outgoing_off_net_komente']
        },
        "operatori_1": {
          "emri": form_data['trafiku_Outgoing_operatori_1_name'],
          "nr_sms_000s": form_data['trafiku_Outgoing_operatori_1_nr'],
          "te_hyrat_000s": form_data['trafiku_Outgoing_operatori_1_thyrat'],
          "komente": form_data['trafiku_Outgoing_operatori_1_komente']
        },
        "drejt_rrjeteve_nderkombtare": {
          "nr_sms_000s": form_data['trafiku_Outgoing_rrjeteve_nderkombtare_nr'],
          "te_hyrat_000s": form_data['trafiku_Outgoing_rrjeteve_nderkombtare_thyrat'],
          "komente": form_data['trafiku_Outgoing_rrjeteve_nderkombtare_komente']
        },
        "Te_hyrat_total_MMS_origjinuar": {
          "on_net": {
            "nr_sms_000s": form_data['trafiku_outgoing_MMS_on_net_nr'],
            "te_hyrat_000s": form_data['trafiku_outgoing_MMS_on_net_thyrat'],
            "komente": form_data['trafiku_outgoing_MMS_on_net_komente']
          },
          "off_net": {
            "nr_sms_000s": form_data['trafiku_outgoing_MMS_off_net_nr'],
            "te_hyrat_000s": form_data['trafiku_outgoing_MMS_off_net_thyrat'],
            "komente": form_data['trafiku_outgoing_MMS_off_net_komente']
          },
          "operatori_1": {
            "emri": form_data['trafiku_outgoing_MMS_operatori1_emri'],
            "nr_sms_000s": form_data['trafiku_outgoing_MMS_operatori1_nr'],
            "te_hyrat_000s": form_data['trafiku_outgoing_MMS_operatori1_thyrat'],
            "komente": form_data['trafiku_outgoing_MMS_operatori1_komente']
          },
		  "drejt_rrjeteve_nderkombtare": {
            "nr_sms_000s": form_data['trafiku_outgoing_MMS_rrjeteve_nderkomtare_nr'],
            "te_hyrat_000s": form_data['trafiku_outgoing_MMS_rrjeteve_nderkomtare_thyrat'],
            "komente": form_data['trafiku_outgoing_MMS_rrjeteve_nderkomtare_komente']
          }
        }
      }
    },

    "Trafiku_ne_thirrje_Incoming": {
    "Nga_rrjetet_tjera_mobile_off_net": {
      "operatori_1": {
        "emri": form_data['trafiku_thirrje_incoming_off_net_operatori1_name'],
        "nr_minutave_000": form_data['trafiku_thirrje_incoming_off_net_operatori1_nr'],
        "te_hyrat_000s": form_data['trafiku_thirrje_incoming_off_net_operatori1_thyrat'],
        "komente": form_data['trafiku_thirrje_incoming_off_net_operatori1_komente']
      }
	  },
      "Nga_rrjeti_fiks": {
        "operatori_1": {
          "emri": form_data['trafiku_thirrje_incoming_rrjet_fiks_operatori1_name'],
          "nr_minutave_000": form_data['trafiku_thirrje_incoming_rrjet_fiks_operatori1_nr'],
          "te_hyrat_000s": form_data['trafiku_thirrje_incoming_rrjet_fiks_operatori1_thyrat'],
          "komente": form_data['trafiku_thirrje_incoming_rrjet_fiks_operatori1_komenti']
        }
		},
        "Nga_thirrjet_hyrese_nderkombtare": {
          "nga_rrjeti_fiks": {
            "nr_minutave_000": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_fiks_nr'],
            "te_hyrat_000s": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_fiks_thyrat'],
            "komente": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_fiks_komente']
          },
          "nga_rrjeti_mobil": {
            "nr_minutave_000": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_mobile_nr'],
            "te_hyrat_000s": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_mobile_thyrat'],
            "komente": form_data['trafiku_thirrje_incoming_hyrje_nderkombtare_mobile_komente']
          }
        }
      },
	# ok
    "Trafiku_dhe_te_hyrat_nga_roamingu": {

    	"trafiku_total_roamingu_outbound": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_outbound_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_outbound_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_outbound_komente'],
        "trafiku_dales_origjinuar": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_dales_origjinuar_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_dales_origjinuar_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_dales_origjinuar_komente']
        },
        "trafiku_hyres_terminuar": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_hyres_terminuar_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_hyres_terminuar_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_hyres_terminuar_komente']
        },
        "sms": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_sms_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_sms_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_sms_komente']
        },
        "data_roaming": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_data_roaming_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_data_roaming_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_data_roaming_komente']
        }
		},
        "trafiku_total_roamingu_inbound": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_total_inbound_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_total_inbound_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_total_inbound_komente'],

		"trafiku_dales_origjinuar_i": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_total_inbound_dales_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_total_inbound_dales_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_total_inbound_dales_komente']
        },
        "trafiku_hyres_terminuar_i": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_total_inbound_hyres_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_total_inbound_hyres_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_total_inbound_hyres_komente']
        },
        "sms_i": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_total_inbound_sms_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_total_inbound_sms_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_total_inbound_sms_komente']
        },
        "data_roaming_i": {
          "nr_min_sms_000s": form_data['trafiku_thyrat_roamingu_total_inbound_data_roaming_nr'],
          "te_hyrat_000s": form_data['trafiku_thyrat_roamingu_total_inbound_data_roaming_thyrat'],
          "komente": form_data['trafiku_thyrat_roamingu_total_inbound_data_roaming_komente']
        }
      }
    },

	# ok

    "Trafiku_te_dhenave_data": {
      "trafiku_total_perdoruesve_prepaid_postpaid": {
        "perdoruesit_parapagim_prepaid": {
          "trafiku_GB": form_data['trafiku_dhenave_data_perdoruesit_prepaid_trafiku'],
          "te_hyrat_000s": form_data['trafiku_dhenave_data_perdoruesit_prepaid_thyrat'],
          "komente": form_data['trafiku_dhenave_data_perdoruesit_prepaid_komente']
        },
        "perdoruesit_kontrat_postpaid": {
          "trafiku_GB": form_data['trafiku_dhenave_data_perdoruesit_postpaid_trafiku'],
          "te_hyrat_000s": form_data['trafiku_dhenave_data_perdoruesit_postpaid_thyrat'],
          "komente": form_data['trafiku_dhenave_data_perdoruesit_postpaid_komente']
        }
      }
    },
	#ok
    "tarifat_prepaid": {

        "emri": form_data['prepaid_plani_1_emri'],
        "tarifa_e_aktivizimit":form_data['prepaid_plani_1_tarifa_aktivizimit'],
        "tarifa_grupet_biznesit": form_data['prepaid_plani_1_tarifa_biznesit'],
      "kohezgjatja_e_kontrates_gr_biznesit": form_data['prepaid_plani_1_kohezgjatja_biz'],
      "numri_i_perdoruesve": form_data['prepaid_plani_1_numri_perd'],
	  "komente":form_data['prepaid_plani_1_komente'],

    "thirrjet_kombetare": {
      "brenda_rrjetit_MNO": {
          "peak": form_data['prepaid_plani_1_thirrjet_kombtare_MNO_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_kombtare_MNO_off_peak'],
          "komente": form_data['prepaid_plani_1_thirrjet_kombtare_MNO_komente']
      },
      "brenda_rrj_MNOMVNO": {
          "peak": form_data['prepaid_plani_1_thirrjet_kombtare_MNOMVNO_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_kombtare_MNOMVNO_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_kombtare_MNOMVNO_komente']
      },
      "ne_rrjetin_tjeter_MNO": {
          "peak": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MNO_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MNO_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MNO_komente']
      },
      "ne_rrjetin_tjeter_MVNO": {
          "peak": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MVNO_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MVNO_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_kombtare_tjeter_MVNO_komente']
      },
      "ne_rrjetin_fiks_OP1": {
	  	"emri":form_data['prepaid_plani_1_thirrjet_kombtare_fiks_emri'],
        "peak": form_data['prepaid_plani_1_thirrjet_kombtare_fiks_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_kombtare_fiks_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_kombtare_fiks_komente']
      }
    },
    "thirrjet_nderkombetare": {
      "shqiperi": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_shqiperi_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_shqiperi_off_peak'],
          "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_shqiperi_komente']
      },
      "maqedoni": {
        "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_maqedoni_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_maqedoni_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_maqedoni_komente']
      },
      "mal_te_zi": {
        "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_malizi_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_malizi_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_malizi_komente']
      },
      "serbi": {
        "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_serbi_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_serbi_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_serbi_komente']
      },
      "kroaci": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_kroaci_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_kroaci_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_kroaci_komente']
      },
      "bosnje_dhe_hercegovine": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_bosna_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_bosna_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_bosna_komente']
      },
      "turqi": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_turqi_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_turqi_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_turqi_komente']
      },
      "gjermani": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_gjermani_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_gjermani_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_gjermani_komente']
      },
      "itali": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_itali_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_itali_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_itali_komente']
      },
      "france": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_france_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_france_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_france_komente']
      },
      "zvicer": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_zvicerr_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_zvicerr_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_zvicerr_komente']
      },
      "mbreteri_e_bashkuar":{
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_mbreteri_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_mbreteri_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_mbreteri_komente']
      },
      "shba": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_shba_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_shba_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_shba_komente']
      },
      "kanada": {
          "peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_kanada_peak'],
          "off_peak": form_data['prepaid_plani_1_thirrjet_nderkombtare_kanada_off_peak'],
        "komente": form_data['prepaid_plani_1_thirrjet_nderkombtare_kanada_komente']
      }
    },

	# vetura
    "tarifat_e_sms": {
      "brenda_rrjetit": {
          "peak": form_data['prepaid_plani_1_tarifat_sms_brenda_rrjetit_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_sms_brenda_rrjetit_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_sms_brenda_rrjetit_komente']
      },
      "jashte_rrjetit": {
          "peak": form_data['prepaid_plani_1_tarifat_sms_jashte_rrjetit_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_sms_jashte_rrjetit_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_sms_jashte_rrjetit_komente']
      },
      "nderkombetar": {
          "peak": form_data['prepaid_plani_1_tarifat_sms_nderkombtar_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_sms_nderkombtar_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_sms_nderkombtar_komente']
      }
    },
    "tarifat_MMS": {
      "brenda_rrjetit": {
          "peak": form_data['prepaid_plani_1_tarifat_mms_brenda_rrjetit_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_mms_brenda_rrjetit_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_mms_brenda_rrjetit_komente']
      },
      "jashte_rrjetit": {
          "peak": form_data['prepaid_plani_1_tarifat_mms_jashte_rrjetit_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_mms_jashte_rrjetit_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_mms_jashte_rrjetit_komente']
      },
      "nderkombetar": {
          "peak": form_data['prepaid_plani_1_tarifat_mms_nderkombtar_peak'],
          "off_peak": form_data['prepaid_plani_1_tarifat_mms_nderkombtar_off_peak'],
        "komente": form_data['prepaid_plani_1_tarifat_mms_nderkombtar_komente']
      }
    },

    "tarifat_e_te_dhenave": {
      "tarifa_javore_mujore": {
          "peak": form_data['tarifat_dhena_javore_mujore_peak'],
          "off_peak": form_data['tarifat_dhena_javore_mujore_off_peak'],
        "komente": form_data['tarifat_dhena_javore_mujore_komente']
      },
      "tarifa_per_100kB": {
          "peak": form_data['tarifat_dhena_tarifa_100kB_peak'],
          "off_peak": form_data['tarifat_dhena_tarifa_100kB_off_peak'],
        "komente": form_data['tarifat_dhena_tarifa_100kB_komente']
      }
    }
    },
#ok
    "tarifat_kontrate": {
      "emri_planit_tarifor1":  form_data['tarifat_kontrate_plani_tarifor_1_emri'],
      "kohezgjatja_e_kontrates_muaj":form_data['tarifat_kontrate_plani_tarifor_1_kohezgjatja_kontrates'],
      "tarifa_e_aktivizimit": form_data['tarifat_kontrate_plani_tarifor_1_tarifa_aktivizimit'],
      "tarifa_parapagimi_mujor":  form_data['tarifat_kontrate_plani_tarifor_1_tarifa_parapagimi_mujore'],
      "numri_i_min_brenda_rrjetit": form_data['tarifat_kontrate_plani_tarifor_1_numri_min_brenda_rrjetit'],
      "numri_i_min_jashte_rrjetit": form_data['tarifat_kontrate_plani_tarifor_1_numri_min_jashte_rrjetit'],
      "numri_i_min_tel_fiks":form_data['tarifat_kontrate_plani_tarifor_1_numri_min_tel_fiks'],
      "numri_sms": form_data['tarifat_kontrate_plani_tarifor_1_numri_sms'],
      "numri_i_mms": form_data['tarifat_kontrate_plani_tarifor_1_numri_mms'],
      "internet_ne_gb": form_data['tarifat_kontrate_plani_tarifor_1_internet_gb'],
      "numri_i_perdoruesve": form_data['tarifat_kontrate_plani_tarifor_1_numri_perdoruesve'],
			"komente":form_data['tarifat_kontrate_plani_tarifor_1_komente'],

	"thirrjet_kombetare": {
	    "brenda_rrjetit_MNO": {
	        "peak": form_data['postpaid_plani_1_thirrjet_kombtare_MNO_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_kombtare_MNO_off_peak'],
	        "komente": form_data['postpaid_plani_1_thirrjet_kombtare_MNO_komente']
	    },
	    "brenda_rrj_MNOMVNO": {
	        "peak": form_data['postpaid_plani_1_thirrjet_kombtare_MNOMVNO_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_kombtare_MNOMVNO_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_kombtare_MNOMVNO_komente']
	    },
	    "ne_rrjetin_tjeter_MNO": {
	        "peak": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MNO_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MNO_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MNO_komente']
	    },
	    "ne_rrjetin_tjeter_MVNO": {
	        "peak": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MVNO_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MVNO_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_kombtare_tjeter_MVNO_komente']
	    },
	    "ne_rrjetin_fiks_OP1": {
			"emri":form_data['postpaid_plani_1_thirrjet_kombtare_fiks_emri'],
	      "peak": form_data['postpaid_plani_1_thirrjet_kombtare_fiks_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_kombtare_fiks_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_kombtare_fiks_komente']
	    }
	  },
	  "thirrjet_nderkombetare": {
	    "shqiperi": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_shqiperi_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_shqiperi_off_peak'],
	        "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_shqiperi_komente']
	    },
	    "maqedoni": {
	      "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_maqedoni_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_maqedoni_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_maqedoni_komente']
	    },
	    "mal_te_zi": {
	      "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_malizi_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_malizi_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_malizi_komente']
	    },
	    "serbi": {
	      "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_serbi_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_serbi_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_serbi_komente']
	    },
	    "kroaci": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_kroaci_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_kroaci_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_kroaci_komente']
	    },
	    "bosnje_dhe_hercegovine": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_bosna_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_bosna_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_bosna_komente']
	    },
	    "turqi": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_turqi_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_turqi_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_turqi_komente']
	    },
	    "gjermani": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_gjermani_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_gjermani_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_gjermani_komente']
	    },
	    "itali": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_itali_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_itali_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_itali_komente']
	    },
	    "france": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_france_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_france_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_france_komente']
	    },
	    "zvicer": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_zvicerr_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_zvicerr_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_zvicerr_komente']
	    },
	    "mbreteri_e_bashkuar":{
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_mbreteri_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_mbreteri_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_mbreteri_komente']
	    },
	    "shba": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_shba_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_shba_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_shba_komente']
	    },
	    "kanada": {
	        "peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_kanada_peak'],
	        "off_peak": form_data['postpaid_plani_1_thirrjet_nderkombtare_kanada_off_peak'],
	      "komente": form_data['postpaid_plani_1_thirrjet_nderkombtare_kanada_komente']
	    }
	  },

	# vetura
	  "tarifat_e_sms": {
	    "brenda_rrjetit": {
	        "peak": form_data['postpaid_plani_1_tarifat_sms_brenda_rrjetit_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_sms_brenda_rrjetit_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_sms_brenda_rrjetit_komente']
	    },
	    "jashte_rrjetit": {
	        "peak": form_data['postpaid_plani_1_tarifat_sms_jashte_rrjetit_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_sms_jashte_rrjetit_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_sms_jashte_rrjetit_komente']
	    },
	    "nderkombetar": {
	        "peak": form_data['postpaid_plani_1_tarifat_sms_nderkombtar_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_sms_nderkombtar_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_sms_nderkombtar_komente']
	    }
	  },
	  "tarifat_MMS": {
	    "brenda_rrjetit": {
	        "peak": form_data['postpaid_plani_1_tarifat_mms_brenda_rrjetit_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_mms_brenda_rrjetit_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_mms_brenda_rrjetit_komente']
	    },
	    "jashte_rrjetit": {
	        "peak": form_data['postpaid_plani_1_tarifat_mms_jashte_rrjetit_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_mms_jashte_rrjetit_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_mms_jashte_rrjetit_komente']
	    },
	    "nderkombetar": {
	        "peak": form_data['postpaid_plani_1_tarifat_mms_nderkombtar_peak'],
	        "off_peak": form_data['postpaid_plani_1_tarifat_mms_nderkombtar_off_peak'],
	      "komente": form_data['postpaid_plani_1_tarifat_mms_nderkombtar_komente']
	    }
	  },

	  "tarifat_e_te_dhenave": {
	    "tarifa_javore_mujore": {
	        "peak": form_data['postpaid_tarifat_dhena_javore_mujore_peak'],
	        "off_peak": form_data['postpaid_tarifat_dhena_javore_mujore_off_peak'],
	      "komente": form_data['postpaid_tarifat_dhena_javore_mujore_komente']
	    },
	    "tarifa_per_100kB": {
	        "peak": form_data['postpaid_tarifat_dhena_tarifa_100kB_peak'],
	        "off_peak": form_data['postpaid_tarifat_dhena_tarifa_100kB_off_peak'],
	      "komente": form_data['postpaid_tarifat_dhena_tarifa_100kB_komente']
	    }
	  }
	},

#ok


    "Tarifat_e_Roamingut_Outbond_parapagim": {
      "Shqiperi": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_minimale_origjinimi'],
          "pranimi": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_minimale_pranimi'],
          "SMS": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_minimale_sms'],
          "DatakB": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_minimale_datakb'],
		  },
        "tarifat_maksimale": {
            "origjinimi": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_maksimale_origjinimi'],
        "pranimi": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_maksimale_pranimi'],
        "SMS": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_maksimale_sms'],
        "DatakB": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_maksimale_datakb'],
    "Komente": form_data['tarifat_roaming_outbound_parapagim_shqiperi_tarifat_maksimale_komente']
        }
      },
      "Maqedoni": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_maksimale_origjinimi'],
		     "pranimi": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_maksimale_pranimi'],
		     "SMS": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_maksimale_sms'],
		     "DatakB": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_maksimale_datakb'],
		 "Komente": form_data['tarifat_roaming_outbound_parapagim_maqedoni_tarifat_maksimale_komente']
        }
      },
	        "Mali_i_zi": {
	          "tarifat_minimale": {
			        "origjinimi": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_minimale_origjinimi'],
			        "pranimi": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_minimale_pranimi'],
			        "SMS": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_minimale_sms'],
			        "DatakB": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_minimale_datakb'],
			    # "Komente": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_minimale_komente']
			       },
			       "tarifat_maksimale": {
			         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_maksimale_origjinimi'],
			         "pranimi": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_maksimale_pranimi'],
			         "SMS": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_maksimale_sms'],
			         "DatakB": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_maksimale_datakb'],
			     "Komente": form_data['tarifat_roaming_outbound_parapagim_malizi_tarifat_maksimale_komente']
			       }
	        },
      "Serbi": {
        "tarifat_minimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_minimale_origjinimi'],
		     "pranimi": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_minimale_pranimi'],
		     "SMS": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_minimale_sms'],
		     "DatakB": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_minimale_datakb'],
		#  "Komente": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_maksimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_maksimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_maksimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_maksimale_datakb'],
		  "Komente": form_data['tarifat_roaming_outbound_parapagim_serbi_tarifat_maksimale_komente']
        }
      },
      "Kroaci": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_minimale_komente']
        },
        "trifat_maksimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_maksimale_origjinimi'],
		     "pranimi": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_maksimale_pranimi'],
		     "SMS": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_maksimale_sms'],
		     "DatakB": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_maksimale_datakb'],
		 "Komente": form_data['tarifat_roaming_outbound_parapagim_kroaci_tarifat_maksimale_komente']
        }
      },
      "Bosne_dhe_Hercegovine": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_bosna_tarifat_maksimale_komente']
        }
      },
      "Turqi": {
        "tarifat_minimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_turqi_tarifat_maksimale_komente']
        }
      },
      "Gjermani": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_minimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_minimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_minimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_minimale_datakb'],
		#    "Komente": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
        "origjinimi": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_maksimale_origjinimi'],
		     "pranimi": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_maksimale_pranimi'],
		     "SMS": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_maksimale_sms'],
		     "DatakB": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_maksimale_datakb'],
		 "Komente": form_data['tarifat_roaming_outbound_parapagim_gjermani_tarifat_maksimale_komente']
        }
      },
      "Itali": {
        "tarifat_minimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_itali_tarifat_maksimale_komente']
        }
      },
      "France": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_minimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_minimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_minimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_minimale_datakb'],
		#    "Komente": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
		"origjinimi": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_maksimale_origjinimi'],
		     "pranimi": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_maksimale_pranimi'],
		     "SMS": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_maksimale_sms'],
		     "DatakB": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_maksimale_datakb'],
		 "Komente": form_data['tarifat_roaming_outbound_parapagim_france_tarifat_maksimale_komente']
        }
      },
      "Zvicer": {
        "tarifat_minimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_zvicerr_tarifat_maksimale_komente']
        }
      },
      "Mbreteria e Bashkuar": {
        "tarifat_minimale": {
         "origjinimi": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_minimale_origjinimi'],
		      "pranimi": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_minimale_pranimi'],
		      "SMS": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_minimale_sms'],
		      "DatakB": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_minimale_datakb'],
		#   "Komente": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_britani_tarifat_maksimale_komente']
        }
      },
      "SHBA": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_minimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_minimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_minimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_minimale_datakb'],
		#    "Komente": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_shba_tarifat_maksimale_komente']
        }
      },
      "Kanada": {
        "tarifat_minimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_minimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_minimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_minimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_minimale_datakb'],
		#    "Komente": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_minimale_komente']
        },
        "tarifat_maksimale": {
          "origjinimi": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_maksimale_origjinimi'],
		       "pranimi": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_maksimale_pranimi'],
		       "SMS": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_maksimale_sms'],
		       "DatakB": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_maksimale_datakb'],
		   "Komente": form_data['tarifat_roaming_outbound_parapagim_kanada_tarifat_maksimale_komente']
        }
      }
    },

		#ok
    "Tarifat_e_RoamingutOutbond_kontrate": {

	    "Shqiperi": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	          "origjinimi": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_maksimale_origjinimi'],
	      "pranimi": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_maksimale_pranimi'],
	      "SMS": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_maksimale_sms'],
	      "DatakB": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_maksimale_datakb'],
	  "Komente": form_data['tarifat_roaming_outbound_kontrate_shqiperi_tarifat_maksimale_komente']
	      }
	    },
	    "Maqedoni": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_maksimale_origjinimi'],
	       "pranimi": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_maksimale_pranimi'],
	       "SMS": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_maksimale_sms'],
	       "DatakB": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_maksimale_datakb'],
	   "Komente": form_data['tarifat_roaming_outbound_kontrate_maqedoni_tarifat_maksimale_komente']
	      }
	    },

"Malizi": {
  "tarifat_minimale": {
   "origjinimi": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_minimale_origjinimi'],
   "pranimi": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_minimale_pranimi'],
   "SMS": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_minimale_sms'],
   "DatakB": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_minimale_datakb'],
  # "Komente": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_minimale_komente']
   },
   "tarifat_maksimale": {
    "origjinimi": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_maksimale_origjinimi'],
    "pranimi": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_maksimale_pranimi'],
    "SMS": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_maksimale_sms'],
    "DatakB": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_maksimale_datakb'],
  "Komente": form_data['tarifat_roaming_outbound_kontrate_malizi_tarifat_maksimale_komente']
   }
},

	    "Serbi": {
	      "tarifat_minimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_minimale_origjinimi'],
	       "pranimi": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_minimale_pranimi'],
	       "SMS": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_minimale_sms'],
	       "DatakB": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_minimale_datakb'],
	#    "Komente": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_maksimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_maksimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_maksimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_maksimale_datakb'],
	    "Komente": form_data['tarifat_roaming_outbound_kontrate_serbi_tarifat_maksimale_komente']
	      }
	    },
	    "Kroaci": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_minimale_komente']
	      },
	      "trifat_maksimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_maksimale_origjinimi'],
	       "pranimi": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_maksimale_pranimi'],
	       "SMS": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_maksimale_sms'],
	       "DatakB": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_maksimale_datakb'],
	   "Komente": form_data['tarifat_roaming_outbound_kontrate_kroaci_tarifat_maksimale_komente']
	      }
	    },
	    "Bosne_dhe_Hercegovine": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_bosna_tarifat_maksimale_komente']
	      }
	    },
	    "Turqi": {
	      "tarifat_minimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_turqi_tarifat_maksimale_komente']
	      }
	    },
	    "Gjermani": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_minimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_minimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_minimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_minimale_datakb'],
	    #  "Komente": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	      "origjinimi": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_maksimale_origjinimi'],
	       "pranimi": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_maksimale_pranimi'],
	       "SMS": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_maksimale_sms'],
	       "DatakB": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_maksimale_datakb'],
	   "Komente": form_data['tarifat_roaming_outbound_kontrate_gjermani_tarifat_maksimale_komente']
	      }
	    },
	    "Itali": {
	      "tarifat_minimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_itali_tarifat_maksimale_komente']
	      }
	    },
	    "France": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_minimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_minimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_minimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_minimale_datakb'],
	    #  "Komente": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	  "origjinimi": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_maksimale_origjinimi'],
	       "pranimi": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_maksimale_pranimi'],
	       "SMS": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_maksimale_sms'],
	       "DatakB": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_maksimale_datakb'],
	   "Komente": form_data['tarifat_roaming_outbound_kontrate_france_tarifat_maksimale_komente']
	      }
	    },
	    "Zvicer": {
	      "tarifat_minimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_zvicerr_tarifat_maksimale_komente']
	      }
	    },
	    "Mbreteria e Bashkuar": {
	      "tarifat_minimale": {
	       "origjinimi": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_minimale_origjinimi'],
	        "pranimi": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_minimale_pranimi'],
	        "SMS": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_minimale_sms'],
	        "DatakB": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_minimale_datakb'],
	    # "Komente": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_britani_tarifat_maksimale_komente']
	      }
	    },
	    "SHBA": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_minimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_minimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_minimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_minimale_datakb'],
	    #  "Komente": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_shba_tarifat_maksimale_komente']
	      }
	    },
	    "Kanada": {
	      "tarifat_minimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_minimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_minimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_minimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_minimale_datakb'],
	    #  "Komente": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_minimale_komente']
	      },
	      "tarifat_maksimale": {
	        "origjinimi": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_maksimale_origjinimi'],
	         "pranimi": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_maksimale_pranimi'],
	         "SMS": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_maksimale_sms'],
	         "DatakB": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_maksimale_datakb'],
	     "Komente": form_data['tarifat_roaming_outbound_kontrate_kanada_tarifat_maksimale_komente']
	      }
	    }

    },

		#ok
    "fitimi_para_tatimit_per_vitin_paraprak": {
      "ebit": {
        "sasia": form_data['fitimi_para_tatimit_vitin_paraprak_ebit_sasia'],
        "komente": form_data['fitimi_para_tatimit_vitin_paraprak_ebit_komenet']
      },
      "ebitda": {
                "sasia": form_data['fitimi_para_tatimit_vitin_paraprak_ebitda_sasia'],
		        "komente": form_data['fitimi_para_tatimit_vitin_paraprak_ebitda_komenet']
      },
      "roce": {
                "sasia": form_data['fitimi_para_tatimit_vitin_paraprak_roce_sasia'],
		        "komente": form_data['fitimi_para_tatimit_vitin_paraprak_roce_komenet']
      },
      "ebitda_margina": {
        "sasia": form_data['fitimi_para_tatimit_vitin_paraprak_ebitda_margina_sasia'],
        "komente": form_data['fitimi_para_tatimit_vitin_paraprak_ebitda_margina_komenet']
      },
      "ebit_margina": {
                "sasia": form_data['fitimi_para_tatimit_vitin_paraprak_ebit_margina_sasia'],
		        "komente": form_data['fitimi_para_tatimit_vitin_paraprak_ebit_margina_komenet']
      }
    },
		#ok
    "te_dhenat_tjera_financiare": {
      "te_ardhurat_e_pergjithshme_nga_sherbimet_telekomunikuese": {
        "te hyrat ne 000s": form_data['dhenat_tjera_financiar_ardhurat_pergjithshme_thyrat'],
        "komente": form_data['dhenat_tjera_financiar_ardhurat_pergjithshme_komente']
      },
      "te_ardhurat_mes_per_perdorues": {
        "te hyrat ne 000s": form_data['dhenat_tjera_financiar_ardhurat_perdorues_thyrat'],
        "komente": form_data['dhenat_tjera_financiar_ardhurat_perdorues_komente']
      },
      "minutat_e_perdorimit": {
        "te hyrat ne 000s": form_data['dhenat_tjera_financiar_minutat_perdorimit_thyrat'],
        "komente": form_data['dhenat_tjera_financiar_minutat_perdorimit_komente']
      },
      "te_ardhurat_per_minute": {
        "te hyrat ne 000s": form_data['dhenat_tjera_financiar_ardhurat_minute_thyrat'],
        "komente": form_data['dhenat_tjera_financiar_ardhurat_minute_komente']
      },
      "CCPU": {
        "te hyrat ne 000s": form_data['dhenat_tjera_financiar_ccpu_thyrat'],
        "komente": form_data['dhenat_tjera_financiar_ardhurat_ccpu_komente']
      },
      "investimet_shpenzimet_totale": {
        "invest_sherb_infrasrrukt_telekom": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_shpenzimet_totale_infras_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_shpenzimet_totale_infras_komente']
        },
        "investime_rrjeti_backbone": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_rrjeti_backbone_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_rrjeti_backbone_komente']
        },
        "investime_rrjetin_eqasjes": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_rrjeti_qasjes_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_rrjeti_qasjes_komente']
        },
        "inv_sherb_telekom": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_sherbimet_telekom_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_sherbimet_telekom_komente']
        },
        "shpenzimet_nemarketing": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_shpenzimet_marketing_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_shpenzimet_marketing_komente']
        },
        "shpenzime_tjera": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_investimet_shpenzimet_tjera_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_investimet_shpenzimet_tjera_komente']
        }
      },
      "shvleftesimi_amortizimi": {
        "shvleftesimi": {
          "te hyrat ne 000s": form_data['dhenat_tjera_financiar_shvletf_amort_shvleftesimi_thyrat'],
          "komente": form_data['dhenat_tjera_financiar_shvletf_amort_shvleftesimi_komente']
        },
        "amortizimi": {
         "te hyrat ne 000s": form_data['dhenat_tjera_financiar_shvletf_amort_amortizimi_thyrat'],
		 "komente": form_data['dhenat_tjera_financiar_shvletf_amort_amortizimi_komente']
        }
      }
		},

		"Marreveshje_interkoneksionit":{
			"operatori1":{
			"emri": form_data['marreveshja_interkoneksionit_opertaori_1_emri'],
			"data_marreveshjes": form_data['marreveshja_interkoneksionit_opertaori_1_data_marreveshjes'],
			"nr_pika_interkoneksionit": form_data['marreveshja_interkoneksionit_opertaori_1_nr_pika'],
			"komente": form_data['marreveshja_interkoneksionit_opertaori_1_komente']

			}

		},
		"Te_dhenat_mbi_puntorin":{
      "Puntoret_me_orar_te_plote": {
        "Sasi": {
          "Meshkuj": form_data['dhena_mbi_puntor_orar_plote_mashkuj'],
          "Femra": form_data['dhena_mbi_puntor_orar_plote_femra']
				},
        "Komente": form_data['dhena_mbi_puntor_orar_plote_koment']

      },
      "Puntoret_me_orar_te_pjeseshem": {
        "Sasi": {
          "MESHKUJ": form_data['dhena_mbi_puntor_orar_pjes_mashkuj'],
          "femra": form_data['dhena_mbi_puntor_orar_pjes_femra']
				},
          "Komente": form_data['dhena_mbi_puntor_orar_pjes_komente']

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

@mod_main.route('/remove/<string:remove_id>', methods=['POST'])
def remove(remove_id):
    db = mongo.db.arkep
    remove = db.remove({"_id" : ObjectId(remove_id)})
    if remove['n'] == 1:
        return Response(response=dumps({"removed": True}),
        status=200,
        mimetype='application/json')
    else:
        return Response(response=dumps({"removed": False}),
        status=500,
        mimetype='application/json')

@mod_main.route('/raporti/<string:report_id>')
def raporti(report_id):
	db = mongo.db.arkep
	report = db.find_one({ "_id" : ObjectId(report_id) })
	return render_template('raporti.html',report=report)
