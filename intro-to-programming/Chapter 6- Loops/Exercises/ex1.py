prompt = "\nwhat are your topping for you pizza?(type 'quit' when you are finsihed):"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add that {topping} to your pizza.")
    else:
        break
    