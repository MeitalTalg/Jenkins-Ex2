# calculator.py

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second.
    
    Raises:
        ValueError: If division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
