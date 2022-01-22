import random

def random_words(words):
  if ',' in words:
    #remove comma
    change_words = words.replace(',', ' ')
    #split words
    split_words = change_words.split(' ')
    #shuffle random words
    random.shuffle(split_words)
    print(" ".join(split_words))

  else:
    #split words
    split_words = words.split(' ')
    #shuffle random words
    random.shuffle(split_words)
    print(" ".join(split_words))

if __name__ == '__main__':
  words = input("Enter words here: ")
  random_words(words)