# ============================================================
# Python Practice Program Day3
# Topics:
# 1. Conditional Statement
# 2. Nested Condition
# 3. Ternary Operator
# ============================================================


# ------------------------------------------------------------
# 1. CONDITIONAL STATEMENT
# ------------------------------------------------------------

age = 20

# Check whether the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ------------------------------------------------------------
# 2. CONDITIONAL STATEMENT - if / elif / else
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

# Check the grade based on marks
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# ------------------------------------------------------------
# 3. NESTED CONDITION
# ------------------------------------------------------------

age = 25
has_id = True

# First check the age
if age >= 18:

    # This if statement is inside the first if statement
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID to enter.")

else:
    print("You are not old enough to enter.")


# ------------------------------------------------------------
# 4. NESTED CONDITION - LOGIN EXAMPLE
# ------------------------------------------------------------

username = "admin"
password = "1234"

# Check the username first
if username == "admin":

    # If username is correct, check the password
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")

else:
    print("Incorrect username.")


# ------------------------------------------------------------
# 5. TERNARY OPERATOR
# ------------------------------------------------------------

age = 20

# Normal if-else:
# if age >= 18:
#     result = "Adult"
# else:
#     result = "Minor"

# The same logic using a ternary operator
result = "Adult" if age >= 18 else "Minor"

print("Age category:", result)


# ------------------------------------------------------------
# 6. TERNARY OPERATOR - EVEN / ODD
# ------------------------------------------------------------

number = 10

# If remainder is 0, number is even; otherwise it is odd
result = "Even" if number % 2 == 0 else "Odd"

print("Number is:", result)


# ------------------------------------------------------------
# 7. MINI PRACTICE PROGRAM
# ------------------------------------------------------------

marks = 85

# Check whether the student passed
if marks >= 50:

    # Nested condition to identify the performance
    if marks >= 90:
        print("Excellent performance!")
    elif marks >= 75:
        print("Very good performance!")
    else:
        print("Good performance.")

else:
    print("You failed. Try again.")


# Ternary operator to determine pass/fail
status = "Pass" if marks >= 50 else "Fail"

print("Result:", status)