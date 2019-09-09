# assigning-pkmn-tiers
Attempting to use the power of machine learning to assign Pokemon to Smogon tiers

Competitive Pokemon is a bit of a hobby of mine. I first got interested in Smogon (the hub for all things competitive Pokemon) around when Pokemon Diamond / Pearl / Platinum came out, and I've been involved ever since.

Competitive battlers assign Pokemon to various tiers based on their power level -- anyone who's played Pokemon knows a battle between Mewtwo and a Beedrill is not a fair fight! All Pokemon known up through Pokemon Sun / Moon (as well as their base stats, abilities, types, and tier) may be found on Smogon's website: https://www.smogon.com/dex/sm/pokemon/

There are many factors that battlers consider when deciding what tier a Pokemon belongs in. The Pokemon's base stats are the most significant factor, but the Pokemon's abilities, typing, and movepool also need to be considered. Additionally, a Pokemon may be excellent in all of the above, yet be outclassed by a still better Pokemon, keeping its tier somewhat low.

For this project, I aim to classify a Pokemon into a tier based only on its base stats. This is the largest contribution to its tier placement, and the sample size for this problem is somewhat low, compared to other machine-learning problems. There are only ~380 or so Pokemon which are fully-evolved, competitive Pokemon in some tier, so we have less than 400 data points, and potentially many variables influencing our predicted variable. Thus, we only use a Pokemon's base stats in predicting what tier it belongs in.

----------------------------------------------------------------

TO RUN THIS CODE:

You first must have Python 3 installed. Begin by running the code "create_data.py" to use web-scraping to pull relevant data from the Smogon website above and write it out in a .csv file. Once this file has been created, running the code "learn.py" will read in the data using Pandas, train the machine-learning function on a sample of the known data, and predict on a small (unused) sub-set of the known data. When the new Pokemon games (Sword / Shield) come out, this may be useful to get a first look at what tiers certain Pokemon may fall into.

Over time, the Smogon website above may change, so I am also including the dataset that would have been created if the website never changed.

----------------------------------------------------------------

WHAT THE CODE DOES:

(create_data.py): The program uses web-scraping to pull data from the Pokemon page on Smogon. In contrast to normal web-scraping, the Smogon data is not formatted in such a way as to make web-scraping easy to perform. Instead, much of the beginning of the program is simply cleaning the data to properly assign variables for each Pokemon. All the data are stored in a large dictionary ("dict_of_dicts"), where each key is the name of the Pokemon, and the "value" corresponding to that key is all of the base stats and data for that Pokemon. Inside that particular dictionary are keys corresponding to relevant data for each Pokemon (such as base hp, atk, def, etc., as well as typing, if it is fully-evolved, and others). After "dict_of_dicts" is created, the program then loops over all entries in that dictionary and writes out the data to a csv file ("pokemonstats.csv"). The data are converted to numbers (with the exception of the Pokemon's name) and are written out in this way, to better allow the machine-learning program to model the data.

(learn.py): The data from the previous program are read in using the Pandas "read_csv" function. The data are then cleaned to remove various sets of Pokemon (LC, NFE, and Untiered Pokemon), and these may be toggled on or off by commenting out the appropriate lines. Next, the names are assigned to their own variable, and the remaining numerical variables are assigned to NumPy arrays. A random sample of 90% of the data are set as training data, and the remaining data are set as testing data. Several modelling functions from the sklearn library are trained on the sample data and then asked to predict the tiers of the testing data. The deviations from the true values are plotted, and the number of correct predictions within a certain range of closeness are calculated and printed as a percent correct.

----------------------------------------------------------------

THE MACHINE-LEARNING PROBLEM:

At the root of it, this is a classification problem; we are attempting to train a model to place Pokemon into their correct tiers. However, because these are tiers (rather than arbitrary assignments), there is a hierarchy, which transforms easily to a numerical ranking. Thus, this is easily adapted to a regression problem. Now, some difficulty may arise when one tries to carefully assign numerical values to the tiers. How much more powerful is OU than UU? And how much more powerful is OU than PU? For now, we avoid this by simply declaring that all tiers are separated by 10 "points". This is not the most rigorous method of assigning numbers to tiers, but hey -- this is Pokemon. Let's relax a bit.

----------------------------------------------------------------

RESULTS:

The output of learn.py produces a set of four histograms, each using a distinct modelling technique. Additionally, it calculates the number of Pokemon that the modelling technique predicted correctly, to within some closeness. We immediately see from the text output of the program that the two classification models are worse at predicting the data than the regression models. To within one full tier (ignoring the BL tiers) up or down, the best classification model (K-Neighbors) predicts at just under 2/3 accuracy, and Linear Classification predicts at less than 1/2. Increasing the number of iterations of the Linear Classification model increases the accuracy up to a maximum of 56 percent with 10^7 iterations. The two regression models predict at or above 2/3 accuracy. Overall, we conclude that, while the dominant factor contributing to a Pokemon's tier placement, base stats and typing cannot sufficiently predict a Pokemon's final tier. Perhaps if each Pokemon's movepool and abilities were assigned a grade based on how likely they were to raise or lower a Pokemon's tier or if much more data were available, the models would predict more accurately. I leave the scoring of movepools and abilites for another time.




