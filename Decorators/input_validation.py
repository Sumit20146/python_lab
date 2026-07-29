import functools

def validate_positive_integers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if not isinstance(arg, int) or isinstance(arg, bool) or arg <= 0:
                print(f"Error: Invalid argument '{arg}'. All arguments must be positive integers.")
                return
        return func(*args, **kwargs)
    return wrapper

@validate_positive_integers
def calculate_area(length, width):
    print(f"Area: {length * width}")

calculate_area(5, 10)
calculate_area(-2, 4)
