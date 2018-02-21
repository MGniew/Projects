'''Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

'''

def change(cost, money, nominals_list):

    nominals_list.sort(reverse = True)

    change = money - cost
    if (change < 0):
        print("Gimme more money!")

    change = round(change, 2)
    result = dict()

    for i in nominals_list:
        x = int(change/float(i))
        change -= x * float(i)
        change = round(change,2)
        result[i] = x

    return result


def main():

    nominals = [0.01, 0.05, 0.1, 0.25]
    cost = float(input("cost: "))
    money = float(input("money: "))

    result = change(cost,money,nominals)

    for key, value in sorted(result.items(), reverse = True):
        print(repr(key).ljust(5), repr(value))

if __name__ == "__main__":
    main()

