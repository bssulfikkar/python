#####################################################
#call the python script  using the below command inside the REPL
#import os
#import subprocess
#DIR = os.path.join('C:\\', 'Users', 'K', 'Desktop', 'demo.py')
#subprocess.call(['python', DIR])
#from demo import nth_root
#nth_root(16,2)
#from demo import ordinal
#ordinal(2)
#from demo import display_nth_root
#display_nth_root(16,2)

#call the function inside the python script from windows using the below commands
#python -c 'import demo; demo.nth_root(16, 2)'
#python -c 'import demo; demo.ordinal(2)'
#python -c 'import demo; demo.display_nth_root(16,2)'
#####################################################

def nth_root(radicand, n):
    print (radicand ** (1/n))
    return radicand ** (1/n)
	

def ordinal_suffix(n):
    s = str(n)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(n):
    print (str(n) + ordinal_suffix(n))
    return str(n) + ordinal_suffix(n)
    
def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    ordinal_number = ordinal(n)
    message = "The " + str(ordinal_number)  + " root of " + str(radicand) + " is " + str(root)
    print(message)
