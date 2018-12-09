x = [i for i in range(10)]

print x

y = [i**2 for i in range(10)]
print y

z=  [i*3 for i in range(10)]
print z

list = ['python','java','scala','haskell']

list2 = [str.capitalize()[0] for str in list]
print list2

result = [x +y for x in [1,2,3] for y in [1,2,3,4]] # works as nested loop
print result

