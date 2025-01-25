
pet1 = {
    'name': 'Dog',
    'Owner': 'Christian',
}

pet2 = {
    'name': 'Cat',
    'Owner': 'Christine',
}

pet3 = {
    'name': 'Parrot',
    'Owner': 'Jacob',
}


pets = [pet1, pet2, pet3]


for pet in pets:
    print(f"\n Everything you know about  {pet['Owner'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")