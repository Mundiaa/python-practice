def reverse_string(s):

    reversed_string = "" #Initialize an empty string to store the reversed result

    #Loop through each character in the input string from the last index to the 1st
    for i in range(len(s) -1, -1, -1): #This gives the last index. #The range() counts backwards from the end to the beginning
        reversed_string += s[i] #Add each character one by one to the result string

    return reversed_string #Return the reversed string

original = "strathmore"
reversed_string = reverse_string(original)
print("Original string:", original) #Output: strathmore
print("Reversed string:", reversed_string) #Output: eromhtarts
