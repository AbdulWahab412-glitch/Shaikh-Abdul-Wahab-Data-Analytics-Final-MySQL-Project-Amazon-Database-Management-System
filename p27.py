""" 
Introduction to jupiter Notebook :

1. What is Jupiter Notebook?

- Open-source web-based IDE for python and data analysis.
- Stands for Julia, Python, R.
    Jupiter = Julia + Python  R (Support multiple languages).
- Used in Data Science, AI, ML, Research and data visualization.
- File extension = .ipynb (IPython Notebook)

2. Why use it

- Interactive: mix of code + output + explanation + Visualization in one place
- Great for exprimentation, documentation, and collaboration.

3. Real-World use cases:

- Data analysis at NetFlix, Google, Kaggle competition.
- Academic research papers.
- Prototyping ML models.

4. Installation & Setup, Working on Jupiter Notebook.

- Install Anaconda Distribution (recommended).
- Easy package & environment management.
- Alternative: pip install notebook or pip install jupiterlab.
- Run using Anaconda Navigator or command:

- Opens in brower -> .ipynb files.
cells:
    - Code Cell -> Write & run Python code.
    - Markdown Cell -> Add text, headings, equations.

5. Understand the Interface

- Dashboard: File browser.
- Notbook Structure: 
            Cells -> Code cells, Markdown cells, Raw cells.
            Kernel -> Execute code.
- Toolbar & Menus:
    Run, stop, restart Kernel.
- Save notebook (.ipynb extention).

- Working with cells.
- Code cell:
print('hello, python in jupiter!')

- Markdown Cell:
Heading: # Heading 1, ## Heading 2.
Formating: bold , italic, inline code.
Lists, tables, links, LaTeX equations ($a^2+b^2=c^25).

-Keyword shortcuts:
Shift + Enter -> Run Cell.
A/B -> Insert cell Above/below.
D + D -> Delete cell.

"Jupiter is not just a coding tool --
It's your lab notebook for ideas, experiments, and discoveries.
Master it, and you'll master the art of presenting data prefessionally."

"""
def greet(name):
    return f"Hello, {name}"
greet("Wahab")


""" 
===================================================
  Modules VS Packages VS Libraries in python
===================================================

1. Module:
    - A single python file (.py) containing functions, classes or variable.
    - Help in reusing code across programs.
    - Example: math, random (built-in modules).

2. Package:
    - A collection of modules organized in a directory.
    - Contains an __init__.py file (can be empty).
    - Allows hierarchical structuring of python code.
    - Example: numpy.linalg (linalg is a sub-package inside numpy).

3. Library:
    - A collection of packages and module that provide wide functionality.
    - Often maintained by the community for specific purposes.
    - Example: Numpy, pandas, TensorFlow, Scikit-learn.
Hierarchy:
    Library > Packages > Module
"""

# ----------------------------
# 1. Example of a module
# ----------------------------

import math # math is abuild-in python module

print("Square root of 16:",math.sqrt(16))
print("Factorial of 5",math.factorial(5))

#-----------------------------
# 2. Example of a package
# ----------------------------
# Numpy is a library, and inside it we have sub-packages like numpy.linalg

import numpy as np
arr = np.array([1,2,3,4])
print("Array",arr)

# Using a sub-package (numpy.linalg)
from numpy import linalg

matrix = np.array([[1,2],[3,4]])
print("Determinant of matrix:",linalg.det(matrix))

# ----------------------------------
# 3. Example of a birary
# ----------------------------------

import pandas as pd
data  = {"Name":["Shalini","Rahul","Kavita"],"Age":[28,30,25]}
df = pd.DataFrame(data)
print("\nDataFrame from Pandas Library:\n",df)

""" 
Data Via CSV using numpy

1. Introduction
CSV (Comma Separeted Values) is a common format to store tabular data.
numpy provides efficient way to read, write and mamipulate CSV files.

Main functions:
- numpy.loadtxt() -> Reads simple CSV files.
- numpy.genfromtxt() -> Reads CSV with missing values  / advanced handling.
- numpy.savetxt() -> Save Numpy arrays into CSV.

2. Steps to work with CSV using numpy
- Prepare a CSV file (like students.CSV).
- Load data info Numpy arrays (loadtxt, genfromtxt).
- Perform operations (sum,  mean, filter, etc.,).
- Save processed data back into a CSV.

3. Sample CSV file (students.CSV)
ID,Name,Math,Science, English
1,Amit,78,85,82
2,Neha,92,88,95
3,Rahul,67,72,70
4,Anjali,85,79,90
5,Rohan,58,60,65


Note-
- Use loadtxt() for numeric-only CSV.
- Use genfromtxt() for mixed data (string + numbers).
- Perform operations using Numpy functions (sum, mean, min, max).
- Save back to CSV using savetxt().
"""

# Program: Load, Analyze, And, Save CSV Data

import numpy as np
import os

# --------------------------------------------------------------
# Utility: Get curretn script directory (so code work anywhere)
# --------------------------------------------------------------

base_path = os.path.dirname(__file__)
csv_file = os.path.join(base_path,"students.csv") # CSV input file
output_file = os.path.join(base_path,"results.csv") # CSV output file
print(output_file)
# ---------------------------------------------------------
# Program 1: Load Csv (only Numeric Columns) Using loadtxt
# ---------------------------------------------------------
# - Skip header row
# - select columns: math (2), Science (3), English (4)
# ---------------------------------------------------------


with open (csv_file, "w") as f:
    f.write(
        "ID,Name,Math,Science,English\n"
        "1,Amit,78,85,80\n"
        "2,Riya,88,90,92\n"
        "3,Rahul,65,70,68\n"
        "4,Neha,95,93,97\n"
    )
print("successfully created CSV file")
import numpy as np
data = np.loadtxt(csv_file, delimiter= ",",  skiprows = 1, usecols=(2,3,4))
print("\n--- program 1: Load csv (Numeric only) ---")
print("data from CSV:\n", data)
print("shape of data (row ,columns ):",data.shape) # Extra funcationality

# -------------------------------------------------------
# Program 2: Load CSV with Mixed Data using genfromtxt
# -------------------------------------------------------
# - Read both strings and numbers
# - Keeps header row as column names
# -------------------------------------------------------
import numpy as np
data_mixed = np.genfromtxt(csv_file,delimiter=",", dtype=  None,encoding="utf-8",names =True)
print("\n--- Program 2: Load CSV with Mixed Data ---")
print("CSV Data with column names:")
print(data_mixed)
print("Student Name:", data_mixed['Name'])
print("Math Marks:",data_mixed['Math'])
print("All column names",data_mixed.dtype.names) # Extra functionality