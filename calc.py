import math

####################################################################
def add():
    list = []
    sum = 0
    inp = int()
    length = int(input("Enter len: "))
    for i in range(0,length):
        inp = int(input("Enter number: "))
        list.append(inp)
    for i in range(len(list)):
        sum += list[i]
    print(f"Sum is :{sum}")
        
def subtract():
    list = []
    diff = 0
    inp = int()
    length = int(input("Enter length: "))
    for i in range(0,length):
        inp = int(input("Enter number: "))
        list.append(inp)
    for i in range(len(list)):
        diff -= list[i]
    print(f"Difference is: {diff}")
    
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y
def trignometric():
    pass
#####################################################################

# print('Below are your following options :')
# print('1.Addition')
# print('2.Subtraction')
# print('3.Division')
# print('4.Multiply')
# print('5.Perform a trignometric Calculation')
choice = int(input("Below are your following options :\n"
               "1.Addition\n"
               "2.Subtraction\n"
               "3.Division\n"
               "4.Multiply\n"
               "5.Perform a trignometric Calculation\n"
               "Your Choice :"))



match choice:
    case 1 :
        add()  
    case 2 :
        subtract()
    case 3 :
        divide()
    case 4 :
        multiply()
    case 5 :
        trignometric()