import random
import time


def fib_sequence(target_num):

    num1 = 0
    num2 = 1

    for i in range(target_num):

        if i % 2 == 0:
            num1 = num1 + num2
        else:
            num2 = num1 + num2

    if target_num % 2 == 0:

        return num1

    return num2


if __name__ == "__main__":

    et = time.time()

    rand_number = random.randint(15, 35)

    print(f"fib({rand_number})={fib_sequence(rand_number)}")

    print(f"fib({rand_number}) took {time.time()-et} milliseconds")
