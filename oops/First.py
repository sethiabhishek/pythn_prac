class example:
    var1 = "This is var1"

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return name


obj1 = example()
obj1.set_name("abhishek")
print "name of the person is: %s" %obj1.name