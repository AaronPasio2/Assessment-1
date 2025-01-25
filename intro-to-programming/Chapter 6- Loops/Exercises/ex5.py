sandwich_orders = ['Egg', 'Grilled Cheese', 'Pastrami', 'Meatball', 'Turkey', 'Pastrami', 'Pastrami']
finished_sandwiches = []

print("We've run out of pastrami sandwiches.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that are made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")