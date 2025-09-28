# Day 2: Functions with *args, **kwargs, and lambda
# Exercises cover function definition, dynamic parameters, and lambda usage

# Exercise 1: Write a function that calculates the cube of a number, defaulting to zero
def calc_cube(num=0):
    return num**3
print(calc_cube(5))
print(calc_cube())

# Exercise 2: Write a function that accepts an arbitrary number of positional arguments and prints each one.
def display_all(*arguments):
    for item in arguments:
        print(item)
display_all("hello", 2, 5.4, True)

# Exercise 3: Write a function that calculates and prints the sum of all values passed as keyword arguments.
def calc_sum(**key_args):
    total_sum = 0
    for key, value in key_args.items():
        total_sum += value
    print(total_sum)
calc_sum(x=5, y=10, z=15)

# Exercise 4: Write a function to print all key-value pairs passed as keyword arguments.
def show_info(**key_values):  # **key_values is a dict containing key-value pairs
    for key, value in key_values.items():  # Iterate through the dict
        print(f"{key}: {value}")
show_info(name="Alice", age=25)  # name: Alice \n age: 25
show_info(city="Hanoi")          # city: Hanoi

# Exercise 5: Write a function that prints the sum of the values from all keyword arguments.
def total_values(**key_args):
    print(sum(key_args.values()))
total_values(a=5, b=10, c=15)

# Exercise 6: Use the filter() function and a lambda to extract all even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Exercise 7: Write a function that calculates and returns the sum of an arbitrary number of positional arguments.
def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result
print(add_numbers(1, 2, 3, 4, 5))

# Exercise 8: Write a function to check if a given integer is a prime number.
def check_prime(n):
    if n < 2:
        print(f"{n} is not a prime number")
        return
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                return
        print(f"{n} is a prime number")
input_number = int(input("Enter a number: "))
check_prime(input_number)

# Exercise 9: Use a lambda function as a key to sort a list of numbers in descending order.
num_list = [5, 2, 9, 1, 5, 6]
sorted_nums = sorted(num_list, key=lambda x: -x)
print(sorted_nums)

# Exercise 10: Write a function to print the key and value of all keyword arguments in a specific format.
def display_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
display_details(name="hieu", age=22, country="vietnam")

# Exercise 11: Use the map() function and a lambda to double every element in a list.
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_values = list(map(lambda x: x * 2, values))
print(doubled_values)

# Exercise 12: Write a function that calculates the average of an arbitrary number of positional arguments.
def average(*args):
    if len(args) == 0:
        return 0
    tong = 0
    for a in args:
        tong += a
    return tong / len(args)
print(average(1, 2, 3, 4, 5, 6, 4, 8, 9))
print(average())

# Exercise 13: Write a function that prints the values of all keyword arguments separated by hyphens.
# 1st way
def printAll(**kwargs):
    if not kwargs:
        return
    else:
        i = len(kwargs)
        for key, value in kwargs.items():
            if i == 1:
                print(f"{value}", end=" ")
            else:
                print(f"{value}", end="-")
            i -= 1
    return
printAll(Name="Hieu", age=22, country="VietNam")

# 2nd way
def printALL(**kwargs):
    if not kwargs:
        return
    else:
        values = kwargs.values()
        result = "+".join(str(value) for value in values)
        print(result)
    return
printALL(Name="Hieu", age=22, country="VietNam")

# Exercise 14: Write a function that prints the maximum value from an arbitrary number of positional arguments.
def max_number(*args):
    if not args:
        print("No values provided.")
        return
    else:
        if any(value < 0 for value in args):
            print("Invalid input: negative numbers are not allowed.")
            return
        else:
            max_value = max(args)
            print(max_value)
            return
max_number(1, 2, 3, 4, 5, 6, -7, 8, 9)
max_number(1, 2, 3, 4, 5, 6, 7, 8, 9)
max_number()

# Exercise 15: Write a function that uses map with a lambda to double the numbers in a list, then uses filter with a lambda to keep only the numbers greater than 5, and prints the final list.
def process_numbers(*args):
    if not args:
        print("No values provided.")
        return
    else:
        double_value = list(map(lambda x: x*2, args))
        biggerthan5value = list(filter(lambda y: y>5, double_value))
        print(biggerthan5value)
        return
process_numbers(2, 3, 4)
process_numbers(1, 2, 3)

# Exercise 16: Create a function that sums all positional number arguments (*args). If a keyword argument multiply (containing a number) is passed, multiply the sum by that value before returning the total.
def calculate_total(*args, **kwargs):
    if not args:
        print("No values provided.")
        return
    else:
        tong = 0
        for a in args:
            tong += a
        if "multiply" in kwargs:
            tong *= kwargs["multiply"]
            print(tong)
            return
        else:
            print(tong)
            return
calculate_total(1, 2, 3)
calculate_total(1, 2, 3, multiply=2)
calculate_total()
calculate_total(1, 2, 3, 4, 5)
