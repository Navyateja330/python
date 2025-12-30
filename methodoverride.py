class MethodOverride1:
    def display(self):
        print("Method invoked from base class")


class MethodOverride2(MethodOverride1):
    def display(self):
        print("Method invoked from derived class")



ob = MethodOverride2()
ob.display()
