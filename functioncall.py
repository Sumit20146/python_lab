import functools
import datetime

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG] '{func.__name__}' called at {timestamp}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    print(f"Hello, {name}!")

greet("Sumit")