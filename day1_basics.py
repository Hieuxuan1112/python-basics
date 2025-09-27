# Exercise 1: Write a program to input your age and print it out
age = int(input("Enter your age: "))
print("You are", age, "years old.")


# Exercise 2: Write a program to check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2== 0:
    print(f"{number} is an EVEN number")
else:
    print(f"{number} is an ODD number")


# Exercise 3: Write a program to print all numbers from 0 to 10
for a in range(11):
    print(a, end=" ")
print()


# Exercise 4: Write a program to calculate the sum of all numbers from 0 to 10
a = 0
sum = 0
while a <= 10:
    sum += a
    a += 1
print(f"Sum of all numbers from 0 to 10 is: {sum}", end="\n")


# Exercise 5: Write a program to print the multiplication table from 2 to 9
for numA in range(2, 10, 1):
    for numB in range(1, 11, 1):
        print(f"{numA} x {numB} = {numA * numB}", end="\t")
print()

# Exercise 6: Write a program to calculate the factorial of a number n input from the keyboard
n = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i += 1
print(f"Factorial of {n} is: {factorial}")


# Exercise 7: Write a program to check if a number is prime or not
number = int(input("Enter a number: "))
if number <= 1:
    print(f"{number} is not a Prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a Prime number")
            break
    else:
        print(f"{number} is a prime number")


# Exercise 8: Write a program to reverse a string
string = input("Enter a string: ")
string_lenght = len(string)
reverse_string = ""
for char in range(string_lenght - 1, -1, -1):
    reverse_string = reverse_string + string[char]
print(reverse_string)


# Exercise 9: Write a program to find sum of all even numbers from 0 to n, include n if n is even
number = int(input("Enter a number: "))
sum = 0
for i in range(2, number+1, 2):
    sum += i
print(f"Sum of all even numbers from 0 to {number} is: {sum}")


# Exercise 10: Write a program to print the following pattern for n lines, where n is input from the keyboard
n = int(input("Enter a number: "))
for a in range(1, n+1):
    for b in range(1, a+1):
        print("*", end="")
    print()