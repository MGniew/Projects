'''Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them'''
import math

def main():

    x = int(input("Enter a number: "))
    if (x <= 1):
        print("x > 1")
        return

    max_factor = math.sqrt(x)
    i = 2

    while x > 1:
        if x % i == 0:
            print(i, end=" ")
            x = x//i
            i = 2
        elif i > max_factor:
            print(x, end=" ")
            x = x//x
        else:
            i += 1
            

    print()



if __name__ == "__main__":
    main()
