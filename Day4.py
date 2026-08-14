# ============================================================
# Python Practice Program Day4
# Topics:
# 1. For Loop
# 2. List Comprehension

for i in range(5, 10):
    print("Iteration:", i)


list1 = [1, 45, 3, 55, 5]

for num in list1:   
    print("List1:", num)
  


# ------------------------------------------------------------
# Assignments 1. Dictionary → for loop
# ------------------------------------------------------------


student = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

for key in student:
    print(key, "->", student[key])


# ------------------------------------------------------------
# Assignments 2. Two lists → dictionary using for loop
# ------------------------------------------------------------              

keys = ["name", "age", "city"]
values = ["Alice", 20, "New York"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)