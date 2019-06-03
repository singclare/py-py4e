#Conditionals#
##Multi-way
#elif: 'if' condtion is false >> elif do condtion
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
# if x=5, it print 'Medium' / if x=0, it print 'small'
# 'else' activate when all condition is false.
# When you use 'elif', you attend order

##The try / except Structure
# You surround a dangerous section of code with 'try' and 'except'
# If the code in the try works - the except is skipped
# If the code in the try fails - it jumps to the except section
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1       # except code activates

print('First', istr)

astr = '123'
try:
    istr = int(astr) # try code activates
except:
    istr = -1

print('Second', istr)
#But you don't abuse 'try' sentence
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)

##Sample try / except
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('Nice work')
else :
    print('Not a Number')
