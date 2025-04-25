def even_odd(num):#The function even_odd takes one parameter: num
    if num % 2 == 0: #The modulus operator gives the remainder

        print(f"{num} is even")#If remainder is 0, it is even
    else:
        print(f"{num} is odd")#If remainder is not 0, it is odd

even_odd(15) #Output: 15 is odd
even_odd(10) #Output: 10 is even