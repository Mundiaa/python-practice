def sum_lists(numbers):#The function sum_lists lists that holds one parameter: numbers

    total = 0 #Initialize a variable total to 0 to hold the sum

    #Loop through each number in the list
    for num in numbers:
        total += num #Adds the current number to the total

    return total

#Create a list of numbers
num = [1, 2, 3, 4, 5]
print("Sum:", sum_lists(num))
