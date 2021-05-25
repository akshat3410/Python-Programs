# # multiply = lambda x, y : x * y 
# # print(multiply(8, 9))
# # ------------------------------------------------------------------------
# # def fibonatchi(n):
# #     while (True):    
# #         if n == 1:
# #             return 0
# #         elif n == 2:
# #             return 1
            
# #         else:
# #             return fibonatchi(n - 1) + fibonatchi(n-2)
            
# # number = int(input("Enter the Number:"))

# # print("The fibonatchi of number is ", fibonatchi(number))
# # # 0112358
# # ---------------------------------------------------------------------------
# # def factorial_itrative(n):
    
# #     fac = 1
# #     for i in range(n):
# #         fac = fac * (i + 1)
# #     return fac

# # def factorial_recursive(n):
# #     if n == 1:
# #         return 1
# #     else:
# #         return n * factorial_recursive(n - 1)
# # number = int(input("Enter The Number:"))

# # print("This is itrative", factorial_itrative(number))
# # print("This is recursive", factorial_recursive(number))
# # ----------------------------------------------------------------------------
# # f = open("Hello World.txt")

# # content = f.read()

# # print(content)

# # f.close()
# # --------------------------------------------------------------------------
# # f = open("Hello World.txt")

# # content = f.read()

# # print(content)

# # f.close()
# # ---------------------------------------------------------------------------
# # f = open("Hello World.txt")

# # content = f.read()

# # print(content)

# # f.close()
# # ----------------------------------------------------------------------
# # # f = open("Hello World.txt")
# # print(f.readlines())


# # f.close()
# # -----------------------------------------------------------------------------
# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             value=input("type here\n")
#             with open("harry-ex.txt","a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c==2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
# print("health management system: ")
# a=int(input("press 1 for lock the value and 2 for retrieve "))

# if a==1:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)

# ----------------------------------------------------------------------------------------
# import random

# lower = "abcdefghijklmnopqrstivwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTIVWXYZ"
# number = "1234567890"
# symbol = "[]{}()*;/,._-"

# all = lower + upper + number + symbol
# length = 8

# password = "".join(random.sample(all, length))

# print(password)

# ------------------------------------------------------------------------------
# import random

# # Generates a random number between 1 and 20
# guess = random.randint(1, 20)
# chances = 10

# # print(guess)

# done = False

# while chances > 0:
#     print(f"You have {chances} left. Guess the number")
#     x = int(input())
#     if(x == guess):
#         done = True
#         print(f"You have guessed the number correctly!. The number is {guess}")
#         break
#     chances = chances-1

# if(done == False):
#     print("You lost the game :(")