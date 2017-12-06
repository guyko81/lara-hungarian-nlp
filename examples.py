# -*- coding: UTF-8 -*-

import lara

if __name__ == "__main__":
	alma_intents	= {
		"alma"			: [{"stem":"alma","wordclass":"noun"}],
		"szed"			: [{"stem":"szed","wordclass":"verb"}],
		"piros"			: [{"stem":"piros","wordclass":"adjective"}]
	}
	alma_test		= lara.parser.Intents(alma_intents)
	print(alma_test.match("Mikor szedjük le a pirosabb almákat?"))
	
	igekoto_intents	= {
		"to_do"			: [{"stem":"csinál","wordclass":"verb"}],
	}
	igekoto_test		= lara.parser.Intents(igekoto_intents)
	
	print(igekoto_test.match("Ő mit csinál a szobában?"))
	print(igekoto_test.match("Mit fogok még csinálni?"))
	print(igekoto_test.match("Mikor csináltad meg a szekrényt?"))
	print(igekoto_test.match("Megcsináltatták a berendezést."))
	print(igekoto_test.match("Teljesen kicsinálva érzem magamat ettől a melegtől."))
	print(igekoto_test.match("Csinálhatott volna mást is."))
	print(igekoto_test.match("Visszacsinalnad az ekezeteket a billentyuzetemen, kerlek?"))

	busz_intents	= {
		"palyaudvar"	: [{"stem":"pályaudvar","wordclass":"noun","prefix":["busz"]}],
		"auto"			: [{"stem":"autó","wordclass":"noun","affix":["busz"]}],
		"szinten_jo"	: [{"stem":"pálya","wordclass":"noun","prefix":["busz"],"affix":["udvar"]}]
	}
	busz_test		= lara.parser.Intents(busz_intents)
	print(busz_test.match("Lassan beérünk az autóval a pályaudvarra."))
	print(busz_test.match("Lassan beérünk az autóbusszal a buszpályaudvarra."))
	
	hasonul_intents	= {
		"enni"		: [{"stem":"esz","wordclass":"verb","match_stem":False},{"stem":"en","wordclass":"verb","match_stem":False}]
	}
	hasonul_test	= lara.parser.Intents(hasonul_intents)
	print(hasonul_test.match("Tőmorfémák: esz, en."))		# nem veszi figyelembe
	print(hasonul_test.match("Eszel valamit?"))
	print(hasonul_test.match("Azt nem lehet megenni."))
	
	egyutt_intents	= {
		"jo_ido"	: [{"stem":"jó","wordclass":"adjective","score":0,
						"with":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}]}]
	}
	egyutt_test		= lara.parser.Intents(egyutt_intents)
	print(egyutt_test.match("Jó."))							# nem veszi figyelembe
	print(egyutt_test.match("Meleg van."))					# nem veszi figyelembe
	print(egyutt_test.match("Milyen az időjárás?"))			# nem veszi figyelembe
	print(egyutt_test.match("Jó meleg van."))
	print(egyutt_test.match("Jó az idő."))
	print(egyutt_test.match("Jó meleg az idő."))			# dupla pont
	print(egyutt_test.match("Jó meleg az időjárás."))		# dupla pont

	kulon_intents	= {
		"jobb_ido"	: [{"stem":"jó","wordclass":"adjective","score":0,
						"with":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}],
						"without":[{"stem":"este","wordclass":"noun"},{"stem":"esté","match_stem":False,"wordclass":"noun"}]}]
	}
	kulon_test		= lara.parser.Intents(kulon_intents)
	print(kulon_test.match("Jó."))							# nem veszi figyelembe
	print(kulon_test.match("Jó meleg az időjárás."))		# dupla pont
	print(kulon_test.match("Jó estét!"))					# nem veszi figyelembe
	print(kulon_test.match("Jó meleg esténk van!"))			# szintén nem veszi figyelembe

	fals_pozitiv	= {
		"megszerel"	: [{"stem":"szerel","wordclass":"verb"}],
		"hibasan"	: [{"stem":"alma","wordclass":"noun"}],
	}
	hibas_test		= lara.parser.Intents(fals_pozitiv)
	print(hibas_test.match("Gyönyörű dolog a szerelem!"))	# elfogadja hibásan
	print(hibas_test.match("Ezt is elfogadja találatként: Almainüdböz"))	# elfogadja hibásan

	match_common	= lara.parser.Intents(lara.entities.common()).match_as_set("Köszönöm szépen!")
	print(match_common)