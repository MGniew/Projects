'''Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.'''
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help="Start number")
    args = parser.parse_args()

    if (args.n <= 1):
	    print("n > 1")

    fun = lambda x: x//2 if x%2 == 0 else 3*x + 1

    i = 0
    x = args.n
    while args.n != 1:
        print(args.n)
        args.n = fun(args.n)
        i += 1

    print("Numbers of steps: " + repr(i))


if __name__ == "__main__":
    main()
