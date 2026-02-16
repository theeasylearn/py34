countries = ["India", "United States", "Canada", "Australia", "United Kingdom", "Germany", "France", "Japan", "China", "Brazil", "Italy", "Spain", "Mexico", "Russia", "South Africa", "Argentina", "Indonesia", "Saudi Arabia", "South Korea", "Netherlands"]

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Papaya", "Strawberry", "Watermelon", "Kiwi")


line = "The quick brown fox jumps over the lazy dog while five quirky wizards vex bold knights."

country = input("where are you from?") # France 
country_visit = input("Which is your favorite tourist destination country")

isFound = country in countries
isNotFound = country_visit not in country 
print(f"{country} found ?",isFound);
print(f"{country_visit} not found ?",isNotFound);

favorite_fruit = input("Which is your favorite fruit?")
isFound = favorite_fruit in fruits
isNotFound = favorite_fruit not in fruits

print(f"{favorite_fruit} found ?",isFound);
print(f"{favorite_fruit} not found ?",isNotFound);

word = input("Enter any word")
isFound = word in line
isNotFound =  word not in line 

print(f"{word} found {line}?",isFound);
print(f"{word} not found {line}?",isNotFound);


