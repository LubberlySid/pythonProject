def greeting(name):
    print("Begin")
    greet = f"Hello, {name}"
    print("End")
    return greet


def test_func():
    return None


print(greeting("Ostap"))
print(test_func())
