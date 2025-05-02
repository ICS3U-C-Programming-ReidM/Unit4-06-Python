#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program uses a nested loop to create a 2D RGB array and print it


def main():

    # Nested loop for all colors
    for r in range(0, 256, 15):
        for g in range(0, 256, 15):
            for b in range(0, 256, 15):

                # Print the RGB value and the color
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m ".format(
                        r, g, b, (("RGB"), r, g, b)
                    )
                )


if __name__ == "__main__":
    main()
