from math import pi

print("Problem 1. Convert radians to degrees")
def rad_to_degrees(rad):
    # radians to degrees involves multiplying radians by pi / 180
    deg = rad * (180 / pi)
    return deg
print("pi/4 radians = " + str(rad_to_degrees(pi/4)) + " degrees")

print()

print("Problem 2. Sort a list")
def list_sorter(list, sorter):
    if sorter == "asc":
        list.sort(reverse = False) # sorts ascending
        return list
    elif sorter == "desc":
        list.sort(reverse = True) # sorts descending
        return list
    elif sorter == "None":
        return list
    
x = [1, 0, 5, 4, 9]
print(list_sorter(x, "desc"))

print()

print("Problem 3. Convert decimal to binary")
def dec_to_bin(num):
    s = ""
    while num != 0:
       s = s + str(num % 2)
       num = num // 2
    s2 = ""
    for i in s:
        s2 = i + s2
    return s2

print(dec_to_bin(76)) # should print 1001100

print()

print("Problem 4. Count the vowels in a string")
def vowel_counter(word):
    n = 0
    word = word.lower()
    for i in word:
        if i == "a":
            n = n + 1
        elif i == "e": 
            n = n + 1
        elif i == "i":
            n = n + 1
        elif i == "o":
            n = n + 1
        elif i == "u":
            n = n + 1
    return n

word = "Hello"
print(word + " has " + str(vowel_counter(word)) + " vowels")

print()

print("Problem 5. Hide the credit card number")
def last_four(num):
    num = str(num)
    censored = ""
    for i in num[0:-4:1]:
        i = "*"
        censored = censored + i
    for i in num[-4:len(num):1]:
        censored = censored + i
    return censored

print(last_four(4444444444444444))

print()

print("Problem 6. Are the Xs equal to the Os?")
def x_and_o(str_var):
    x_counter = 0
    o_counter = 0
    str_var = str_var.lower()
    for i in str_var:
        if i == "o":
            o_counter = o_counter + 1
        elif i == "x":
            x_counter = x_counter + 1
    if x_counter == o_counter:
        return True
    else:
        return False
   
print(x_and_o("xoXOxOO")) # this should print False (there are more o's than x's)

print()

print("7. Create a calculator function")
def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == ".":
        return num1 * num2

print(calc(6, ".", 4)) # should return 24

print()

print("8. Give me the discount")
def disc(price, discount):
    new_price = price - discount
    return new_price

print(disc(100, 20))

print()

print("9. Just the numbers")
def just_nums(my_list):
    new_list = []
    for i in my_list:
        if type(i) == int:
            new_list.append(i)
        else:
            continue
    return new_list

my_list = ["Hello", 2, 5, "World", 7, 6]
print(just_nums(my_list)) # should return [2, 5, 7, 6]

print()

print("Problem 10. Repeat the characters")
def repeat_chars(phrase):
    new_phrase = ""
    for i in phrase:
        new_phrase = new_phrase + i + i
    return new_phrase

print(repeat_chars("123a!")) # should return “112233aa!!”