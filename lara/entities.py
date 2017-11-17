# -*- coding: UTF-8 -*-

# common intents
def common():
	return {
		"yes"				: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay"]}],
		"no"				: [{"stem":"nem"},{"stem":"ne"},{"stem":"soha"},{"stem":"mégse","affix":["m"]}],
		"hi" 				: [{"stem":"hi","match_at":"start"},{"stem":"hai","match_at":"start"},{"stem":"szia","match_at":"start","affix":["sztok"]},{"stem":"helló","match_at":"start","affix":["ka"]},{"stem":"szervusz","match_at":"start"},{"stem":"szerbusz","match_at":"start"},{"stem":"szevasz","match_at":"start"},{"stem":"hali","match_at":"start","affix":["hó"]},{"stem":"j[oó]\s?(reggelt|napot|est[eé]t)","wordclass":"regex"}],
		"bye" 				: [{"stem":"bye","match_at":"end"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]},{"stem":"jóéjt"},{"stem":"jóccakát"},{"stem":"mennem kell"}],
		"thx"				: [{"stem":"kösz","affix":["i","önöm","önjük","önet","ike","csi"]},{"stem":"kössz"},{"stem":"kösszentyű"},{"stem":"thx"},{"stem":"thanks?","wordclass":"regex"}],
		"pls"				: [{"stem":"p+l+[iíea]*[zs]+e*","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex"},{"stem":"(meg)?kér(het)?([ln]?[eéi][km]?)","wordclass":"regex"},{"stem":"szeretné([km]|lek)","wordclass":"regex"}],
		"command"			: [{"stem":"keres(s|d)","wordclass":"regex"},{"stem":"mutass(s|d)","wordclass":"regex"},{"stem":"mond(j|d)","wordclass":"regex"},{"stem":"néz(né|ze)?d","wordclass":"regex"},{"stem":"akaro(k|m)","wordclass":"regex"},{"stem":"utas[ií]t\w{1,}","wordclass":"regex"}],
		"question"			: [{"stem":"\?+($|\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki","affix":["t","k","ket","nek","knek","től","ktől","ből","kből","hez","re","kre","vel","kkel"]}],
		"conditional"		: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}],
		"profanity"			: [{"stem":"(fel|le|meg|rá|ki|be|oda|össze|bele|hozzá)?bas*z+(at)?(hat)?(us|a[dk]?|á[kl]|[aá]?t[aáo][lkm]?|ott|ni|n[aá]n?[dlkm]?|va|meg)?","wordclass":"regex"},{"stem":"fasz","prefix":["ló"],"wordclass":"noun"},{"stem":"fasza","wordclass":"adjective"},{"stem":"geci","wordclass":"noun"},{"stem":"kurva","affix":["élet"],"wordclass":"noun"},{"stem":"hülye","wordclass":"adjective"},{"stem":"pi(n|cs)[aá][dk]?(a?t|nak|ban?|[bt][oó]l|[eé]rt)?","wordclass":"regex"},{"stem":"((bekap(ja?|hato?|n[aái])?d?)|(kap.*be))","wordclass":"regex"}]
	}

