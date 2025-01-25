def describe_city(city, country='Philippines'):
    """Describe city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Cagayan Valley')
describe_city('Rome', 'Italy')
describe_city('Isabela')

