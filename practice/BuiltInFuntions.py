names = ['abhishek','piku','mishu']
print "list is %s" %names
worker = dict(one=1,two=2)
worker1 = dict([("two",2)])
print worker == worker1
print "worker is %s" %worker1

print worker.keys()


worker_keys = set(worker.keys())
worker1_keys = set(worker1.keys())

print "worker_keys %s" %worker_keys
print "worker1_keys %s" %worker1_keys

keys_intersection = worker1_keys & worker_keys

print "instersection is %s" %keys_intersection

