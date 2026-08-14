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
# 2. FUNCTION WITH PARAMETERS
# ============================================================================

def add(a, b):
    """Function that takes two parameters and adds them"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Call with arguments
sum_result = add(5, 3)
print(f"Result stored: {sum_result}\n")


# ============================================================================
# 3. FUNCTION WITH DEFAULT PARAMETERS
# ============================================================================

def introduce(name, age=25, city="Unknown"):
    """Function with default parameter values"""
    print(f"Name: {name}, Age: {age}, City: {city}")

introduce("Alice")  # Uses default age and city
introduce("Bob", 30)  # Uses default city
introduce("Charlie", 28, "New York")  # All parameters specified
print()


# ============================================================================
# 4. FUNCTION WITH MULTIPLE RETURN VALUES
# ============================================================================

def get_person_info():
    """Function that returns multiple values"""
    name = "David"
    age = 35
    email = "david@example.com"
    return name, age, email

# Unpacking return values
person_name, person_age, person_email = get_person_info()
print(f"Person: {person_name}, Age: {person_age}, Email: {person_email}\n")


# ============================================================================
# 5. FUNCTION WITH *ARGS (Variable Number of Arguments)
# ============================================================================

def sum_all(*numbers):
    """Function that accepts any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

result1 = sum_all(1, 2, 3)
result2 = sum_all(10, 20, 30, 40, 50)
print(f"Sum of 1,2,3: {result1}")
print(f"Sum of 10,20,30,40,50: {result2}\n")


# ============================================================================
# 6. FUNCTION WITH **KWARGS (Keyword Arguments)
# ============================================================================

def print_info(**info):
    """Function that accepts keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(language="Python", version="3.9", difficulty="Intermediate")
print()


# ============================================================================
# 7. LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================================================

# Lambda function for simple operations
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"15 * 4 = {multiply(15, 4)}\n")


# ============================================================================
# 8. MAP, FILTER, REDUCE WITH LAMBDA
# ============================================================================

numbers = [1, 2, 3, 4, 5, 6]

# MAP: Apply function to all items
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# FILTER: Keep items that satisfy condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}\n")


# ============================================================================
# 9. NESTED FUNCTIONS (Functions inside Functions)
# ============================================================================

def outer_function(x):
    """Outer function with inner function"""
    def inner_function(y):
        return y ** 2
    
    result = inner_function(x)
    return result

result = outer_function(4)
print(f"Outer -> Inner result: {result}\n")


# ============================================================================
# 10. CLOSURE (Function returning a function)
# ============================================================================

def multiplier(n):
    """Returns a function that multiplies by n"""
    def multiply(x):
        return x * n
    return multiply

times_3 = multiplier(3)
times_5 = multiplier(5)

print(f"10 * 3 = {times_3(10)}")
print(f"10 * 5 = {times_5(10)}\n")


# ============================================================================
# 11. DOCSTRINGS AND TYPE HINTS
# ============================================================================

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle (float)
    
    Returns:
        The area of the circle (float)
    """
    pi = 3.14159
    return pi * radius ** 2

area = calculate_area(5)
print(f"Area of circle with radius 5: {area:.2f}\n")


# ============================================================================
# 12. PRACTICAL EXAMPLE: PASSWORD VALIDATOR
# ============================================================================

def validate_password(password):
    """
    Validate password strength.
    
    Returns:
        Dictionary with validation results
    """
    requirements = {
        'length': len(password) >= 8,
        'has_uppercase': any(c.isupper() for c in password),
        'has_lowercase': any(c.islower() for c in password),
        'has_digit': any(c.isdigit() for c in password),
    }
    
    is_valid = all(requirements.values())
    return is_valid, requirements

is_valid, details = validate_password("Python2024!")
print(f"Password valid: {is_valid}")
print(f"Details: {details}\n")


# ============================================================================
# 13. PRACTICAL EXAMPLE: LIST OPERATIONS
# ============================================================================

def process_list(items, operation="count"):
    """
    Process a list based on operation.
    
    Operations: count, sum, average, sort
    """
    if operation == "count":
        return len(items)
    elif operation == "sum":
        return sum(items)
    elif operation == "average":
        return sum(items) / len(items) if items else 0
    elif operation == "sort":
        return sorted(items)
    else:
        return None

numbers = [5, 2, 8, 1, 9, 3]
print(f"List: {numbers}")
print(f"Count: {process_list(numbers, 'count')}")
print(f"Sum: {process_list(numbers, 'sum')}")
print(f"Average: {process_list(numbers, 'average'):.2f}")
print(f"Sorted: {process_list(numbers, 'sort')}\n")


# ============================================================================
# 14. PRACTICAL EXAMPLE: STRING MANIPULATION
# ============================================================================

def format_text(text, style="normal"):
    """Format text in different styles"""
    if style == "upper":
        return text.upper()
    elif style == "lower":
        return text.lower()
    elif style == "title":
        return text.title()
    elif style == "reverse":
        return text[::-1]
    else:
        return text

text = "python functions are awesome"
print(f"Original: {text}")
print(f"Uppercase: {format_text(text, 'upper')}")
print(f"Title: {format_text(text, 'title')}")
print(f"Reversed: {format_text(text, 'reverse')}\n")


