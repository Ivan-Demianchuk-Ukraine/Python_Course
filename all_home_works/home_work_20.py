def skipper(cond, reason='this function skipped, but reason not added.'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if cond:
                return reason
            elif not cond:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@skipper(True, 'because of bug')
def hello(name):
    return f"Hello, {name}"


print(hello("User"))


@skipper(True)
def summer(operand_1, operand_2):
    return operand_1 + operand_2


print(summer(2, 5))


@skipper(False)
def subtraction(operand_1, operand_2):
    return operand_1 - operand_2


print(subtraction(15, 10))
