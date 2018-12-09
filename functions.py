def say_hello(greet,name):
    print "Good %s %s" %(greet,name)

say_hello('morning','abhishek')

a = say_hello

a('morning','abhishek')

def calculate_square(input):
    return input*input

print "square of 2 is %d" %calculate_square(2)

# var args code check
def log_me(*num):
    print type(num)
    print num[0]

log_me(1,1.2,2)

#key word arguments

def log_keyword_args(**num):
    print type(num)
    print num
    print num.get('a')

log_keyword_args(a=5,b=6)

newDict = {'a':5,'b':6,'c':2}

print newDict

log_keyword_args(a=newDict)

# Lambda functions

x= lambda a : a*a

print "value return by first lambda: %d" %x(2)

y = lambda a,b : a*b

print y(2,3)

x=  lambda a : lambda b : a + b

firstArg = x(2)

finalR = firstArg(3)

print "result is %d" %finalR


list1 = [1,2,3,4]
list2 = [5,6,7]

list1.append(list2)

print "list3 is %s" %list1

list1.remove(3)
print "list3 is %s" %list1

















