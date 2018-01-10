**Lara** is a lightweight Python3 NLP library for Chatbot AI developement in Hungarian language. Instead of developing an all purpose NLTK library, **Lara** was created to fit the quirks and uniqueness of the Hungarian (online) language as much as possible.

The library is capable of matching inflected forms of keywords in text messages written in Hungarian. It also comes with a collection of common NLP functions for text processing, and can even identify common expressions and small talk topics in discussions.

# Table of contents

1. [About Lara](#about-lara)
	1. [Find intents](#find-intents)
	2. [Extract information](#extract-information)
	3. [Handle common topics](#handle-common-topics)
	4. [Create ML features](#ecreate-ml-features)
	5. [And much more](#and-much-more)
2. [Misc.](#misc)

## About Lara

Here is a short list of things you can easily do with **Lara** in Hungarian. For documentation and examples, check out [the Wiki](https://github.com/sedthh/lara-hungarian-nlp/wiki).

#### Find intents

**Lara** is perfect for developing chatbots in Hungarian language, where certain keywords would trigger certain answers. The Class will allow developers to easly match almost every possible inflected forms of any keyword in Hungarian language. For example:

```python
from lara import parser

ragozott_forma	= {
	"to_do"		: [{"stem":"csinál","wordclass":"verb"}],
}
ragozott_talalat= parser.Intents(ragozott_forma)
```

Will match the intent `"to_do"` in the following sentences:
- Ő mit **csinál** a szobában?
- Mit fogok még **csinálni**?
- Mikor **csináltad** meg a szekrényt?
- **Megcsináltatták** a berendezést.
- Teljesen **kicsinálva** érzem magamat ettől a melegtől.
- **Csinálhatott** volna mást is.
- **Visszacsinalnad** az ekezeteket a billentyuzetemen, kerlek?

All you have to do is set the `wordclass` and `stem` of a keyword, and **Lara** will do the rest for you, without the having to rely on large dictionaries!

```python
from lara import parser

alma_intents	= {
	"alma"		: [{"stem":"alma","wordclass":"noun"}],
	"szed"		: [{"stem":"szed","wordclass":"verb"}],
	"piros"		: [{"stem":"piros","wordclass":"adjective"}]
}
alma_test		= parser.Intents(alma_intents)
print(alma_test.match("Mikor szedjük le a pirosabb almákat?"))

>>> {'alma': 1, 'szed': 2, 'piros': 2}
```

#### Extract information

It allows simple text processing:

```python
from lara import parser

tweet		= 'A robotok elveszik a munkát! #NLP #Chatbot'
hashtags	= parser.Extract(tweet).hashtags()

print(hashtags)
>>> ["#NLP","#Chatbot"]
```

#### Handle common topics

Understands when the user is just trying to mess with your Chatbot, instead of actually sending a request:

```python
from lara import parser, entities

user_text	= 'Hasta la vista baby!'

references	= entities.popculture()
references_match= parser.Intents(references).match_set(user_text)
if references_match:
	print('Értem, egy másik AI-ra utaltál az üzenetedben.')
	if 'terminator' in references_match:
		print('Visszatérek!')
else:
	print('Ez egy valós üzenetnek tűnik!')
		
>>> Értem, egy másik AI-ra utaltál az üzenetedben.
>>> Visszatérek!
```

#### Create ML features

Creates features from short Hungarian texts for Machine Learning models:

```python
from lara import tippmix, nlp

text 	= '''
	A szövegbányászat a strukturálatlan vagy kis mértékben strukturált 
	szöveges állományokból történő ismeret kinyerésének tudománya; 
	olyan különböző dokumentumforrásokból származó szöveges ismeretek
	és információk gépi intelligenciával történő kigyűjtése és 
	reprezentációja, amely a feldolgozás előtt rejtve és feltáratlanul 
	maradt az elemző előtt. 
	'''

text	= nlp.remove_stopwords(text)
stems	= tippmix.stemmer(text)
bigrams = nlp.ngram(stems,2)
print(bigrams)

>>> ['szövegbányász strukturál', 'strukturál kis', 'kis mér', 'mér strukturál', 'strukturál szöveg', 'szöveg állományok', ... 'mar elemz']

```

#### And much more

```python
from lara import nlp

huszt	= [
	'Bús düledékeiden, Husztnak romvára megállék;',
	'Csend vala, felleg alól szállt fel az éjjeli hold.',
	]

for line in husz:
	print(nlp.metre(line))
	
>>> ['-', 'u', 'u', '-', 'u', 'u', '-', '-', '-', '-', '-', 'u', 'u', '-', '-']
>>> ['-', 'u', 'u', '-', 'u', 'u', '-', '-', 'u', 'u', '-', 'u', 'u', '-']
```

## Misc.

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details. Feel free to use it in your own AI solutions, as

![Every civilization was built off the back of a disposable workforce... But I can only make so many.](https://github.com/sedthh/lara-hungarian-nlp/blob/master/bladerunner.gif)

Initial work by **[Richard Nagyfi](https://github.com/sedthh)**, 2016. Special thanks to [Peter Varo](https://github.com/petervaro).

Created in collaboration with [Kitchen Budapest](http://kibu.hu) and the [Institute of Advanced Studies, Kőszeg](http://iask.hu/).
