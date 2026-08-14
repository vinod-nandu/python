
import math
import time
import webbrowser
import requests

time.sleep(5)
#output = requests.get("https://www.google.com")


#from math import sqrt

# Use the module name as a prefix
print(math.sqrt(16)) 
#print(sqrt(16)) 


#webbrowser.open("https://www.google.com")
#print(output)
'''
📦 1. How to Install Packages
You cannot install packages directly inside a Python file. Instead,
 you use your computer's Terminal (Mac/Linux) or Command Prompt/PowerShell (Windows).
 Python uses a package manager called pip to download libraries from the
  Python Package Index (PyPI).Standard command: 
  python -m pip install package_nameExample
   (Installing NumPy): python -m pip install numpy
   Mac/Linux alternative: python3 -m pip install numpy
   Upgrade a package: python -m pip install --upgrade numpy

'''


import pandas as pd

# -------------------------------------------------------------
# 1. CREATING A DATAFRAME
# -------------------------------------------------------------
# You can create a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 22],
    'City': ['New York', 'London', 'Paris', 'London'],
    'Salary': [70000, 85000, 95000, 60000]
}
df = pd.DataFrame(data)

# Note: To load external data, you would use:
# df = pd.read_csv('dataset.csv')

print("--- Original DataFrame ---")
print(df)
print("\n")