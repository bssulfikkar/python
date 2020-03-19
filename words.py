#####################################################
#call the python script  using the below command inside the REPL
#import os
#import subprocess
#DIR = os.path.join('C:\\', 'Users', 'K', 'Desktop', 'words.py')
#subprocess.call(['python', DIR])
#from words import fetch_words
#fetch_words()

#call the function inside the python script from windows using the below commands
#python -c 'import words; words.fetch_words()'

#call the function by importing the module
#cd desktop
#python
#import words
#words.fetch_words()
#or
#import words
#from words import fetch_words
#fetch_words()
#url = 'http://sixty-north.com/c/t.txt'
#####################################################

import sys
from urllib.request import urlopen
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