# ============================================================================
# 15. KEY CONCEPTS SUMMARY
# ============================================================================

print("=" * 60)
print("KEY FUNCTION CONCEPTS SUMMARY:")
print("=" * 60)
print("""
1. def - Define a function
2. Parameters - Variables in function definition
3. Arguments - Values passed when calling
4. return - Send back value from function
5. Default parameters - Pre-set values
6. *args - Variable number of positional arguments
7. **kwargs - Variable number of keyword arguments
8. Lambda - Anonymous short functions
9. Nested functions - Functions inside functions
10. Closures - Functions that remember outer scope
11. Docstrings - Documentation for functions
12. Type hints - Specify expected data types
""")



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
# 2. CALCULATOR WITH OPERATION SELECTION
# ============================================================================

def calculate(num1, num2, operation):
    """
    Perform calculation based on operation string.
    
    Operations: +, -, *, /, **, %
    """
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    elif operation == "**":
        return power(num1, num2)
    elif operation == "%":
        return modulus(num1, num2)
    else:
        return "Invalid operation!"

print("=" * 50)
print("CALCULATOR WITH OPERATION SELECTION")
print("=" * 50)
operations = [(15, 3, "+"), (15, 3, "-"), (15, 3, "*"), (15, 3, "/"), (2, 8, "**"), (15, 4, "%")]
for num1, num2, op in operations:
    result = calculate(num1, num2, op)
    print(f"{num1} {op} {num2} = {result}")
print()


# ============================================================================
# 3. CHAIN CALCULATOR (Multiple operations)
# ============================================================================

def chain_calculate(numbers, operations):
    """
    Process multiple operations in sequence.
    
    Args:
        numbers: List of numbers
        operations: List of operations (+, -, *, /)
    """
    if len(numbers) != len(operations) + 1:
        return "Error: Mismatch between numbers and operations"
    
    result = numbers[0]
    for i, operation in enumerate(operations):
        result = calculate(result, numbers[i + 1], operation)
    
    return result

print("=" * 50)
print("CHAIN CALCULATOR (MULTIPLE OPERATIONS)")
print("=" * 50)
# Example: (10 + 5) * 2 - 3
numbers = [10, 5, 2, 3]
operations = ["+", "*", "-"]
result = chain_calculate(numbers, operations)
print(f"Chain: 10 + 5 * 2 - 3 = {result}")
print(f"(Note: Processes left to right, not by precedence)\n")


# ============================================================================
# 4. ADVANCED MATHEMATICAL FUNCTIONS
# ============================================================================

def square(x):
    """Calculate square of a number"""
    return x ** 2

def cube(x):
    """Calculate cube of a number"""
    return x ** 3

def square_root(x):
    """Calculate square root"""
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return x ** 0.5

def absolute(x):
    """Get absolute value"""
    return abs(x)

def average(*numbers):
    """Calculate average of multiple numbers"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def find_max(*numbers):
    """Find maximum number"""
    return max(numbers) if numbers else None

def find_min(*numbers):
    """Find minimum number"""
    return min(numbers) if numbers else None

print("=" * 50)
print("ADVANCED MATHEMATICAL FUNCTIONS")
print("=" * 50)
print(f"Square of 5: {square(5)}")
print(f"Cube of 3: {cube(3)}")
print(f"Square root of 16: {square_root(16)}")
print(f"Absolute value of -15: {absolute(-15)}")
print(f"Average of 10, 20, 30, 40: {average(10, 20, 30, 40)}")
print(f"Max of 5, 12, 3, 45, 8: {find_max(5, 12, 3, 45, 8)}")
print(f"Min of 5, 12, 3, 45, 8: {find_min(5, 12, 3, 45, 8)}\n")


# ============================================================================
# 5. PERCENTAGE CALCULATOR
# ============================================================================

def calculate_percentage(value, percentage):
    """Calculate percentage of a value"""
    return (value * percentage) / 100

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    discount_amount = calculate_percentage(price, discount_percent)
    final_price = price - discount_amount
    return final_price, discount_amount

def calculate_tax(price, tax_percent):
    """Calculate price with tax"""
    tax_amount = calculate_percentage(price, tax_percent)
    total_price = price + tax_amount
    return total_price, tax_amount

print("=" * 50)
print("PERCENTAGE CALCULATOR")
print("=" * 50)
print(f"20% of 500: {calculate_percentage(500, 20)}")

price = 100
discount = 15
final, discount_amount = calculate_discount(price, discount)
print(f"Price: ${price}, Discount: {discount}%, Final: ${final:.2f} (Saved: ${discount_amount:.2f})")

price = 100
tax = 10
total, tax_amount = calculate_tax(price, tax)
print(f"Price: ${price}, Tax: {tax}%, Total: ${total:.2f} (Tax: ${tax_amount:.2f})\n")


# ============================================================================
# 6. TEMPERATURE CONVERTER
# ============================================================================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

print("=" * 50)
print("TEMPERATURE CONVERTER")
print("=" * 50)
print(f"0°C = {celsius_to_fahrenheit(0):.2f}°F")
print(f"25°C = {celsius_to_fahrenheit(25):.2f}°F")
print(f"100°C = {celsius_to_fahrenheit(100):.2f}°F")
print(f"32°F = {fahrenheit_to_celsius(32):.2f}°C")
print(f"25°C = {celsius_to_kelvin(25):.2f}K\n")


# ============================================================================
# 7. STATISTICS CALCULATOR
# ============================================================================

def calculate_sum(numbers):
    """Calculate sum of numbers"""
    return sum(numbers)

def calculate_average(numbers):
    """Calculate average"""
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    """Calculate median"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

