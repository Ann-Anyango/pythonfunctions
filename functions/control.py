# control flow if statenment
def even_numbers():
    x=range(10)
    for i in x:
        if i%2==0:
            print (i)
def odd_numbers():
    x=range(20)
    for i in x:
        if i%2!=0:
            print(i)
# else statenment
def divisible_by_five():
    x=range(50)
    for i in x:
        if i %5==0:
            print(f"{i}is divisible by 5")
    else:
        print(f"{i}is not divisible by 5")
# elsi statenment
def multiple_comparision():
    x=range(50)
    for  i in x:
        if i %5==0:
            print(f"{i}is  divisible by 5")
        elif i %7==0:

            print(f"{i} is divisible by 7")
        elif i %9==0:
            print(f"{i} is divisible by 9")
                
        else:
            print(f"{i}is not divisible by 5,7,or9")

                
# comparing if statenment with logical operaters
def odd_or_even():
    x=range(20)
    for i in x:
        if i%2==0 and i %3==0:
            print(f"{i}is divisible by both 2 and 3")
        elif i %2==0 or i %3==0 :
            print(f"{i} is divisible by either 2 or 3")   
        else:
            print(f"{i} is not divisible by either 2 or 3 ")    


def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1
# break statenment
def break_statenment():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break
def contue_statenment():
    x=0
    while x<20:
        x+=1
        if x%3==0:
            continue
        print(x)
         
 # ass
         
#    Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 

def  continue_work():
    x=0
    while x<=50:
        x+=1
        if (x%2!=0):
         continue
        print(x)

# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def integer_prime():
     x=range(20)
     for i in x:
        if i%2==0 and i %3==0:
            print(f"{i}if the number is prime ")
        elif i %2==0 or i %3==0 :
            print(f"{i} is not a prime number")   
        else:
            print(f"{i} if the number is not prime ")    
# Write a function that takes a list of integers as input
# #  and prints the sum of all the even numbers in the list.
# def sum_even(lst):
#     sum_of_even = 0
#     for num in lst:
#         if num % 2 == 0:
#             sum_of_even_numbers += num


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_even_numbers(my_list)




 

# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
#  def divisible_num():
     


