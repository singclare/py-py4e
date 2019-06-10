##Loops and Iteration##
##Repeated Steps
#Loops(repeated steps) have iteration variables that change each time through a loop.
#Often these iteration variables go through a sequence of numbers
n = 5
while n > 0 : #If this condition is true, excution below sentence
    print(n) #And repeat while sentence > reaksing same question
    n = n - 1 # >> Iteration variable
print('Blastoff!') #If condition is false, skip over sentence
print(n)

##Breaking Out of Loop
#The break statement ends the current loop and jumps to the statement immediately folling the Loop
#It is like a loop test that can happen anywhere in the body of the Loop
while True :
    line = input('> ')
    if line == 'done' :
        break # >> loop is done
    print(line)
print('Done!')

##Finishing an Iteration with continue
#The continue statement ends the current iteration and jumps to the top of the loop and stats the next iteration
while True :
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

##Indefinite Loops
#While loops are called "indefinite loops" because they keep goin until a logical condition becomes false
#It is easy to look at, but
