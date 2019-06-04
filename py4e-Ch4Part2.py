#Functions#

##Building our Own Functions
#We create a new function using def keyword
#This defines the function but does not excute the body of the function
x = 5
print('Hello')

def print_lyrics() :
    print("I'm a lumberjack, and I'm okay")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)

##Definitions and Uses
#Once we have defined a function, we can call(or invoke) it as many times as we like
#This is the store and reuse pattern

##Aruguments
#An argument is a value we pass into the function as its input when we call the function
#We use arguments so we can direct the function to do different kinds of work when we call it at different times
#We put the arguments in parentheses after the name of the function

##Parameters
#A parameters is a variable which we use in the function definition.
def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('Hello')
greet('en') #result: Hello
greet('es') #result: Hola
greet('fr') #result: Bonjour

##Return Values
#Often a function will take its arguments, do some computation, and
#return a value to be used as the value of the function call in the calling expression.
#The return keyword is used for This
def greet() :
    return "Hello"
print(greet(), "Glenn") #result: Hello Glenn
print(greet(), "Sally") #result: Hello Sally
#A "fruitful" function is one that produces a result(or return value)
#The return statement ends the function execution and "sends back" the result of the function
def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('Hello')
print(greet('en'), 'Glenn') #result: Hello Glenn
print(greet('es'), 'Sally') #result: Hola Sally
print(greet('fr'), 'Michael') #Bonjour Michael

##Arguments, Parameters, and Results
big = max('Hello world') #Hello world==Argument
print(big) # result: w==result

##Multiple Parameters / Arguments
#We can define more than one parameter in the function definition
#We simply add more arguments when we call the function
#We match the number and order of arguments and parameters
def addtwo(a, b) :
    added = a + b
    return added
x = addtwo(3, 5)
print(x)  #result: 8

##Void(non-fruitful) Functions
#When a function does not return a value, we call it a "void" function

##To function or not to function...
#Organize your ode into "paragraphs" - capture a complete thought and "name it"
#Don't repeat yourself - make it work once the then reuse it
#If something gets too long or complex, break it up into logical chunks and put those cunks in Functions
#Make a library of common stuff that you do over & over - perhaps share this with your friends...
