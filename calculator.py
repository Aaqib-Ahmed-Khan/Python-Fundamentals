num1=int(input("enter no 1: "))
num2=int(input("enter no 2: "))

operator=input("enter operator")
match operator:
    case "+":
     print("sum is ",num1+num2)
    case"-":
     print("differnce is ",num1-num2)
    case "*":
     print("product is",num1*num2)
    case "/":
     print("quotient is ")
    case "_":
     print("enter a valid operator")
