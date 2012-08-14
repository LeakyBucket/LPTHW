class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):  
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit() # This will invoke the implicit function in Parent
son.implicit() # This will invoke the implicit function in Parent

dad.override() # This will invoke the override function in Parent
son.override() # This will invoke the override function in Child

dad.altered() # This will invoke the altered function in Parent
son.altered() # This will invoke the altered function in Child which calls the altered in Parent