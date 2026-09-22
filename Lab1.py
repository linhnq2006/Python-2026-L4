import math
# 1
radius = float(input("Enter circle radius? "))
area = 3.14 * (radius ** 2) 
print(f"Circle area = {area}\n")


# 2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
print(f"{int(celsius)} (C) = {fahrenheit} (F)\n")


# 3
num_prime = int(input("Enter a number? "))
if num_prime > 1:
    is_prime = True
    for i in range(2, int(num_prime ** 0.5) + 1):
        if num_prime % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num_prime} is a prime number\n")
    else:
        print(f"{num_prime} is a NOT prime number\n")
else:
    print(f"{num_prime} is a NOT prime number\n")


# 4
num_perfect = int(input("Enter a number? "))
total_divisors = 0
for i in range(1, num_perfect):
    if num_perfect % i == 0:
        total_divisors += i

if total_divisors == num_perfect and num_perfect > 0:
    print(f"{num_perfect} is a perfect number\n")
else:
    print(f"{num_perfect} is a NOT perfect number\n")


# 5
color_list = ["Blue", "Yellow", "Black", "Red", "White"]  
fav_color = input("What is your favorite color? ").strip()
color_list_lower = [c.lower() for c in color_list]

if fav_color.lower() in color_list_lower:
    idx = color_list_lower.index(fav_color.lower())
    print(f"Your color is at index {idx} in my list\n")
else:
    print("Sorry, I could not find your color\n")


# 6
range1 = list(range(7))
print("range1:", ", ".join(map(str, range1)))

range2 = list(range(1, 11, 3))
print("range2:", ", ".join(map(str, range2)))

range3 = list(range(5, 0, -1))
print("range3:", ", ".join(map(str, range3)))

range4 = list(range(6, -3, -2))
print("range4:", ", ".join(map(str, range4)))
print()


# 7
def remove_dollar_sign(s):
    new_string = ""
    for i in range(0, len(s)):
        if s[i] != "$":
            new_string = new_string + s[i]
    return new_string


# 8
def extract_even(l):
    return [num for num in l if num % 2 == 0]


# 9
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 10
def get_divisors(n):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


# 11
print("Enter coordinates for Point 1:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("Enter coordinates for Point 2:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between two points = {distance:.2f}\n")


# 12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m-1:
            print("*"*n)
        else:
            print("*"+" "*(n-2)+"*")
print_pattern(4, 5)


