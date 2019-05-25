def user_operation():
    return input('Type operation: ')

def user_number():
    #Return numbers used in operations
    n1 = int(input('First number: '))
    n2 = int(input('Second number: '))
    return (n1, n2)

#Operations
def add(x, y):
    a = x + y
    return ('%d + %d is %d' % (x, y, a))
def sub(x, y):
    s = x - y
    return ('%d - %d = %d' % (x, y, s))
def mult(x, y):
    m = x * y
    return ('%d * %d is %d' % (x, y, m))
def div(x, y):
    d = x / y
    return ('%d / %d is %d' % (x, y, d))
def sqr(x,y):
    d = x ** y
    return ('%d ** %d is %d' % (x, y, d))
def calculate():
    while True:
        n1, n2 = user_number()
        operation = user_operation()
        if operation.lower() == 'quit':
            break
        elif operation == '+':
            print (add(n1, n2))
        elif operation == '-':
            print (sub(n1, n2))
        elif operation == '*':
            print (mult(n1, n2))
        elif operation == '/':
            print (div(n1, n2))
        elif operation == '**':
            print (sqr(n1, n2))
        else:
            print ("That is not a valid operation!!")

def main():
    print ("Calculator program by Tzortzis\n"
           "Available operations:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication(*)\n4. Division (/)\n5. Power (**)"
           "Type their respective character(s) to perform the selected operation\n"
           "Type 'quit' to end the program.\n")

    calculate()

if __name__ == "__main__":
    main()