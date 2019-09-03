import requests
from lxml import html
import numpy as np

site = 'https://www.smogon.com/dex/sm/pokemon'
page = requests.get(site)
tree = html.fromstring(page.content)
mess = tree.xpath('//text()')		# get all the page info
notrash = mess[7]			# select out the one entry with all the data in it
brokenup = notrash.split('},{')		# split it up somewhat into each individual pkmn

# Abomasnow is the first one, kinda messed up
# enter this by hand
del(brokenup[1010:])			# delete unnecessary data after Sableye-Mega (it's last, for some reason)
del(brokenup[:7])			# delete unnecessary data before Abra

# create an empty dictionary
# this dictionary will return a dictionary of stats and such, and the key is the pkmn name
dict_of_dicts = {}
# all keys are [name, (stats), weight, height, types, abilities, formats, oob (no idea), cap, evos, alts, genfamily]
# cap: is the pokemon part of the CAP project? all should be false
# evos: lists all evolutions of a pokemon
# alts: other possible "names" of the pokemon (mostly just if the Pokemon can Mega
# genfamily: what gens the Pokemon was in
important_keys = ['hp', 'atk', 'def', 'spa', 'spd', 'spe', 'types', 'formats', 'evos']
types = ['Steel', 'Fairy', 'Dragon', 'Bug', 'Electric', 'Fire', 'Grass', 'Rock', 'Dark', 'Flying', 'Ground', 'Poison', 'Normal', 'Fighting', 'Ghost', 'Ice', 'Psychic', 'Water']
dtypes = {types[i]:i for i in range(len(types))}
tiers = ['CAP', 'LC', 'Untiered', 'PU', 'PUBL', 'NU', 'NUBL', 'RU', 'RUBL', 'UU', 'UUBL', 'OU', 'Uber', 'AG']
dtiers = {tiers[i]:(10*(i-2)) for i in range(len(tiers))}
for entry in brokenup:		# loops over each pokemon

	# make each row have the form of a dictionary
	a = entry.split(',')
	b = [a[0]]
	setback = 1
	for i in range(1, len(a)):
		if ':' in a[i]:		b.append(a[i])
		else:
			b[i-setback] += ',' + a[i]
			setback += 1
	
	# by now, each row should have a ':' in it
	# all rows are characters, and the true strings have "" encasing them
	d = {}
	name = ''
	for x in b:	# loops over each key:val pair in the pokemon
		key, *val = x.split(':')

		# clean up the key, perhaps skipping it
		if '"' in key:			key = key.strip('"')
		if key == 'name':		name = val[0].strip('"')
		if key not in important_keys:	continue
		val = val[0]
		
		# if the val has multiple entries, create a proper array
		if '[' in val:
			val = val.strip('[').strip(']').split(',')
			for i in range(len(val)):
				val[i] = val[i].strip('"')
				
		if '"' in val:		val.strip('"')
		if type(val) != list:
			if val.isdigit():	val = float(val)
		
		d[key] = val
	dict_of_dicts[name] = d

# columns of the csv are going to be:
# name, (hp, atk, def, spa, spd, spe), (type1, type2), is_nfe, tier
#   0     1   2    3    4    5    6      7       8       9      10
fout = open('pokemonstats.csv', 'a')

# write first line
fout.write('name,hp,atk,def,spa,spd,spe,type1,type2,is_nfe,tier\n')
# write Abomasnow line
#fout.write('Abomasnow,90.0,92.0,75.0,92.0,85.0,60.0,Grass,Ice,0,PU\n')
fout.write('Abomasnow,90.0,92.0,75.0,92.0,85.0,60.0,6,15,0,10\n')

# write out each pokemon's info
bad_names = ['Floette-Eternal', 'Pikachu-Starter', 'Eevee-Starter', 'Meltan', 'Melmetal']
for name in dict_of_dicts:
	if name in bad_names:	continue
	d = dict_of_dicts[name]
	fout.write(name + ',')
	
	# write all the stats
	for key in important_keys[:6]:
		fout.write(str(d[key]) + ',')
	
	# write out types, write nothing if no second type
	# now writing out just a number that corresponds to a certain type
	types = d['types']
	fout.write(str(dtypes[types[0]]) + ',')
	if len(types) > 2:
		print('AHHHHH WHAT ', name)
		exit(10)
	if len(types) > 1:		fout.write(str(dtypes[types[1]]) + ',')
	else:				fout.write('-1,')

	
	# check if the pokemon has an evo
	if 'evos' not in d.keys():	has_evo = False
	elif len(d['evos']) > 1:	has_evo = True
	elif d['evos'] != ['']:		has_evo = True
	else:				has_evo = False
	
	if has_evo:			fout.write('1,')
	else:				fout.write('0,')

	# write out the tier
	# now just writing out a number that corresponds to a tier -- increases
	if d['formats'][0] == '':	T = 'Untiered'
	elif name == 'Sableye-Mega':	T = 'UUBL'
	else:				T = d['formats'][0]
	fout.write(str(dtiers[T]))
	fout.write('\n')


fout.close()
print('done')






			
			