# menu commands
def commands():
	return {
		"ok"				: [{"stem":"ye","affix":["s","ah","p"]},{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay","ézd"]},{"stem":"úgy"},{"stem":"így"},{"stem":"jó","wordclass":"adjective"}],
		"cancel"			: [{"stem":"no","affix":["ne","pe"]},{"stem":"cancel"},{"stem":"ne","affix":["m"]},{"stem":"mégse","affix":["m"]},{"stem":"elvetés"},{"stem":"ál","affix":["lít"],"wordclass":"verb"}],
		"next"				: [{"stem":"next"},{"stem":"tovább"},{"stem":"előre"},{"stem":"még","wordclass":"regex"},{"stem":"more"},{"stem":"continue"},{"stem":"folytat","wordclass":"verb"},{"stem":"folyta[st]+([ao]?d|ni|ás)?","wordclass":"regex"}],
		"back"				: [{"stem":"back"},{"stem":"vissza","affix":["lép","lépés"]},{"stem":"hátra"}],
		"save"				: [{"stem":"save"},{"stem":"ment","wordclass":"verb"},{"stem":"mentés","wordclass":"noun"}],
		"open"				: [{"stem":"open"},{"stem":"nyit","wordclass":"verb"},{"stem":"nyis","match_stem":False,"wordclass":"verb"}],
		"delete"			: [{"stem":"del","affix":["ete"]},{"stem":"töröl","wordclass":"verb"},{"stem":"törlés"}],
		"exit"				: [{"stem":"exit"},{"stem":"quit"},{"stem":"esc","affix":["ape"]},{"stem":"kilép","wordclass":"verb"},{"stem":"l[eé]pj?([eé][dln])?.+ki","wordclass":"regex"}],
		"options"			: [{"stem":"options"},{"stem":"beállít","wordclass":"verb"},{"stem":"[aá]ll[ií]ts.+be","wordclass":"regex"}],
		"menu"				: [{"stem":"menü","prefix":["main","fő","al","legördülő"],"wordclass":"noun"}],
		"login"				: [{"stem":"login"},{"stem":"log in"},{"stem":"belép","prefix":[],"wordclass":"verb"},{"stem":"bejelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+be","wordclass":"regex"},{"stem":"jelentkez.+be","wordclass":"regex"}],
		"logout"			: [{"stem":"logout"},{"stem":"log out"},{"stem":"kilép","prefix":[],"wordclass":"verb"},{"stem":"kijelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+ki","wordclass":"regex"},{"stem":"jelentkez.+ki","wordclass":"regex"}]
	}
	
# hungarian counties and county seats
def counties():
	return {
		"bacs-kiskun"		: [{"stem":"Bács-Kiskun","wordclass":"noun"},{"stem":"Kecskemét","wordclass":"noun"}],
		"baranya"			: [{"stem":"Baranya","wordclass":"noun"},{"stem":"Pécs","affix":["ett"],"wordclass":"noun"}],
		"bekes"				: [{"stem":"Békés","wordclass":"noun"},{"stem":"Békéscsaba","wordclass":"noun"}],
		"borsod-abauj-zemplen": [{"stem":"Borsod","affix":["-Abaúj-Zemplén"],"wordclass":"noun"},{"stem":"Zemplén","wordclass":"noun"},{"stem":"BAZ","ignorecase":False}],
		"csongrad"			: [{"stem":"Csongrád","wordclass":"noun"},{"stem":"Szeged","wordclass":"noun"}],
		"fejer"				: [{"stem":"Fejér","wordclass":"noun"},{"stem":"Fehérvár","prefix":["Székes"],"wordclass":"noun"}],
		"gyor-moson-sopron"	: [{"stem":"Győr","affix":["-Moson-Sopron"],"wordclass":"noun"},{"stem":"Sopron","wordclass":"noun"}],
		"hajdu-bihar"		: [{"stem":"Hajdú-Bihar","wordclass":"noun"},{"stem":"Debrecen","wordclass":"noun"}],
		"heves"				: [{"stem":"Heves","wordclass":"noun"},{"stem":"Eger","wordclass":"noun"},{"stem":"egri"}],
		"jasz-nagykun-szolnok": [{"stem":"Szolnok","wordclass":"noun","prefix":["Jász-Nagykun-"]}],
		"komarom-esztergom"	: [{"stem":"Esztergom","wordclass":"noun","prefix":["Komárom-"]},{"stem":"Komárom","wordclass":"noun"},{"stem":"Tata","affix":["bánya"],"wordclass":"noun"}],
		"nograd"			: [{"stem":"Nógrád","wordclass":"noun"},{"stem":"Salgótarján","wordclass":"noun"}],
		"pest"				: [{"stem":"Buda","wordclass":"noun","affix":["pest"]},{"stem":"Pest","wordclass":"noun"},{"stem":"[IVX]+.?(-?ik)?\sker([uü]let)?\w{0,3}","wordclass":"regex"}],
		"somogy"			: [{"stem":"Somogy","wordclass":"noun"},{"stem":"Kaposvár","wordclass":"noun"}],
		"szabolcs-szatmar-bereg": [{"stem":"Szabolcs","wordclass":"noun","affix":["-Szatmár-Bereg"]},{"stem":"Szatmár","wordclass":"noun"},{"stem":"Nyíregyháza","wordclass":"noun"}],"somogy"			: [{"stem":"Somogy","wordclass":"noun"},{"stem":"Kaposvár","wordclass":"noun"}],
		"tolna"				: [{"stem":"Tolna","wordclass":"noun"},{"stem":"Szekszárd","wordclass":"noun"}],
		"vas"				: [{"stem":"Vas","wordclass":"noun"},{"stem":"Szombathely","wordclass":"noun"}],
		"veszprem"			: [{"stem":"Veszprém","wordclass":"noun"}],
		"zala"				: [{"stem":"Zala","wordclass":"noun","affix":["egerszeg"]}]
	}

# days of the week
def dow():
	return {
		"hetfo"				: [{"stem":"hétfő","wordclass":"noun"}],
		"kedd"				: [{"stem":"kedd","wordclass":"noun"}],
		"szerda"			: [{"stem":"szerda","wordclass":"noun"}],
		"csutortok"			: [{"stem":"csütörtök","wordclass":"noun"}],
		"pentek"			: [{"stem":"péntek","wordclass":"noun"}],
		"szombat"			: [{"stem":"szombat","wordclass":"noun"},{"stem":"szonbat","wordclass":"noun"}],
		"vasarnap"			: [{"stem":"vasárnap","wordclass":"noun"}],
		"hetkoznap"			: [{"stem":"hétköznap","wordclass":"noun"},{"stem":"hétfő","wordclass":"noun"},{"stem":"kedd","wordclass":"noun"},{"stem":"szerda","wordclass":"noun"},{"stem":"csütörtök","wordclass":"noun"},{"stem":"péntek","wordclass":"noun"}],		
		"hetvege"			: [{"stem":"hétvége","wordclass":"noun"},{"stem":"szombat","wordclass":"noun"},{"stem":"szonbat","wordclass":"noun"},{"stem":"vasárnap","wordclass":"noun"}]
	}