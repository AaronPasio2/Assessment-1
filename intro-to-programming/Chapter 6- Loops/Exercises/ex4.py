sandwich_orders = ['Egg', 'grilled cheese', 'Meatball ', 'Turkey ']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your  {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("Sandwitches that are made:")
for sandwich in finished_sandwiches:
    print(f" {sandwich} sandwich")