message = "hello"
name = "pierre"
message = f"{message}, {name}. Welcome!"

"""
    Will print info about method upper in this case
"""
print(help(str.upper))

"""
    will print all the methods that can be applied to this type of variable.
    string in this case
"""
print(dir(name))
