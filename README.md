# assigning-pkmn-tiers
Attempting to use the power of machine learning to assign Pokemon to Smogon tiers

Competitive Pokemon is a bit of a hobby of mine. I first got interested in Smogon (the hub for all things competitive Pokemon) around when Pokemon Diamond / Pearl / Platinum came out, and I've been involved ever since.

Competitive battlers assign Pokemon to various tiers based on their power level -- anyone who's played Pokemon knows a battle between Mewtwo and a Beedrill is not a fair fight! All Pokemon known up through Pokemon Sun / Moon (as well as their base stats, abilities, types, and tier) may be found on Smogon's website: https://www.smogon.com/dex/sm/pokemon/

There are many factors that battlers consider when deciding what tier a Pokemon belongs in. The Pokemon's base stats are the most significant factor, but the Pokemon's abilities, typing, and movepool also need to be considered. Additionally, a Pokemon may be excellent in all of the above, yet be outclassed by a still better Pokemon, keeping its tier somewhat low.

For this project, I aim to classify a Pokemon into a tier based only on its base stats. This is the largest contribution to its tier placement, and the sample size for this problem is somewhat low, compared to other machine-learning problems. There are only ~380 or so Pokemon which are fully-evolved, competitive Pokemon in some tier, so we have less than 400 data points, and potentially many variables influencing our predicted variable. Thus, we only use a Pokemon's base stats in predicting what tier it belongs in.

TO RUN THIS CODE:
You first must have Python 3 installed. Begin by running the code "create_data.py" to use web-scraping to pull relevant data from the Smogon website above and write it out in a .csv file. Once this file has been created, running the code "learn.py" will read in the data using Pandas, train the machine-learning function on a sample of the known data, and predict on a small (unused) sub-set of the known data. When the new Pokemon games (Sword / Shield) come out, this may be useful to get a first look at what tiers certain Pokemon may fall into.

Over time, the Smogon website above may change, so I am also including the dataset that would have been created if the website never changed.
