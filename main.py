class Complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part
    
    def __add__(self, C2):  # Using dunder function add 
        return Complex(self.r + C2.r, self.i + C2.i)
    
    def __sub__(self, C2):
        return Complex(self.r - C2.r, self.i - C2.i)
    
    def __mul__(self, C2):  # Using dunder function multiply
        real_part = self.r * C2.r - self.i * C2.i
        imag_part = self.r * C2.i + self.i * C2.r
        return Complex(real_part, imag_part)
    
    def __truediv__(self, C2):
        denom = C2.r ** 2 + C2.i ** 2  # c^2 + d^2
        if denom == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (self.r * C2.r + self.i * C2.i) / denom  # a*c + b*d
        imag_part = (self.i * C2.r - self.r * C2.i) / denom  # b*c - a*d
        return Complex(real_part, imag_part)

    def __str__(self):  # Return String dunder function of values
        return f"{self.r} + {self.i}i"


# Example usage
r1=int(input("Enter the real part of first number: ")) #input Real part of 1st number
i1=int(input("Enter the imaginary part of first number: ")) #input Imaginary part of 1st number
r2=int(input("Enter the real part of second number: ")) #input Real part of 2nd number
i2=int(input("Enter the imaginary part of second number: ")) #input imaginary part of 2nd number.
num1 = Complex(r1, i1)
num2 = Complex(r2, i2)

print(num1 + num2)   # Expected output: 7 + 9i
print(num1 - num2)   # Expected output: 1 + 1i
print(num1 * num2)   # Expected output: -8 + 31i
print(num1 / num2)   # Expected output: 1.28 + -0.04i 