def calculate_variance(numbers):
    """Calculate variance"""
    mean = calculate_average(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_std_dev(numbers):
    """Calculate standard deviation"""
    return calculate_variance(numbers) ** 0.5

print("=" * 50)
print("STATISTICS CALCULATOR")
print("=" * 50)
data = [10, 20, 15, 30, 25]
print(f"Data: {data}")
print(f"Sum: {calculate_sum(data)}")
print(f"Average: {calculate_average(data):.2f}")
print(f"Median: {calculate_median(data)}")
print(f"Variance: {calculate_variance(data):.2f}")
print(f"Standard Deviation: {calculate_std_dev(data):.2f}\n")


# ============================================================================
# 8. COMPOUND CALCULATOR (Complex calculations)
# ============================================================================

def compound_interest(principal, rate, time):
    """Calculate compound interest"""
    amount = principal * (1 + rate/100) ** time
    interest = amount - principal
    return amount, interest

def simple_interest(principal, rate, time):
    """Calculate simple interest"""
    interest = (principal * rate * time) / 100
    amount = principal + interest
    return amount, interest

def loan_payment(principal, annual_rate, years):
    """Calculate monthly loan payment"""
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    
    if monthly_rate == 0:
        return principal / num_payments
    
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    return payment

print("=" * 50)
print("COMPOUND CALCULATOR (FINANCIAL)")
print("=" * 50)
principal = 1000
rate = 5
time = 2

amount, interest = compound_interest(principal, rate, time)
print(f"Compound Interest: Principal ${principal} at {rate}% for {time} years")
print(f"  Final Amount: ${amount:.2f}, Interest: ${interest:.2f}")

amount, interest = simple_interest(principal, rate, time)
print(f"Simple Interest: Principal ${principal} at {rate}% for {time} years")
print(f"  Final Amount: ${amount:.2f}, Interest: ${interest:.2f}")

monthly = loan_payment(200000, 6, 30)
print(f"Monthly Loan Payment: ${200000} loan at 6% for 30 years = ${monthly:.2f}/month\n")


# ============================================================================
# 9. COMPLETE CALCULATOR CLASS-LIKE FUNCTION
# ============================================================================

def complete_calculator(num1, num2, operation, display=True):
    """
    Complete calculator with validation and detailed output.
    
    Returns: Dictionary with calculation details
    """
    result_dict = {
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': None,
        'error': None
    }
    
    try:
        if operation == "+":
            result_dict['result'] = add(num1, num2)
        elif operation == "-":
            result_dict['result'] = subtract(num1, num2)
        elif operation == "*":
            result_dict['result'] = multiply(num1, num2)
        elif operation == "/":
            if num2 == 0:
                result_dict['error'] = "Division by zero!"
            else:
                result_dict['result'] = divide(num1, num2)
        else:
            result_dict['error'] = "Invalid operation!"
    except Exception as e:
        result_dict['error'] = str(e)
    
    if display:
        if result_dict['error']:
            print(f"Error: {result_dict['error']}")
        else:
            print(f"{num1} {operation} {num2} = {result_dict['result']}")
    
    return result_dict

print("=" * 50)
print("COMPLETE CALCULATOR (WITH VALIDATION)")
print("=" * 50)
complete_calculator(20, 4, "+", display=True)
complete_calculator(20, 4, "-", display=True)
complete_calculator(20, 0, "/", display=True)
complete_calculator(20, 4, "unknown", display=True)
print()


# ============================================================================
# 10. SUMMARY OF CALCULATOR FUNCTIONS
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

MATHEMATICAL:
  - square(x)
  - cube(x)
  - square_root(x)
  - average(*numbers)
  - find_max(*numbers)
  - find_min(*numbers)

FINANCIAL:
  - calculate_percentage(value, percent)
  - calculate_discount(price, discount%)
  - calculate_tax(price, tax%)
  - compound_interest(principal, rate, time)
  - simple_interest(principal, rate, time)
  - loan_payment(principal, rate, years)

STATISTICS:
  - calculate_sum(numbers)
  - calculate_average(numbers)
  - calculate_median(numbers)
  - calculate_variance(numbers)
  - calculate_std_dev(numbers)

TEMPERATURE:
  - celsius_to_fahrenheit(celsius)
  - fahrenheit_to_celsius(fahrenheit)
  - celsius_to_kelvin(celsius)

UTILITY:
  - calculate(num1, num2, operation)
  - chain_calculate(numbers, operations)
  - complete_calculator(num1, num2, operation)
""")

