#    Write a function that uses while, if and continue statements to print all the even
#  numbers between 0 and 50. 

def  continue_work():
    x=0
    while x<=50:
        x+=1
        if (x%2!=0):
         continue
        print(x)

# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def integer_prime(x=11):
        if (x%1==0 and x %11==0):
            print(f"{x}if the number is prime ")
        else:
            print(f"{i} if the number is not prime ") 
 # Write a function that takes a list of integers as input
# # #  and prints the sum of all the even numbers in the list.
def sum_even():
        sum=0
        for i in range(0,30):
            if i %2==0:
                sum=sum+i
        print(sum)     


# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def divisible_num(num1,num2):
        sum=0
        for i in range(num1,num2):
                if i%3==0:
                  sum+=i
                  num1[2,3,4,5]
        print(sum)
