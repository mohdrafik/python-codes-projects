# Multilevel Inheritance
class grandparent:
    def grandparent_method(self):
        print(f"I am grandparent")

class parent(grandparent):
    def parent_method(self):
        print(f"I am parent")

class child(parent):
    def child_method(self):
        print(f"I am grand_child")

c1= child()
c1.grandparent_method()
c1.parent_method()
c1.child_method()