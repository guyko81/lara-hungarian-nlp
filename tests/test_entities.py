# -*- coding: UTF-8 -*-

import pytest
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','inc','exc','score','clean_score','match_stem','ignorecase','boundary','max_words'])
valid_class = set(['noun','verb','adjective','regex','emoji','special'])
is_regex	= set(['|','(',')','+','*','+','?','\\','[',']','{','}'])
accents		= set(['á','Á','é','É','í','Í','ü','Ü','ű','Ű','ú','Ú','ö','Ö','ő','Ő','ó','Ó'])
	
def validate_intent(intents):
	for intent,declaration in intents.items():
		for char in intent:
			if char in accents:
				print(intent,"key has accents in declaration")
				break
		for item in declaration:				
			validate_intent_item(item,intent)
			if 'inc' in item:
				for sub_item in item['inc']:
					validate_intent_item(sub_item,intent)
			if 'exc' in item:
				for sub_item in item['exc']:
					validate_intent_item(sub_item,intent)	
			
def validate_intent_item(item,intent):
	for key in item:
		if key not in valid_keys:
			print(intent,'has unknown key:',key)
	if 'wordclass' in item:
		if item['wordclass'] not in valid_class:
			print(intent,'has invalid "wordclass" declared')
	if 'affix' in item:
		if not isinstance(item['affix'], list) and not isinstance(item['affix'], tuple):
			print(intent,'has "affix" declared, but not as a list:',item['stem'])
	if 'prefix' in item:
		if not isinstance(item['prefix'], list) and not isinstance(item['prefix'], tuple):
			print(intent,'has "prefix" declared, but not as a list:',item['stem'])
	if 'stem' not in item:
		print(intent,'missing "stem" key')
	else:
		if '\b' in item['stem'] and ('boundary' not in item or item['boundary']):
			print(intent,'has bounary set but has \\b declared as regular expression')
		if 'wordclass' in item and item['wordclass']=='regex':
			switch	= False
			last		= ''
			for char in item['stem']:
				if char=='[':
					switch	= True
				elif char==']':
					switch	= False
				elif char in accents:
					if not switch:
						print(intent,'has accents declared in regular expression without counterparts:',item['stem'])
						break
				elif char.isalpha() and char==last:
						print(intent,'has double letters in regular expression:',item['stem'])
						break
				if last=='\\':
					last	= last+char
				else:
					last	= char
		elif 'wordclass' in item and item['wordclass']=='regex':
			really	= False
			for char in item['stem']:
				if not char.isalnum() and char not in (' ','-'):
					really	= True
					break
			if not really:
				print(intent,'probably has a regex "wordclass" declared by accident in',item['stem'])
		if any(test in item['stem'] for test in is_regex):
			if 'wordclass' not in item or item['wordclass']!='regex':
				print(intent,'probably has a regex "wordclass" declared otherwise in',item['stem'])
							
@pytest.mark.parametrize("entity", [
    "common","commands","counties","dow","smalltalk","emoji","disallow","tone"
])
def test_entities(entity):
	parenthesis_check = eval('parser.Intents(entities.'+entity+'()).match_set("test")')
	eval('validate_intent(entities.'+entity+'())')
	
	
	
valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','inc','exc','score','clean_score','match_stem','ignorecase','boundary','max_words'])
valid_class = set(['noun','verb','adjective','regex','emoji','special'])
is_regex	= set(['|','(',')','+','*','+','?','\\','[',']','{','}'])
accents		= set(['á','Á','é','É','í','Í','ü','Ü','ű','Ű','ú','Ú','ö','Ö','ő','Ő','ó','Ó'])
				