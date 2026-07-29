def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Access denied: Please log in first.")
            return
        return func(*args, **kwargs)
    return wrapper

is_logged_in = False  # toggle this to test

@login_required
def view_dashboard():
    print("Welcome to your dashboard!")

view_dashboard()
