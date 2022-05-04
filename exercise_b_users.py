users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  },
  "Mike":{
    "twitter": "mikeyboy",
    "lottery_numbers": [6,2,34,21,19],
    "home_town": "Southampton",
    "pets": [
      {
        "name": "tulip",
        "species": "parot"
      }
    ]

  },
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

Jonathans_handle = users ["Jonathan"]["twitter"]
print(Jonathans_handle)
# 2. Get Erik's hometown

Eriks_hometown = users ["Erik"] ["home_town"]
print(Eriks_hometown)
# 3. Get the list of Erik's lottery numbers
E_lottery = users ["Erik"] ["lottery_numbers"]
print(E_lottery)
# 4. Get the species of Avril's pet Monty
A_pet = users ["Avril"]["pets"][0]
print(A_pet)
# 5. Get the smallest of Erik's lottery numbers
print(min (users ["Erik"] ["lottery_numbers"]))

# 6. Return an list of Avril's lottery numbers that are eve

avrils_numbers = users ["Avril"] ["lottery_numbers"]
for num in avrils_numbers:
   if num % 2 == 0:
      print(num)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

Eriks_numbers = users ["Erik"] ["lottery_numbers"] 
Eriks_numbers.append (7)
print(Eriks_numbers)


# 8. Change Erik's hometown to Edinburgh

Eriks_hometown2 = users ["Erik"] ["home_town"]
Eriks_hometown2 = "Edinburgh"
print(Eriks_hometown2)

# 9. Add a pet dog to Erik called "fluffy"

Eriks_pet = users ["Erik"] ["pets"]
Eriks_pet.append({"Name":"fluffy", "Species":"Dog"})
print (Eriks_pet)
# 10. Add another person to the users dictionary
#Done