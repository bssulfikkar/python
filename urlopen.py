#####################################################
#call the python script  using the below command inside the REPL
#import os
#import subprocess
#DIR = os.path.join('C:\\', 'Users', 'K', 'Desktop', 'urlopen.py')
#subprocess.call(['python', DIR])
#from urlopen import fetch_words
#fetch_words()

#call the function inside the python script from windows using the below commands
#python -c 'import urlopen; urlopen.fetch_words()'
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
