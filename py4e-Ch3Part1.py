##Chapter3.Conditional Execution##
##Conditional Steps
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

Print('Finis')

##Comparison Operators
#Boolean Expressions > comparison operators evaluate to T/F or Y/N
#Indentation(들여쓰기): 'if' sentence의 기준
x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 :
    print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6
    print('Not equal 6')

##One-Way Decisions
x = 5
print('Before 5')
if x == 5 :
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6') #False
    print('Is still 6') #False
    print('Third 6') #False
print('Afterwards 6')

##Indentation >> Import!
#Increase indent indent after an if or for statement(after :)
#Maintain indent to indicate the scope of block
#Reduce intend back to the level of if or for statement
#Blank lines are ignored - they do not effect Indentation
#Comments on a line by themselves are ignored with regard to Indentation

##Warning: Turn off Tabs!!
#Atom: automatically uses spaces for files with ".py" extension(nice!)
#Most text editors can turn tabs into spaces - make sure to enable this feature
#Python cares a "lot" about how far a line is indented
#If you mix tabs & spaces, you may get "indentation errors"

#increase / maintain after if or for
#decrease to indicate end of back
x = 5
if x > 2 : #Maintain
    print("Bigger than 2") #Increase
    print('Still bigger') #maintain
print('Done with 2') #decrease

for i in range(5) : #maintain
    print(i) #increase
    if i > 2 : #maintain
            print(i) #Increase
        print('Done with i', i) #decrease
print('All Done') #decrease

##Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')

##Two-Way Decisions(IF, ELSE)
#It is like a fork in the road - we must choose one or the other
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')

#Visualize Blocks
#We can use 'Enter' to visualiz Blocks
x = 4

if x > 2 :
    print('Bigger')
else :
    print('Smaller')

print('All done')
