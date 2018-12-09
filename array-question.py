array = [2,4,1,1,4]

i = len(array)

while i >= 1 :
    if array(i) > 0:
        i = i - 1
        continue
    else:
        break
if i > 1:
 print "end is not reachable"
else :
 print "end is reachable"