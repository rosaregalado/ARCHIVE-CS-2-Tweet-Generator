import random

def dictionary_words():
  open_file = open('/usr/share/dict/words')
  file_words = open_file.readlines()
  num_words = random.randint(0, len(file_words)-1)


if __name__ == "__main__":
  dictionary_words()