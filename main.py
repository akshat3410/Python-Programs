# import turtle
#
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.width(x / 150 + 1)
#     t.forward(x)
#     t.left(59)

#
# #
# ------------------------------------------------------------------------
# import turtle
#
# colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
#
# screen = turtle.Screen()
# trtl = turtle.Turtle()
# trtl.speed(0)
# screen.bgcolor('black')
#
# for x  in range(360):
#     trtl.pencolor(colors[x%6])
#     trtl.width(x / 5 + 1)
#     trtl.forward(x)
#     trtl.left(20)

#-------------------------------------------------------
#
# import winsound
# f = 32767
# d = 111111

# winsound.Beep(f,d)

# -------------------------------------------------------------
# from pytube import YouTube
#
# link = input("https://www.youtube.com/watch?v=W0DM5lcj6mw")
# video = YouTube(link)
# stream = video.streams.get_highest_resolution()
# stream.download()
#
#
# ------------------------------------------------------------
# def hcf(a, b):
#     if (b == 0):
#         return a
#     else:
#         return hcf(b, a % b)
#
#
# a = 60
# b = 48
# print(hcf(60, 48))
# ----------------------------------------------------------------
# var1 = int(input("Enter First Number:"))
# var2 = int(input("Enter Second Number:"))

# var3 = input("What you want:"+'+, -, *, /:')

# if var1 == 56 and var2 == 9 and var3 == '+':
#     print("77")
# elif var3 == '+':
#     print(int(var1) + int(var2))

# elif var1 == 93 and var2 == 42 and var3 == '-':
#     print("0.007")
# elif var3 == '-':
#     print(int(var1) - int(var2))

# elif var1 == 45 and var2 == 3 and var3 == '*':
#     print("555")
# elif var3 == '*':
#     print(int(var1) * int(var2))

# elif var1 == 56 and var2 == 6 and var3 == '/' :
#     print("4")

# # else:
# #     print(int(var1) / int(var2))


# # ------------------------------------------------------------------

n = int(input("Enter Rows"))

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print()
# # ---------------------------------------------------------------------------

# n = 18
# number_of_guesses = 1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses < 9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number < 18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number > 18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses, "no.of guesses he took to finish.")
#         break
#     print(9 - number_of_guesses, "no. of guesses left")
#     number_of_guesses += 1

# if (number_of_guesses > 9):
#     print("Game Over")
# ------------------------------------------------------------------------------------------

"""
"r" - Open file for reading -- Default
"w" - Open file for writing 
"x" - Creates a file if not exist
"a" - Add more content to a file
"b" - binary mode
"t" - text mode -- Default
"+" - read and write 
"""
# ----------------------------------------------------------------------------

# def print_factors(x):
#     print("The factor of", x ,"are:")
#     for i in range(1, x + 1):
#         if x % i == 0:
#             print(i)
#
# num = 28
# print_factors(num)
# --------------------------------------------------------------------
# import pyttsx3
# engine= pyttsx3.init()
# engine.say("Good Afternoon sir")
# engine.say("What can i help you")
# engine.runAndWait()
# ---------------------------------------------------------------------
# import calendar

# yy = 2021
# mm = 10
# yy = int(input("Enter Year:"))
# mm = int(input("Enter month:"))
# print(calendar.month(yy, mm))
# -------------------------------------------------------------------
# def Pattern(n):
#     #upper star Triangle
#     for i in range(n):
#         print((n - i - 1)*" ", end="")
#         print((2*i + 1)*"*")
#     #lower star Triangle
#     for i in range(n - 1, -1 , -1):
#         print((n - 1 - i)*" ", end="")
#         print((2*i + 1)*"*")
# Pattern(10)
# -----------------------------------------------------------------------
# def factorial_itrative(n):
    
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
    
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
# number = int(input("Enter The Number:"))

# print("This is itrative", factorial_itrative(number))
# print("This is recursive", factorial_recursive(number))
#-----------------------------------------------------------------
# def fibonatchi(n):
#     while (True):    
#         if n == 1:
#             return 0
#         elif n == 2:
#             return 1
            
#         else:
#             return fibonatchi(n - 1) + fibonatchi(n-2)
            
# number = int(input("Enter the Number:"))

# print("The fibonatchi of number is ", fibonatchi(number))
# # 0112358
# ---------------------------------------------------------------------------
# def x_pattern(n):
#     for i in range(0, n):
#         for j in range(0, n):
#             if i == j or j == n- 1- i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# x_pattern(100)
# ---------------------------------------------------------------------------
# def frequency():
#     Spos = int(input("Enter the Speed of sound:"))
#     WaveLength = float(input("Enter the WaveLength:"))

#     WaveL = WaveLength / 100

#     Frequency = Spos / WaveLength

#     Total = Spos * 1000 / 15

#     print("Freqency of Sound is :", str(Total))

# frequency()
# --------------------------------------------------------------------------------

