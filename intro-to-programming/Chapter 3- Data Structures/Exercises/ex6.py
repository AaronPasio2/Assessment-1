guests = ['Justin', 'Jhon', 'Ahmad','Sofia']

name = guests[0].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[1].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[2].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[3].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[0].title()
print(f"\nSorry, {name} won't be able to join us for our dinner.")

del(guests[0])
guests.insert(1, 'Will')

name = guests[1].title()
print(f"\n{name}, You are invited to have dinner with us.")

name = guests[0].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[2].title()
print(f"{name}, You are invited to have dinner with us.")

name = guests[3].title()
print(f"{name}, You are invited to have dinner with us.")

print("\nSorry, I can only invite two people to dinner.")

while len(guests) > 2:
    name = guests.pop() 
    print(f"Sorry, {name.title()}, there's no room at the table.")

name = guests[1].title()
print(f"{name}, Come have dinner with us.")

name = guests[0].title()
print(f"{name}, Come have dinner with us.")


guests.clear()
print(guests) 
