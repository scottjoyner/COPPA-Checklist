import sys
import os
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("wordnet")
from nltk.corpus import wordnet as wn

def main():
   filepath = sys.argv[1]
   infile = "infile.txt"
   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
   ruberic = {}
   with open(infile) as fp:
       cnt = 0
       for line in fp:
           if line.find("###"):
               print(line)
               cnt += 1
           else:
               record_rating(line.strip().split(' '), ruberic)
   bag_of_words = {}
   bag_of_synsets = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           # print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   # print("Most frequent 1000 words {}".format(sorted_words[1:]))
   for word in sorted_words:
       print(word[0])
       bag_of_synsets[word] = wn.synsets(word[0])
   score = 0
   for sentiment in ruberic:
       for word in bag_of_synsets:
           if word[0] == sentiment[0]:
               print(word[0])
               score += 1
   print("Score for this policy: {}".format(score))
def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1

def record_rating(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1

if __name__ == '__main__':
    main()