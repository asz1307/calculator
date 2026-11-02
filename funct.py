def calculate(o,x,y):
    if o == "+":
        return x + y
    if o == "−":
        return x - y
    if o == "×":
        return x * y
    if o == "÷":
        return x / y
    if o == "^":
        return x ** y
print(calculate(input("Operation? "),float(input("Value of x? ")),float(input("Value of y? "))))