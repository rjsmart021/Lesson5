#Lesson 5:Assignments ] Python Functions
#1.The Calculator App
 # This function addition two number
def summation(num1, num2):
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter an integer: "))
    return print(num1 + num2,"The sum of the numbers!")
 # This function subtraction two number
def subtract(dif1, dif2):
    dif1 = int(input("Enter an integer: "))
    dif2 = int(input("Enter an integer: "))
    return print(dif1 - dif2,"The diference of the numbers!")
 # This function multiplies two numbers
def multiply(Mult1, Mult2):
    Mult1 = int(input("Enter an integer: "))
    Mult2 = int(input("Enter an integer: "))
    return print(Mult1 * Mult2, "The product is!")
 # This function divides two numbers
def divide(Div1, Div2):
    Div1 = int(input("Enter an integer: "))
    Div2 = int(input("Enter an integer: "))
    if Div2 == 0:
        print("Denominator is zero")
    else:
       print(Div1 / Div2, "the quotient!")        
d1a = input('Would you like to add, subtract, multiply, or divide?')
if d1a == 'add':
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter an integer: "))
    print(num1 + num2,"The sum of the numbers!")
elif d1a == 'subtract':
    dif1 = int(input("Enter an integer: "))
    dif2 = int(input("Enter an integer: "))
    print(dif1 - dif2,"The diference of the numbers!")
elif d1a == 'multiply':
    Mult1 = int(input("Enter an integer: "))
    Mult2 = int(input("Enter an integer: "))
    print(Mult1 * Mult2, "The product is!")
elif d1a == 'divide':
    Div1 = int(input("Enter an integer: "))
    Div2 = int(input("Enter an integer: "))
    if Div2 == 0:
        print("Denominator is zero")
    else:
       print(Div1 / Div2, "the quotient!")     
#2. The Shopping List Maker
#Task 1
# use a fuction we can call in it use while loop to ask what we want to add to get users input their input add to my list by apend is the best way to add
#add it to back of the list let them continue to add things
Shoping_list = ['Ice cream', 'jello', 'gummies', 'life savers']
print("lets go shopping")
action = input("go or stop")
print(Shoping_list)
if action == "go":
    print("Shoping is a go")
    YN= input("add items or remove items")
    if YN == "add items":
        print("add an item to the shoping list")
        Shoping_list.append(input("Enter an item"))
        print(Shoping_list)
        print("complete")
    elif YN == "remove items":
            print("remove an item from the shoping list")
            Shoping_list.remove(input("Enter an item to remove"))
            print(Shoping_list)
else:
    action == "stop"
    print("Shoping Complete")
#Remove an item from the list
#3
#Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
def Average(grades):
    return sum(grades)/ len(grades)
print("Average of the grades =")
print(Average(grades))
#Task 2 

def low(grades):
    return min(grades)
print("Lowest grade =")
print(min(grades))
#BONUS
for grade in grades:
    if grade >= 90:
        print("Your Grade is an A")
    elif grade  >=80:
        print("Your grade is a B")
    else:
        print("Your grade is a C")