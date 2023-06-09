with open('example.txt', 'w') as file_object:
    content = """This tis a multiline string.
Python is a versatile language.
It is easy to learn and use."""
    print(content)
    file_object.write(content)