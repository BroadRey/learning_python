from functools import wraps


# task_1
def check_type(func):
    @wraps(func)
    def wrapper():
        func_result = func()
        if isinstance(func_result, int) or isinstance(func_result, float):
            return func_result
        return None
    return wrapper


# task_2
def add_prefix_suffix(prefix, sufix):
    def decorator(func):
        @wraps(func)
        def wrapper():
            func_result = func()
            func_result = prefix + func_result + sufix
            return func_result
        return wrapper
    return decorator