class demo:
    def __init__(hello,name):
        hello.name=name

    def __init__(slf,name):
        slf.name=name
    
    def greet_hello(hello):
        print(f"Hello!, {hello.name}")
    
    def greet_slf(hello):
        print(f"Hello!, {hello.name}")

d=demo("Utkarsh")

print(f"using hello instead of self : ")
d.greet_hello()
print(f"\nusing slf instead of self : ")
d.greet_slf()