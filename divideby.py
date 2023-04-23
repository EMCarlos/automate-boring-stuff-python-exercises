def div24by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
        
print(div24by(2))
print(div24by(12))
print(div24by(0))
print(div24by(1))
