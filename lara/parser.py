# -*- coding: UTF-8 -*-

import re
import json

import lara.nlp

class Intents:
		
	# STATIC REGULAR EXPRESSIONS
	prefixes			= r'(?:'+('|'.join(["abba","alá","át","be","bele","benn","el","ellen","elő","fel","föl","hátra","hozzá","ide","ki","körül","le","meg","mellé","neki","oda","össze","rá","szét","túl","utána","vissza"]))+')?'
	typo_prefixes		= r'(?:'+('|'.join(["aba","ala","at","be","bele","ben","el","elen","elo","fel","fol","hatra","hoza","ide","ki","korul","le","meg","mele","neki","oda","osze","ra","szet","tul","utana","visza"]))+')?'
	pattern_noun		= r'{1,2}a?i?n?(?:[aáeéioóöőuúü]?[djknmrst])?(?:[abjhkntv]?[aáeéioóöőuúü]?[lgkntz]?)?(?:[ae][kt])?'
	typo_pattern_noun	= r'{1,2}a?i?n?(?:[aeiou]?[djknmrst])?(?:[abjhkntv]?[aeiou]?[lgkntz]?)?(?:[ae][kt])?'
	pattern_adj			= r'(?:[aeoóöő]?s)?(?:[aáeé]?b*)(?:[ae]?[nk])?(?:(?:[aáeéioóöőuúü]?[dklmnt])?(?:[aáeéioóöőuúü]?[klnt]?)?)'
	typo_pattern_adj	= r'(?:[aeo]?s)?(?:[ae]?b?)(?:[ae]?[nk])?(?:(?:[aeiou]?[dklmnt])?(?:[aeiou]?[klnt]?)?)'
	pattern_verb		= r'{1,2}(?:h[ae][st])?(?:[eaá]?s{0,2}d?)?(?:(?:[jntv]|[eo]?g[ae]t+)?(?:[aeioöuü]n?[dklmt]|n[aáeéi]k?|sz|[aái])?(?:t[aáeéou][dkmt]?(?:ok)?)?)?(?:(?:t[ae]t)?(?:h[ae]t(?:[jnt]?[aáeéou](?:[dkm]|t[eéo]k)?)?t*)|ni)?'
	typo_pattern_verb	= r'{1,2}(?:h[ae][st])?(?:[eaá]?s{0,2}d?)?(?:(?:[jntv]|[eo]?g[ae]t)?(?:[aeiou]n?[dklmt]|n[aei]k?|sz|[ai])?(?:t[aeou][dkmt]?(?:ok)?)?)?(?:(?:t[ae]t)?(?:h[ae]t(?:[jnt]?[aeou](?:[dkm]|t[eo]k)?)?t?)|ni)?'
	
	##### CONSTRUCTOR #####
	def __init__(self, new_intents={}, is_raw=False):		
		self.intents	= {}
		if new_intents:
			if is_raw:
				self.raw(new_intents)
			else:
				self.add(new_intents)

	##### DATA MODEL #####
	def __repr__(self):
		return "<Lara Intents Parser instance at {0}>".format(hex(id(self)))
		
	def __str__(self):
		return json.dumps(self.intents)

	def __len__(self):		
		return len(self.intents.keys())
	
	def __eq__(self, other):
		if self.__class__.__name__ == other.__class__.__name__:
			return (self.intents==other.intents)
		elif isinstance(other, bool):
			return (len(self.intents)!=0)==other
		return False
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __add__(self, other):
		if other:
			tmp = Intents(self.intents)
			if self.__class__.__name__ == other.__class__.__name__:
				tmp.add(other.intents)
			elif isinstance(other,dict):
				tmp.add(other)
			return tmp
		return self
	
	##### CLASS FUNCTIONS #####
				
	# Add dict of intents
	def add(self, new_intents={}):
		for key, value in new_intents.items():
			if key not in self.intents:
				self.intents[key]	= []
			for item in new_intents[key]:
				if item not in self.intents[key]:
					item	= self._generate(item)
					if item not in self.intents[key]:
						self.intents[key].append(item)
	
	# Add (previously cached) raw intents without further optimization
	def raw(self, new_intents):
		if new_intents:
			if isinstance(new_intents, str):
				new_intents	= json.loads(new_intents)
			elif new_intents.__class__.__name__=='Intents':
				new_intents	= json.loads(str(new_intents))
			if isinstance(new_intents,dict):
				self.intents	= new_intents.copy()
			else:
				raise ValueError('Unsupported value: %s' % (new_intents))
	
	# Add default values and fill in optional parameters for a single intent
	def _generate(self, item):
		if 'stem' not in item:
			raise KeyError('Intent declaration missing compulsory "stem" key.')
		if not item['stem'] or not isinstance(item['stem'], str):
			raise ValueError('Invalid value for "stem".')
		
		if 'wordclass' not in item:
			item['wordclass']		= 'special'
		elif item['wordclass'] not in ('special','noun','verb','adjective','regex','emoji'):
			if item['wordclass']=='ADJ':
				item['wordclass']	= 'adjective'
			elif isinstance(item['wordclass'],str) and item['wordclass'].lower() in ('noun','verb'):
				item['wordclass']	= item['wordclass'].lower()
			else:
				item['wordclass']	= 'special'		
		if 'typo_stem' not in item:
			if item['wordclass'] in ('regex','emoji'):
				item['typo_stem']	= item['stem']
			else:
				item['typo_stem']	= lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(item['stem'])))
		
		if 'prefix' not in item:
			if item['wordclass']	== 'verb':
				item['prefix']		= r''+Intents.prefixes
				item['typo_prefix']	= r''+Intents.typo_prefixes
			elif item['wordclass']	== 'adjective':
				item['prefix']		= r'(?:leg(?:esleg)?)?'
				item['typo_prefix']	= r'(?:leg(?:esleg)?)?'
			else:
				item['prefix']		= r''
				item['typo_prefix']	= r''
		elif not item['prefix']:
			item['prefix']		= r''
			item['typo_prefix']	= r''
		else:
			if 'typo_prefix' not in item:
				if isinstance(item['prefix'],list):
					item['typo_prefix']	= r'(?:'+lara.nlp.strip_accents('|'.join(item['prefix']))+')?'
				else:
					item['typo_prefix']	= r''+lara.nlp.strip_accents(item['prefix'])
			else:
				if isinstance(item['typo_prefix'],list):
					item['typo_prefix']	=  [re.escape(prefix) for prefix in item['typo_prefix']]
					item['typo_prefix']	= r'(?:'+('|'.join(item['typo_prefix']))+')?' #prefix?
				else:
					item['typo_prefix']	= r''+(item['typo_prefix'])
			if isinstance(item['prefix'],list):
				item['prefix']		= r'(?:'+('|'.join(item['prefix']))+')?'
			else:
				item['prefix']		= r''+(item['prefix'])
		
		if 'affix' not in item or not item['affix']:
			item['affix']		= r''
			item['typo_affix']	= r''
		else:
			if 'typo_affix' not in item:
				if isinstance(item['affix'],list):
					item['typo_affix']	= r'(?:'+lara.nlp.strip_accents('|'.join(item['affix']))+')?'
				else:
					item['typo_affix']	= r''+lara.nlp.strip_accents(item['affix'])
			else:
				if isinstance(item['typo_affix'],list):
					item['typo_affix']	=  [re.escape(affix) for affix in item['typo_affix']]
					item['typo_affix']	= r'(?:'+('|'.join(item['typo_affix']))+')?'
				else:
					item['typo_affix']	= r''+(item['typo_affix'])
			if isinstance(item['affix'],list):
				item['affix']		= r'(?:'+('|'.join(item['affix']))+')?'
			else:
				item['affix']		= r''+(item['affix'])
					
		if 'match_stem' not in item:
			item['match_stem']	= True
		if 'ignorecase' not in item:
			item['ignorecase']	= True
		if 'boundary' not in item:
			if item['wordclass']=='emoji':
				item['boundary']	= False
			else:
				item['boundary']	= True
		
		if 'with' in item:
			if 'score' not in item:
				item['score']		= 0
			new_items	= []
			for sub_item in item['with']:
				sub_item	= self._generate(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['with']	= new_items[:]
		else:
			item['with']	= []
			if 'score' not in item:
				item['score']		= 1
		if 'without' in item:
			new_items	= []
			for sub_item in item['without']:
				sub_item	= self._generate(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['without']	= new_items[:]
		else:
			item['without']	= []		
		
		if 'typo_score' not in item:
			item['typo_score']= item['score']
		
		# cache pattern
		if item['wordclass'] in ('regex','emoji'):
			item['pattern']			= r''+item['stem']+item['affix']
			item['typo_pattern']	= r''+item['typo_stem']+item['typo_affix']
		else:
			item['pattern']			= r'(?:'+re.escape(item['stem'])+item['affix']+')'
			scramble				= item['typo_stem']
			if len(scramble)>3:
				typo		= [scramble[1:-1]]
				for i in range(len(scramble)-3):
					typo.append(re.escape(scramble[1:i+1]+scramble[i+2]+scramble[i+1]+scramble[i+3:-1]))
				scramble	= re.escape(scramble[0])+'(?:'+('|'.join(typo))+')'+re.escape(scramble[-1])
			else:
				scramble				= re.escape(scramble)
			scramble	= '[\s\-]?'.join(scramble.split('\ '))
			item['typo_pattern']	= r'(?:'+scramble+item['typo_affix']+')'
			if item['wordclass'] == 'noun':
				item['pattern']			+= Intents.pattern_noun
				item['typo_pattern']	+= Intents.typo_pattern_noun
			elif item['wordclass'] == 'adjective':
				item['pattern']			+= Intents.pattern_adj
				item['typo_pattern']	+= Intents.typo_pattern_adj
			elif item['wordclass'] == 'verb':
				item['pattern']			+= Intents.pattern_verb
				item['typo_pattern']	+= Intents.typo_pattern_verb
				
		item['pattern']			= item['prefix']+item['pattern']	
		item['typo_pattern']	= item['typo_prefix']+item['typo_pattern']
		return item
	
	# Get all matches from text
	def match(self, text=""):
		if text:
			score		= self._get_score(text)
			final_score	= {}
			for key, value in score.items():
				if value:
					final_score[key]=value
			return final_score
		else:
			return {}
	
	# Get set of matches from text
	def match_set(self, text=""):
		if text:
			matches	= self.match(text)
			return set(list(matches.keys()))
		return set([])
	
	# Remove matches from text
	def clean(self, text=""):
		if text:
			return self._get_clean_text(text)
		else:
			return ""
	
	# Returns text without the inflected forms of matched intents
	def _get_clean_text(self, text):
		text		= lara.nlp.trim(text)
		typo_text	= lara.nlp.strip_accents(lara.nlp.remove_double_letters(text))
		fix_text	= text
		if text:
			for key, value in self.intents.items():
				ignore	= False
				for item in self.intents[key]:
					if 'without' in item and len(item['without']):
						for without in item['without']:
							if 'stem' in without and self._match_pattern(text,without)[0]:
								ignore	= True
							elif 'typo_stem' in without and self._match_pattern(typo_text,without,True)[0]:
								ignore	= True
				if not ignore:
					for item in self.intents[key]:
						if 'stem' in item:
							fix_text		= self._match_pattern(fix_text,item,False,True)
						if 'typo_stem' in item:
							fix_text		= self._match_pattern(fix_text,item,True,True)
		return fix_text
			
	# Get score for intents in text
	def _get_score(self, text):
		text		= lara.nlp.trim(text)
		typo_text	= lara.nlp.strip_accents(lara.nlp.remove_double_letters(text))
		score		= {}
		if text:
			for key, value in self.intents.items():
				for item in self.intents[key]:
					found	= False
					if 'stem' in item:
						result		= self._match_pattern(text,item)
						found		= found or result[0]
						if key not in score:
							score[key]	= 0
						score[key]	+= result[1]
					if 'typo_stem' in item:
						result		= self._match_pattern(typo_text,item,True)
						found		= found or result[0]
						if key not in score:
							score[key]	= 0
						score[key]	+= result[1]
					if found and 'with' in item and len(item['with']):
						for sub_item in item['with']:
							if 'stem' in sub_item:
								if key not in score:
									score[key]	= 0
								found	= self._match_pattern(text,sub_item)
								if found[0]:
									score[key]	+=found[1]
							if 'typo_stem' in sub_item:
								if key not in score:
									score[key]	= 0
								found	= self._match_pattern(typo_text,sub_item,True)
								if found[0]:
									score[key]	+=found[1]
					if found and 'without' in item and len(item['without']):
						if key in score and score[key]:
							for sub_item in item['without']:
								if 'stem' in sub_item and self._match_pattern(text,sub_item)[0]:
									score[key]	= 0
								elif 'typo_stem' in sub_item and self._match_pattern(typo_text,sub_item,True)[0]:
									score[key]	= 0
		return score
	
	# Find an intent in text
	def _match_pattern(self, text, item, is_clean=False, delete=False):
		if text:		
			if is_clean:
				select		= 'typo_'
			else:
				select		= ''	
			if item['boundary']:
				boundary	= r'\b'
			else:
				boundary	= r''
				
			if item['wordclass'] in ('regex','emoji'):
				if item['ignorecase']:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary).findall(text)
			else:
				if item['ignorecase']:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary).findall(text)
					
			if matches:
				if delete:
					tmp	= text
					for match in matches:
						if not isinstance(match,str):
							match	= match[0]
						if item['match_stem'] or (item['ignorecase'] and match.lower() != item[select+'stem'].lower()) or (match.lower() != item[select+'stem']):
							tmp	= re.sub(boundary+r'('+re.escape(match)+r')'+boundary, '', tmp, flags=re.IGNORECASE)
					return tmp
				else:	
					if not item['match_stem']:
						stem_matches	= re.compile(boundary+r'('+re.escape(item[select+'stem'])+r')'+boundary,re.IGNORECASE).findall(text)
						if stem_matches:
							if len(matches) <= len(stem_matches):
								return (False, 0)
							return (True,(len(matches)-len(stem_matches))*item[select+'score'])
					return (True,len(matches)*item[select+'score'])
		if delete:
			return text
		return (False,0)
		
	# Get N best matching intents with the highest value
	def match_best(self, text, n=1):
		if text:
			score	= self.match(text)
			if score:
				best_candidates	= sorted(score, key=score.get, reverse=True)
				best_candidates	= best_candidates[:(min(len(best_candidates),n))]
				return {item:score[item] for item in best_candidates}
		return {}
	