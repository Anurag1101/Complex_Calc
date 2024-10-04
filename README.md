**Complex Calculator**

This repository contains a Python implementation of a complex number calculator that supports various arithmetic operations, including addition, subtraction, multiplication, and division of complex numbers. The implementation makes use of object-oriented programming principles and demonstrates the use of dunder (double underscore) methods to overload operators for complex number manipulation.

**Features**:

**Addition:** Add two complex numbers.

**Subtraction:** Subtract one complex number from another.

**Multiplication:** Multiply two complex numbers.

**Division:** Divide one complex number by another with error handling for division by zero.

**User Input:** The program allows users to input real and imaginary parts for complex numbers.

**Implementation Details**:

**Class Complex**: The core class of this implementation is the Complex class, which encapsulates the properties and methods associated with complex numbers.

**Attributes**:

**r:** Real part of the complex number.

**i:** Imaginary part of the complex number.

**Methods**:

__init__(self, r, i): Constructor that initializes the real and imaginary parts.

__add__(self, C2): Overloads the + operator to add two complex numbers.

__sub__(self, C2): Overloads the - operator to subtract one complex number from another.

__mul__(self, C2): Overloads the * operator to multiply two complex numbers.

__truediv__(self, C2): Overloads the / operator to divide one complex number by another, with error handling for division by zero.

__str__(self): Provides a string representation of the complex number in the form of "a + bi".

**Example Usage**
The following code demonstrates how to use the Complex class to perform arithmetic operations on complex numbers:
# Example usage

r1 = int(input("Enter the real part of first number: "))  # Input real part of 1st number

i1 = int(input("Enter the imaginary part of first number: "))  # Input imaginary part of 1st number

r2 = int(input("Enter the real part of second number: "))  # Input real part of 2nd number

i2 = int(input("Enter the imaginary part of second number: "))  # Input imaginary part of 2nd number

num1 = Complex(r1, i1)

num2 = Complex(r2, i2)

print(num1 + num2)   # Expected output: Sum of the two complex numbers

print(num1 - num2)   # Expected output: Difference of the two complex numbers

print(num1 * num2)   # Expected output: Product of the two complex numbers

print(num1 / num2)   # Expected output: Quotient of the two complex numbers

**Error Handling**:

The division method raises a ValueError if the denominator is zero, ensuring that the program does not attempt to divide by zero, which would result in an undefined operation.

**Requirements**: **Python 3.x**

**Installation**:

**Clone this repository:**   git clone https://github.com/USERNAME/complex_calc.git

**Navigate to the project directory:**  cd complex_calc

**Run the program:**  python Complex_Calc.py

**Contribution**:

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements or new features.

**License**:

This project is licensed under the MIT License.
