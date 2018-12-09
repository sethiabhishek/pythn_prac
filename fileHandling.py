path = r"C:\Python Prac\test.txt"  #how to mention the raw path

#fh = open(path)
#print fh.read() # moves the pointer to end of the file,you can move the pointer to fwd and back using seek method
#fh.close()

#fh = open(path,"w+")
#fh.write("Writing some dummy data again")
#print fh.read()
#fh.close()

fh = open(path)
for line in fh:
    if __name__ == '__main__':
        print line


# usage of readlines method
fh.seek(0)
a = fh.readlines(7)

for i in a:
    if __name__ == '__main__':
        print i









