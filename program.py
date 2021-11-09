#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program generate random numbers

import random


def number_calculator(ranom_numbers, small_number):
    # this function tells which number is lower

    for loop_counter in ranom_numbers:
        if small_number > loop_counter:
            small_number = loop_counter

    return small_number


def main():
    # this function generate random numbers
    random_numbers = []
    print("Starting ...\n")
    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(-100, 100)  # a number between 0 and 100
        random_numbers.append(random_number)
        print(
            "The random number {0} is: {1}".format(
                loop_counter + 1, random_numbers[loop_counter]
            )
        )
    small_number = random_number
    smallest_number = number_calculator(random_numbers, small_number)

    print("\nThe smallest number is {0}".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
