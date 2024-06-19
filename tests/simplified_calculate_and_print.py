# simplified_calculate_and_print.py

def calculate_and_print(a_string, b_string, operation_string):
    print("Starting calculation")
    try:
        a = float(a_string)
        b = float(b_string)
        print(f"Converted inputs: a={a}, b={b}")
    except ValueError:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    if operation_string == 'add':
        print(f"Performing addition: {a} + {b}")
        result = a + b
    else:
        print(f"Unknown operation: {operation_string}")
        return

    print(f"The result of {a_string} {operation_string} {b_string} is equal to {result}")
