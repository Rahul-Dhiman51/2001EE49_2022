def factorial(x):
    factor = 1
    if x<0:
     print("Fctorial does not exist")
    elif x==0:
     print("Factorial of 0 = 1")  
    else:
     for i in range (1,x+1):
         factor = factor*i
    
    print("Factorial of " ,x ,"is" ,factor,)
x=int(input("Enter the number whose factorial is to be found"))
factorial(x)