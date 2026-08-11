'''
text = input("Enter text: ")
methods = ["upper", "lower", "title", "capitalize", "swapcase"]
for method in methods:
    if method == "upper":
        print("Upper      :", text.upper())
    elif method == "lower":
        print("Lower      :", text.lower())
    elif method == "title":
        print("Title      :", text.title())
    elif method == "capitalize":
        print("Capitalize :", text.capitalize())
    elif method == "swapcase":
        print("Swapcase   :", text.swapcase())
if text.isupper():
    print("The original text is in uppercase.")
elif text.islower():
    print("The original text is in lowercase.")
elif text.istitle():
    print("The original text is in title case.")
else:
    print("The original text has mixed case.")
'''
while True:
    username = input("Enter username (or quit): ")
    if username.lower() == "quit":
        break
    if not username.isalnum():
        print("Invalid: Username must contain only letters and numbers.")
    elif not username[0].isalpha():
        print("Invalid: Username must start with a letter.")
    elif not username.isidentifier():
        print("Invalid: Username is not a valid Python identifier.")

    elif not username.isascii():
        print("Invalid: Username contains non-ASCII characters.")

    else:
        print("Valid username!")
