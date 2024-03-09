def caculation (x,y,oprator):
    if oprator == '+':
        total = x + y
        return total
    elif oprator == '-':
        total = x - y
        return total
    elif oprator == '*':
        total = x*y
        return total
    elif oprator == '/':
        total = x/y
        return total
    
num1 = float(input("Please enter a number : "))
num2 = float(input("Please enter a number : "))

ops = ['+','-','*','/']

oprator = input("Enter the math symbol you would like to use : ")

if oprator not in ops:
    print('your selected opratpr not valid')
calcu = caculation(num1,num2,oprator)

print(calcu)