
def country_city(country, city, population=None):
    """Show full name country and city."""
    if population:
        full_name = f"{country} {city}. Population - {population}"
    else:
        full_name = f"{country} {city}"
    return full_name.title()
