import sys
import os
from nltk.corpus import wordnet as wn

def main():
   filepath = sys.argv[1]

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   bag_of_words = {}
   bag_of_synsets = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent 1000 words {}".format(sorted_words[1:]))
   for word in sorted_words:
       print(word[0])
       bag_of_synsets[word] = wn.synsets(word[0])
   print(bag_of_synsets)
  
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

if __name__ == '__main__':
    main()