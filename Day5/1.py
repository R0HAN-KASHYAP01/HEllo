class MyClass:
    def sayHello(self,name):
        print(f"Hello, {name}")
    
name = input("Enter the name: ")
greeting = MyClass()
greeting.sayHello(name)
