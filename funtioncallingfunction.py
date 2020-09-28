def greeting():
    def say_hello():
        return "hello"
    return say_hello()
hello = greeting()
print(hello)