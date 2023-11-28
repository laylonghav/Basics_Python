country_cities = {
    "Cambodia": "Phnom Penh",
    "Thailand": "Bangkok",
    "Japan": "Tokyo",
    "Korea": "Seoul"
}

# Get the country name from the user
user_country = input("Enter a country: ")

# Lookup and print the corresponding city
if user_country in country_cities:
    city = country_cities[user_country]
    print(f"The city in {user_country} is {city}.")
else:
    print("Country not found in the database.")