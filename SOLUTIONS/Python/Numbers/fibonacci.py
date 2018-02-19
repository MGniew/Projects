import argparse



def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
 

def main():
    parser = argparse.ArgumentParser(description="Fibonacci sequence")
    parser.add_argument('n', type=int, help="amount of fibonacci numbers")

    args = parser.parse_args()
    gen = fibonacci()
    for i in range(args.n):
        print(next(gen), end=' ')
 
    print()


if __name__ == "__main__":
   main()
