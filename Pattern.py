# Pattern Maker
def Pattern(n):
    #upper star Triangle
    for i in range(n):
        print((n - i - 1)*" ", end="")
        print((2*i + 1)*"*")
    #lower star Triangle
    for i in range(n - 1, -1 , -1):
        print((n - 1 - i)*" ", end="")
        print((2*i + 1)*"*")
n = int(input("Enter the number for Pattern:"))
print(Pattern(n))
