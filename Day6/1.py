class Base:
    def showBase(self):
        print("This message from base class.")
    
class Derived(Base):
    def showDerived(self):
        print("This message from derived class.")

Base_msg = Base()
Derived_msg = Derived()

Base_msg.showBase()

Derived_msg.showBase()

Derived_msg.showDerived()

        