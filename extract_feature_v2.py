#!/usr/bin/python3.5

#import required libraries
import os
import csv
from rake_nltk import Rake

#set path, !!!caution path may vary for a diferent machine
path = os.path.expanduser('~/Desktop/Old_files/rake_implement/')

#================================================rake extraction
#create rake object r
r = Rake()

#read reviews from textfile
with open('apple_ipad_reviews.txt') as text:
    content = text.read()

#extract keywords using rake object
r.extract_keywords_from_text(content)

#================================================feature matching from keyword_corpus
#read keywords from csv file
with open('feature_keyword_collection.csv', 'r') as csvfile:
    keyword_corpus = sum(list(csv.reader(csvfile, delimiter=',')), [])

#process user keywords to a single word from a multi dimentional list
#user_keywords = sum([key.split() for key in r.get_ranked_phrases()], [])

#process user keywords to a single list only when the review text is more than 2 words
user_feature_list = [key for key in r.get_ranked_phrases() if len(key.split()) >= 2]

#initialize an empty list for final feature array
final_features = []

#iterate and check for keyword if it matches one from keyword_corpus 
for user_feature in user_feature_list:
    if any(keyword in user_feature for keyword in keyword_corpus):
        final_features.append(user_feature)

final_features = list(set(final_features))


#================================================writing final features to a text file
#write the processed output to a .txt file
with open(path+'final_feature.txt', 'w+') as txt:
    if (final_features):
        txt.write(str(final_features))
    else:
        txt.write('No matching features found !!')



'''
for user_key in user_keywords:
    for key in keyword_corpus:
        if user_key in keyword_corpus:
            with open(path+'final_feature.txt', 'w+') as txt:
                txt.write(user_keyword)
    with open(path+'final_feature.txt', 'w+') as txt:
        txt.write('No matching features found !!')
'''

#write extracted feature to new text file
#with open(path+'feature.txt', 'w+') as txt:
#    txt.write(str(r.get_ranked_phrases()))

#write extracted feature along with feature score to a new text file
#with open(path+'feature_with_score.txt', 'w+') as txt:
#    txt.write(str(r.get_ranked_phrases_with_scores()))
