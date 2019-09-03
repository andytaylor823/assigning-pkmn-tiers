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

(learn.py): The data from the previous program are read in using the Pandas "read_csv" function. The data are then cleaned to remove various sets of Pokemon (LC, NFE, and Untiered Pokemon), and these may be toggled on or off by commenting out the appropriate lines. Next, the names are assigned to their own variable, and the remaining numerical variables are assigned to NumPy arrays. A random sample of 90% of the data are set as training data, and the remaining data are set as testing data. The XXX function from the sklearn library is trained on the sample data, and then asked to predict the tiers of the testing data. The results were compared to the true values, and if the data fell within a certain range of closeness to the true values, they were counted as correct. The program concludes by printing out the Pokemon that are not within the range of closeness, as well as the predicted and actual tier values.

----------------------------------------------------------------

THE MACHINE-LEARNING PROBLEM:
(talk about how it's a classification problem or a regression problem)

----------------------------------------------------------------

RESULTS:
(come back to this after you mess around a bit more with the machine-learning functions)




