# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits=["pineapple", "litchi", "marula", "watermelon"]
print(fruits)
# TODO: Add a fruit to the end of the list
fruits.append("pomelo") 
print(fruits)
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"grapefruit") 
print(fruits)
# TODO: Remove a fruit from the list
fruits.remove("marula") 
#print(fruits)
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers=(1, 2, 3, 4, 5)
#print(numbers)
# TODO: Create a new list with each number squared
#squared_numbers=(1, 4, 9, 25)
squared_numbers=({1*1}, {2*2}, {3*3}, {4*4}, {5*5})
print(squared_numbers)
# TODO: Find the sum and average of the original numbers
sum=(1+2+3+4+5)
print(sum)
average=sum/5
# TODO: Print the results
print(int(average))

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries={
    "South Africa" : "Pretoria",
    "Nigeria" : "Abuja",
    "Angola" : "Luanda",
    "Botswana" : "Gabarone",
    "Brazil" : "Brasilia"    
}

# TODO: Add a new country-capital pair
countries["Canada"]="Ottawa"

# TODO: Update the capital of an existing country
countries.update({"South Africa" : "Cape Town"})

# TODO: Remove a country-capital pair
del countries["Angola"]
# TODO: Print the modified dictionary
print(countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits={
    "Orange" : "orange",
    "apple" : "green",
    "banana" : "yellow"
}
print(fruits)
# TODO: Print all the fruits (keys)
#for keys in fruits :
print(fruits.keys())
# TODO: Print all the colors (values)
print(fruits.values())
# TODO: Print each fruit and its color
for keys_and_values in fruits: 
    if fruits == "orange": 
        a+=1 
print(fruits)
# TODO: Check if a fruit is in the dictionary and print its color
print("insert the name of a fruit")
check = input("Fruit: ")
if check in fruits :
    print(f"The color of {check} is {fruits[check]}.")
else:
    print(f"{check} is not in the dictionary.")