'''Next Prime Number - Have the program find prime numbers until the user chooses to stop asking'''


def is_prime(x):
    
    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5) + 1 , 2):
        if x % i == 0:
            return False

    return True

def get_next_prime(current):
    
    while True:
        if current == 2:
            current += 1
        else:
            current += 2

        if is_prime(current):
            break

    return current

def main():
    
    prime = 2
    get_next = True

    print("next: y, stop: any (default y)")

    while get_next:

        print(prime, end = " ")
        anwser = input()
        get_next = True if anwser == '' or anwser == 'y' else False

        if (get_next != False):
            prime = get_next_prime(prime)


if __name__ == "__main__":
    main()
