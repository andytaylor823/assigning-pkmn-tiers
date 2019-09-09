import pandas as pd
import numpy as np
from sklearn import svm
import random
from sklearn import linear_model
from sklearn import neighbors
import matplotlib.pyplot as plt

# create dictionaries to go from number <-> type and tier -> number
random.seed(7089278395)
types = ['Steel', 'Fairy', 'Dragon', 'Bug', 'Electric', 'Fire', 'Grass', 'Rock', 'Dark', 'Flying', 'Ground', 'Poison', 'Normal', 'Fighting', 'Ghost', 'Ice', 'Psychic', 'Water']
dtypes = {types[i]:i for i in range(len(types))}
tiers = ['CAP', 'LC', 'Untiered', 'PU', 'PUBL', 'NU', 'NUBL', 'RU', 'RUBL', 'UU', 'UUBL', 'OU', 'Uber', 'AG']
dtiers = {tiers[i]:(10*(i-2)) for i in range(len(tiers))}
num_to_tier = {(10*(i-2)):tiers[i] for i in range(len(tiers))}

# read in the data
df = pd.read_csv('pokemonstats.csv')
#for t in ['Untiered', 'PU', 'NU', 'RU', 'UU', 'OU', 'Uber']:
#	print('There are %i Pokemon in %s' %(sum(df['tier']==dtiers[t]), t))
#print('------------------------')

# clean out certain parts of the data
df = df.loc[df['tier'] >= 0]			# excludes CAP and LC
df = df.loc[df['is_nfe'] == 0]			# excludes NFE mons
df = df.loc[df['tier'] > 0]			# excludes Untiered mons

# the names of the pokemon
names = np.array(df['name'])

# turn the data into a NumPy array and separate into training and testing
data = np.array(df)
train_idxs = np.array(random.sample(range(len(data)), int(0.9*len(data))))	# train on 90 % of the data
test_idxs  = np.array([i for i in range(len(data)) if i not in train_idxs])

train_X = np.array(data[train_idxs, 1:-1], dtype = float)
train_y = np.array(data[train_idxs, -1], dtype = float)
test_X = np.array(data[test_idxs, 1:-1], dtype = float)
test_y = np.array(data[test_idxs, -1], dtype = float)

# uncomment these lines to only include certain parts of the data
# only use BST
#train_X, test_X = [arr[:,:6] for arr in [train_X, test_X]]

# only use atk, spa, spe
#train_X, test_X = [arr[:,[1, 3, 5]] for arr in [train_X, test_X]]

# use 4 different fitting models to compare accuracy
x = 2638952
models = [svm.LinearSVC(random_state=x, max_iter=1e5), 
	  linear_model.Lasso(random_state=x, alpha=0.1), 
	  neighbors.KNeighborsClassifier(n_neighbors=5, weights='distance'),
	  svm.SVR(kernel='linear')]
titles = ['Linear Classification', 'Lasso Regression', 'K-Neighbors Classification', 'Linear Regression']

# train & test the models
# plot the deviations from the correct values of each model
fig = plt.figure()
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel('Error', fontsize = 16)
plt.ylabel('Density', fontsize = 16)
for i in range(len(titles)):
	ax = fig.add_subplot(2, 2, i+1)
	clf = models[i]
	clf.fit(train_X, train_y)
	predict_y = clf.predict(test_X)
	diff = test_y - predict_y
	ax.hist(diff, histtype = 'step', bins = 15, density=True)#, label = titles[i])
	ax.set_title(titles[i])

	closeness = 20
	nright = sum(abs(predict_y-test_y)<=closeness)
	print('%s predicted with %.1f percent accuracy' %(titles[i], nright/len(predict_y)*100))

plt.tight_layout()
plt.show()
