#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This prgram calculates the volume of a function


def volume(length):
    # This'll calculate the volume of a cube

    # process
    volume = length * length * length

    # output
    print("The volume is " + str(volume) + " cm^3")


def main():
    # This asks for the length, then it runs volume()

    # variables
    length = 0

    while True:
        try:
            length = int(input("What is the length: "))

            # runs volume()
            volume(length)
            break
        except ValueError:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
