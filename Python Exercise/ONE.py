# Question 1 - Write a function to print "Hello_USERNAME!"

def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")
    
hello_name('Nathan')


# Question 2 - Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def odd_numbers():
    for i in range(1,101,2):
        print(i)
        
#odd_numbers()
        
def odd_numbers2():
  	numbers = list(range(0, 101))
    for number in numbers:
        if number % 2 != 0:
        	print(number)
        
odd_numbers2()


# Question 3 - Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))


# Question 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 5 - Write a function to check to see if all numbers in list are consecutive numbers.

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

