def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thnk u for using this function")
    return mfx
@greet
def hello():
    print("hello sir")
def add(a,b):
    print(a+b)
hello()
# greet(hello)()
add(1,2)
# greet(add)(1,2)
            