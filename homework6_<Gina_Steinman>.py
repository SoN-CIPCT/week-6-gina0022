web_users = ['Gina', 'Nathan', 'Taylor', 'Billy', 'Belle']
new_users = ['Gina', 'William', 'Taylor', 'Nathan', 'Kiki']
for Gina in new_users:
    if Gina in web_users: 
        print(Gina+":This username is already in use. Please choose another username")
    else:
        print(Gina + ":This username is available")
cities = {
    "Seattle": {
        "Country": "United States",
        "Population": 12,
        "Fact": "Seattle opened the first Starbucks"
    },
    "Portland": {
        "Country": "United States",
        "Population": 5,
        "Fact": "Portland is known for staying weird"
    },
    "Baker": {
        "Country": "United States",
        "Population": 2,
        "Fact": "Baker is a city along the Snake River"
    }
}

print(cities["Seattle"]["Fact"])

      
