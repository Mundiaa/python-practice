def factorial(n): #Initialize the function factorial that holds the value 'n'
    result = 1 #Initialize result to 1 since factorial of 0 is 1

    for i in range(1, n + 1): #Loop multiplies result to each number  from n to 1
        result *= i

    return result #Return the final computed factorial

print("factorial of 4 is ", factorial(4)) #Output: 24
print("factorial of 7 is ", factorial(7)) #Output: 5040