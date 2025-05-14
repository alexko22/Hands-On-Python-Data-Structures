# Task 1: Working with List
fruits = ["apple", "banana", "watermelon", "kiwi", "pineapple"]
# adding and removing a fruit...
fruits.append("strawberry")
fruits.remove("watermelon")
# reversing the order of the list...
fruits = fruits[::-1]
print(fruits)

# Task 2: Exploring Dictionaries
info = {"name": "Alex", "age": 22, "city": "Boston"}
# updating the dictionary...
info.update({"favorite color": "blue"})
info.update({"city": "New York"})
# print the values using a loop...
for key in info:
    print("Key:", key, "Value:", info[key])

# Task 3: Using Tuples
tuple = ('Star Wars', 'Walk', 'Eighty-Six')
# this line below fails
# tuple[0] = 'Immutable'
# printing the length of the tuple...
print(len(tuple))


