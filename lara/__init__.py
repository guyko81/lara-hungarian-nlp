# -*- coding: UTF-8 -*-

# Lara - Lingusitic Aim Recognizer API

__all__				= 'nlp','parser','stemmer','entities'
__version__ 		= '1.2.2'
__version_info__	= tuple(int(num) for num in __version__.split('.'))

import lara.nlp
import lara.parser
import lara.stemmer
import lara.entities
