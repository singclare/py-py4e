##Reserved words
#Cannot use variable names / identifiers

##Sentences or Lines
x = 2  # Assignment statement
x = x + 2 #Assignment with expression
print(x) # Print statement

## Python Script
# Most programs are much longer -> Script!
# In a sense, we are "giving Python a script"
# we add ".py" on the end of files

##Interactive vesus Script
# Interactive: directly to Python and it responds
# Script: enter a sequence of statement using a text editor

##Program Steps or Program Flow
# Sequential Steps
x = 2 #1
print(x) #2
x = x + 2 #3
print(x) #4
# Conditional Steps : 'If' something is true, it can running
x = 5
if x < 10:
    print('Smaller') #True
if x > 20:
    print('Bigger') #False
print('Finis') #Output: Smaller; Finis;
#Repeated Steps: 'while' or 'for'
n = 5
while n > 0:
    print(n) #If it is True!
    n = n - 1
print('Blastoff') #If it is False!
