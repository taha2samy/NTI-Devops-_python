import time
def repeat_decorator(number,seconds):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(number):
                time.sleep(seconds)
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat_decorator(3,1)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")