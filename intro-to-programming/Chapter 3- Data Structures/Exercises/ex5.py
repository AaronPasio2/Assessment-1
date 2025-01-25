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