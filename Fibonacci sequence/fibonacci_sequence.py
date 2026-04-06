#define the function to generate the fibonnaco sequence
def fibonacci(n):
    #convert input to integer 
    n=int(n)

    #First two numbers
    a=0
    b=1

    for i in range(n):
        print(a, end=" ")
        #update the values of a and b
        a,b = b ,a+b 
        
#Example
fibonacci(10)