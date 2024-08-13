def fibonacci(number):
    if number == 0 or number == 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

