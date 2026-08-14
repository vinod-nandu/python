# ============================================================
# Python Practice Program Day2
# Topics:
# 1. Numbers
# 2. Strings
# 3. List
# 4. Dictionary
# 5. Tuple
# 6. Set
# 7. Boolean
# 8. Ternary Operator
# ====================================================


# Numbers
a = 10
b = 5.5

# String
name = "John"

# List
marks = [80, 90, 70]

# Dictionary
student = {"name": "John", "age": 16}

# Tuple
point = (4, 5)

# Set
numbers = {1, 2, 2, 3}

# Boolean
pass_exam = True

print(a)
print(name)
print(marks)
print(student)
print(point)
print(numbers)
print(pass_exam)

"""
Quick comparison
Numbers → used for numeric value
Strings → used for text
List → ordered, changeable
Dictionary → key-value pairs
Tuple → ordered, not changeable
Set → unique values, no order
Boolean → True or False
"""

'''

Immutable - மாறாதது

| Data Type   | Example             | Immutable? |
| ----------- | ------------------- | ---------- |
| `int`       | `10`                | ✅ Yes      |
| `float`     | `10.5`              | ✅ Yes      |
| `bool`      | `True`              | ✅ Yes      |
| `str`       | `"Hello"`           | ✅ Yes      |
| `tuple`     | `(1, 2, 3)`         | ✅ Yes      |
| `frozenset` | `frozenset({1, 2})` | ✅ Yes      |
| `bytes`     | `b"Hello"`          | ✅ Yes      |

Mutable types
list → ❌ Mutable
dict → ❌ Mutable
set → ❌ Mutable
bytearray → ❌ Mutable

'''