# ============================================================
# Python Practice Program Day7
# Topic: Set Operations - Indexing and Methods
# ============================================================
'''
skills = {"Python", "Java", "C++", "JavaScript", "Python"} 

#duplicate values will be removed automatically from Set

print("Original set:", skills)

skills.add("SQL")
print("After add:", skills)

skills.remove("Java")
print("After remove:", skills)

skills.discard("C++")
print("After discard:", skills)

frozenset_skills = frozenset(skills)
print("Frozen set:", frozenset_skills)


# frozenset_skills.add("HTML")  # This will raise an error since frozenset is immutable

'''

# ------------------------------------------------------------
# Assignments ::Convert a list with duplicates into a frozenset (duplicates are removed automatically)
#
#------------------------------------------------------------   
 
numbers = frozenset([1, 2, 2, 3, 4, 4, 5])

print(f"Frozen Set Content: {numbers}")
print(f"Total Unique Items: {len(numbers)}")

print("\n--- Iterating through items ---")
for num in numbers:
    # Perform math or logic on the items during iteration
    print(f"Current number: {num}, Squared: {num**2}")