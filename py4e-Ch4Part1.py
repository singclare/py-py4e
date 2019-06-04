##Stored(and reused) Steps
#def : step for store functions > create code and record it
def thing() :  #define function thing()
    print("Hello")
    print('Fun')

thing()
print('Zip')
thing()

##Python Functions
#1.Built-in functions: provided as part of Python - print(), input()
#2.Functions that we define ourselves

##Function Definition
#We define a functions using the def reserved word
#We call/invoke the function by using the function name, arguments, etc.
big = max('Hello world') #big=assignment,'Hello world' = argument
print(big) # result: w - return value
tiny = min('Hello world')
print(tiny)

##Max functions
#A function is some stored code that we use.
#A function takes some input and produces an ouput

##Type Conversions
print float(99) / 100 #result: 0.99
i = 42
type(i) #results: <class 'int'>
f = float(i)
print(f) #results: 42.0
type(f) #result: <class 'float'>
print(1 + 2 * float(3) / 4 - 5) # results: -2.5

##String Conversions
#You can also use int() and float() to convert
#You will get an error if the string does not contain numeric characters
sval = '123'
type(sval) #result: <class 'str'>
print(sval + 1) #result: error
ival = int(sval)
type(ival) #result: <class 'int'>
print(ival + 1) #result: 124
nav = 'hello bob'
niv = int(nav) #result: error
