def greeting(name):
    print("Begin")
    greet = f"Hello, {name}"
    print("Hello")

    return greet


def test_func():
    return None


print(greeting("Ostap"))


def bug_fix():
    print("top")
    

print(test_func())
print(bug_fix())
