##Expressions##
##Numeric Expressions
#lack of mathematical symbols on computer -> using computer-speak
xx = 2
xx = xx + 2
print(xx) #4
yy = 400 * 12
print(yy) #5280
zz = yy / 1000
print(zz) #5.28
jj = 23
kk = jj % 5
print(kk) # 3
print(4 ** 3) #64

##Order of Evaluation = Operator precedence
#When we string operators together - Python must know which one to do first
#1.Parentheses 2.Exponentiation(Power) 3.Multiplication
#4.Addition and Subtraction 5.Left to right
x = 1 + 2 ** 3 / 4 * 5
    1 + 8 / 4 * 5
    1 + 2 * 5
    1 + 10
print(x) # 11

##What does "Type" Mean?
# Type: variables, literals, and constants
ddd = 1 + 4
print(ddd) # 5
eee = 'hello' + 'there'
print(eee) # hello there

##Type Matters
#Python knows what "type" everythin is
#If, "type" is different, it cannot operate
#We can use type() function when we want to know something's Type
eee = 'hello' + 'there'
eee = eee + 1 #error

##Serveral Types of Numbers
#Numbers have two main types: Integers / Floating Point Numbers
xx = 1
type(xx) #'int'
temp = 98.6
type(temp) #'float'

##Type Conversions
#intger and floating point >> the integer is implicitly convert to a floating
#You can control this with the built-in functions int()$float()
print(float(99) + 100) # 199.0
i = 42
type(i) # 'int'
f = float(i)
print(f) # 42.0
type(f) # 'float'

##Integer Division
#Integer division produces a floating point result
print(10 / 2) # 5.0
print(9 / 2) # 4.5

##String Conversions
#You can also use int()&float() to convert
#but, you will get an error if the string does not contain numeric characters
sval = '123'
type(sval) # 'str'
print(sval + 1) # error
ival = int(sval)
type(ival) # 'int'
print(ival + 1) #124
nsv = 'hello bob'
niv = int(nsv) #error

##User Input
#We can instruct Python to pause and read data >> input()
#The input() >> a String
nam = input('Who are you?') #Who are you? ()
print('Welcome' , nam) #Welcome ()

##Convertin User Input
#If we want to read a number from the user, we must conver it
# -string > number using conversion function
inp = input('Erope floor?')
usf = int(inp) + 1
print('US floor' , usf)
