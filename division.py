from readdata import a, b


def div(a, b):
    if b == 0:
        print(f"Error: cannot divide {a} by zero. Division skipped.")
        return None
    c = a / b
    print(f"Division of {a} and {b} is : {c}")
    return c
