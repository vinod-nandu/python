# ============================================================
# Python Practice Program Day5
# Topic: List Operations - Indexing and Methods
# ============================================================

# List example
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


# ------------------------------------------------------------
# Assignments 
#------------------------------------------------------------   


# List methods
numbers.append(60)
print("After append:", numbers)



numbers.insert(2, 25)
print("After insert:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])
''''
numbers.remove(30)
print("After remove:", numbers)

popped_value = numbers.pop()
print("Popped value:", popped_value)
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length of list:", len(numbers))
print("Count of 20:", numbers.count(20))

# Example with strings
fruits = ["apple", "banana", "mango"]
print("Fruits list:", fruits)
print("Second fruit:", fruits[1])

# Clear all items
fruits.clear()
print("After clear:", fruits)

'''
