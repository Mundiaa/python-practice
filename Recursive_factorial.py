def factorial(n): #The function factorial takes only one parameter 'n'

    if n == 0 or n == 1:
        return 1 #factorial of 0 or 1 is 1
    else:

        return n * factorial(n - 1) # This keeps calling the function until it reaches the base case
#This will compute 5 * 4 * 3 * 2 * 1 = 120
print("factorial of 5 is ", factorial(5))

#This his will compute 6 * 5 * 4 * 3 * 2 * 1 = 720
print("factorial of 6 is ", factorial(6))