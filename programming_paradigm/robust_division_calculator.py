def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        
        # Use int() if the result is a whole number (e.g., 6.0 -> 6)
        if result.is_integer():
            return f"The result of the division is {int(result)}"
        else:
            return f"The result of the division is {result:.1f}"  # One decimal place without trailing zero
    except ValueError:
        return "Error: Please enter numeric values only."
