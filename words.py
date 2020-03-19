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
#####################################################

from urllib.request import urlopen
def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    
    for word in story_words:
        print(word)

print(__name__)       
if __name__ == '__main__':
    fetch_words()
    
