def sum_of_digits(n): #The function sumOfDigits takes an integer as input
    #Initialize the variable total to keep track of the total sum of digits
    total = 0

    while n > 0: #The while loop extracts digits to base case = 0
        digit = n % 10 # To get the last digit

        total += digit #Add the digit to the total

        #Remove the last digit by doing integer division by 10
        n = n // 10
        #The loop will go on until no digits are left
    return total

num = 753
print("Sum of digits of", num, "is", sum_of_digits(num)) #Output: 15