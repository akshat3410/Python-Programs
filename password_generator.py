
import random

lower = "abcdefghijklmnopqrstivwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTIVWXYZ"
number = "1234567890"
symbol = "[]{}()*;/,._-"

all = lower + upper + number + symbol
length = 8

password = "".join(random.sample(all, length))

print(password)

