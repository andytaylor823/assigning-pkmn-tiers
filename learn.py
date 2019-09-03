import pandas as pd
import numpy as np
from sklearn import svm		# bruce did this and used svm.SVC()
from sklearn import naive_bayes
import random
from sklearn.metrics import mean_absolute_error as mae
from sklearn import linear_model
from sklearn import neighbors

#random.seed(1638591)
random.seed(7089278395)
types = ['Steel', 'Fairy', 'Dragon', 'Bug', 'Electric', 'Fire', 'Grass', 'Rock', 'Dark', 'Flying', 'Ground', 'Poison', 'Normal', 'Fighting', 'Ghost', 'Ice', 'Psychic', 'Water']
dtypes = {types[i]:i for i in range(len(types))}
tiers = ['CAP', 'LC', 'Untiered', 'PU', 'PUBL', 'NU', 'NUBL', 'RU', 'RUBL', 'UU', 'UUBL', 'OU', 'Uber', 'AG']
dtiers = {tiers[i]:(10*(i-2)) for i in range(len(tiers))}
num_to_tier = {(10*(i-2)):tiers[i] for i in range(len(tiers))}


df = pd.read_csv('pokemonstats.csv')
#for t in ['Untiered', 'PU', 'NU', 'RU', 'UU', 'OU', 'Uber']:
#	print('There are %i Pokemon in %s' %(sum(df['tier']==dtiers[t]), t))
#print('------------------------')
df = df.loc[df['tier'] >= 0]			# excludes CAP and LC
df = df.loc[df['is_nfe'] == 0]			# excludes NFE mons
df = df.loc[df['tier'] > 0]			# excludes Untiered mons

names = np.array(df['name'])

# after cleaning the data...
data = np.array(df)
train_idxs = np.array(random.sample(range(len(data)), int(0.9*len(data))))	# train on 90 % of the data
test_idxs  = np.array([i for i in range(len(data)) if i not in train_idxs])

train_X = np.array(data[train_idxs, 1:-1], dtype = float)
train_y = np.array(data[train_idxs, -1], dtype = float)
test_X = np.array(data[test_idxs, 1:-1], dtype = float)
test_y = np.array(data[test_idxs, -1], dtype = float)

# only use BST
#train_X, test_X = [arr[:,:6] for arr in [train_X, test_X]]

# only use atk, spa, spe
#train_X, test_X = [arr[:,[1, 3, 5]] for arr in [train_X, test_X]]


#clf = svm.SVC()
#clf = svm.LinearSVC(random_state=173950)
clf = linear_model.Lasso(alpha = 0.1)		# this is pretty decent
#clf = neighbors.KNeighborsClassifier(n_neighbors=10, weights='distance')	# this isn't that great
#clf = linear_model.SGDRegressor(random_state = 279024)		# this is only good with huge datasets
clf.fit(train_X, train_y)
predict_y = clf.predict(test_X)


closeness = 20
nright = sum(abs(test_y - predict_y) < closeness)
print('This was %.1f percent right' %(nright/len(test_y)*100))
print('Trained on', len(train_y), 'data points')
print('Tested on ', len(test_y), ' data points')
print('MAE = %.1f' %mae(test_y, predict_y))

for i in range(len(test_y)):

	py = predict_y[i]
	ty = test_y[i]
	# check if they're farther away +/- some amount of the right value
	if abs(py - ty) > closeness:
#		true_tier = num_to_tier[ty]
#		predict_tier = num_to_tier[py]
		name = names[test_idxs[i]]
#		print(names[test_idxs[i]], ' has a true tier of ', true_tier, ' but the ML says it was in ', predict_tier)

		line = name
		for k in range(3, len(name)//8, -1):	line += '\t'
		line += '\t%.1f\t%.1f'
		print(line %(ty, py))
#		print('%s\t%.1f\t%.1f' %(name, ty, py))
#		print(name, '\t', ty, '\t', py)








