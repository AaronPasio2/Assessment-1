rivers = {
    "Cagayan River": "Philippines",
    "Amazon River": "South America",
    "Seine River": "France"
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")


print("\nRivers include in the dictionary:")
for river in rivers.keys():
    print(river.title())


print("\nCountry included in the dictionary:")
for country in rivers.values():
    print(country.title())

