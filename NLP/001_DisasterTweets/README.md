# Disaster Tweets

This folder is dedicated to solving Kaggle's [Natural Language Processing with Disaster Tweets](https://www.kaggle.com/c/nlp-getting-started/overview) challenge. This a **supervised binary classification** task in which the features are tweet information, and the target is a value of 1 if the tweet is about a real disaster, and 0 if not. As an exercise, **I will only be using the text of the tweets to make predictions.** This may affect accuracy, but the point of the exercise as far as we're concerned is to see how much can be gleaned exclusively from the text of the tweets.

In addition to an initial Jupyter Notebook for data exploration, for ease of reading each model or group of models of the same type will have its own dedicated Jupyter Notebook. For the purposes of modularization there are additional Python files containing functions and objects that are used repeatedly across models. These are stored in the `modules` folder. The data sets are stored locally in a folder called `raw_data`, but are not uploaded to GitHub; they can be found on the challenge's [Kaggle page](https://www.kaggle.com/competitions/nlp-getting-started/data).

For the purposes of scorekeeping, in this `README` file I will keep a running list of all of the models used along with the current best score of that model on Kaggle's test data. (Note that the evaluation metric for this challenge is the **F1 score, not accuracy**.) The models will be listed in descending order of highest-achieved F1 score.

1. _K_-nearest neighbors (Bag of words): **0.79037**
2. Decision Tree (Bag of words): **0.76616**
