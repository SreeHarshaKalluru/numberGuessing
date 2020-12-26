import random
from math import *

def even_or_odd(num):
    return "The number is an " + ("even" if (num%2==0) else "odd") + " number."
def is_ten_multiple(num):
    return "The number is " + ("" if (num%10==0) else "not ") + "a 10 multiple."
def is_five_multiple(num):
    return "The number is " + ("" if (num%5==0) else "not ") + "a 5 multiple."
def is_prime(num):
    return "The number is " + ("" if (num!=1 and num%2!=0 and sum([num%a==0 for a in range(3,floor(sqrt(num)) + 1)])==0) else "not ") + "a prime number."

def num_properties(num):
    return [even_or_odd(num), is_ten_multiple(num), is_five_multiple(num), is_prime(num)]

x, y = [int(a) for a in input("Enter the start and end numbers(+ve) with a space in between : ").split()]
random_num = random.randint(x,y+1)
num_prop = num_properties(random_num)
i = 1
print("You will have four chances to guess the number.")
while(i<=4):
    try:
        curr_guess = int(input("Enter your guess : "))
        if(curr_guess==random_num) :
            break;
        print("Hint : " + num_prop[i-1])
        i += 1
    except ValueError as ve:
        print("Please enter an integer only.")

