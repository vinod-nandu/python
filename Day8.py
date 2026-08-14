# Day 8: Python Functions Learning Guide
# Functions are reusable blocks of code that perform specific tasks

# ============================================================================
# 1. BASIC FUNCTION DEFINITION AND CALLING
# ============================================================================

def greet():
    """A simple function with no parameters"""
    print("Hello, Welcome to Day 8 Functions!")

# Call the function
greet()


# ============================================================================
# CALCULATOR PROCESS FUNCTIONS
# ============================================================================

# ============================================================================
# 1. BASIC ARITHMETIC OPERATIONS
# ============================================================================

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(base, exponent):
    """Calculate power (base ** exponent)"""
    return base ** exponent

def modulus(a, b):
    """Get remainder of division"""
    if b == 0:
        return "Error: Division by zero!"
    return a % b

# Test basic operations
print("=" * 50)
print("BASIC ARITHMETIC OPERATIONS")
print("=" * 50)
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")
print(f"2 ** 3 = {power(2, 3)}")
print(f"10 % 3 = {modulus(10, 3)}\n")


# ============================================================================
# SUMMARY OF CALCULATOR FUNCTIONS
# ============================================================================

print("=" * 50)
print("CALCULATOR FUNCTIONS SUMMARY")
print("=" * 50)
print("""
BASIC OPERATIONS:
  - add(a, b)
  - subtract(a, b)
  - multiply(a, b)
  - divide(a, b)
  - power(base, exp)
  - modulus(a, b)

""")

