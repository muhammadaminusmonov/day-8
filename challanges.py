# # challenge #1
# # this program will find how many cans of paint you need to paint your wall
# import math
#
#
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You will need {num_of_cans} to paint your wall")
#
#
# paint_calc(height=3, width=5, cover=5)


# # challenge #2
# # this program will check if the entered number is prime number
# def prime_checker(num):
#     is_prime = True
#     for n in range(2, num):
#         if num % n == 0:
#             is_prime = False
#     if is_prime:
#         print("The number is prime number")
#     else:
#         print("The number is not prime number")
#
#
# number = int(input("Enter a number to check it: "))
# prime_checker(number)
