# # nick_name = input("What is your nickname? ", )
# # print("Hello {}".format(nick_name))

# print("The value of 3+4 is", 3 + 4, ".")
# print("The value of 3+4 is ", 3 + 4, ".", sep='')


# print("On the first line", end="")
# print("On the first line")

# temp = eval(input("Enter a temperature value in Celsius: "))
# print("In Fahrenheit, that is", 9/5*temp+32)

# temp = eval(input("Enter a temperature value in Celsius: "))
# f_temp = 9/5*temp+32

# print("In Fahrenheit, that is", f_temp)

# if f_temp > 212:
#     print("That temperature is above the boiling point.")

# else:
#     print("That temperature is below the freezing point.")


#Exercise 1.8
print("Exercise 1.8.")
print("\n")
print("1. Print a box like the one below.")
print("\n")
for i in range(4):
    print('*'*19)
print("\n")

print("2. Print a box like the one below")
print("\n")

print("*"*19)
print("*", " " * 17, "*", sep="")
print("*", " " * 17, "*", sep="")
print("*"*19)
print("\n")
print("\n")

print("3. Print a triangle like the one below")
print("\n")

print("*")
print("**")
print("***")
print("****")
print("\n")


print("4. Write a program that computes and prints the result of 512 - 282 / 47*48 + 5. It is roughly 0.1017.")
print("\n")

result = (512 - 282)/(47*48+5)
print("The rough estimate of this computation is: ", result)
print("\n")

# print("5. Ask the user to enter a number.")
# num = eval(input("Please enter a number: "))
# squared_num = num**2

# print("The square of {} is {}".format(num, squared_num))
# print("\n")


# print("6. Ask the user to enter a number x.")
# x_value = eval(input("Please enter a number: "))

# x_value_1 = x_value * 2
# x_value_2 = x_value * 3
# x_value_3 = x_value * 4
# x_value_4 = x_value * 5
# print(x_value_1, x_value_2, x_value_3, x_value_4, sep="---")


# print("""7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There
# are 2.2 pounds in a kilogram.""")
# weight_in_kg = eval(input("Please enter the weight in kg: "))
# kg_pd = 2.2

# result = weight_in_kg * kg_pd
# print("The converted weight to pounds is ", result)
# print("\n")


# print("""8. Write a program that asks the user to enter three numbers (use three separate input statements).
# Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.""")
# print("\n")

# num_1 = eval(input("Enter the first number: ", ))
# num_2 = eval(input("Enter the second number: ", ))
# num_3 = eval(input("Enter the third number: ", ))
# total = num_1 + num_2 + num_3
# average = total/3
# print("The sum of the three numbers entered is: ", total)
# print("The average of the three numbers entered is: ", average)
# print("\n")


print("""9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
            the percent tip they want to leave. Then print both the tip amount and the total bill with the
            tip included.""")
print("\n")

meal_price = eval(input("Enter the price of the meal: "))
perc_tip = eval(input("How much percent tip are you leaving behind?: "))
tip_amount = perc_tip/100 * meal_price
total_bill = tip_amount + meal_price

print(f"The tip amount is ${tip_amount} and the total bill  is ${total_bill}".format())


