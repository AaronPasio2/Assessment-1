prompt = "\nEnter your age:"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("free!")
    elif age < 13:
        print("ticket is $10.")
    else:
        print("ticket is $15.")