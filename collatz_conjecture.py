"""
Collatz Conjecture

Author: Lorenzo Suarez
Date: August 3, 2023
Description: This program takes a positive integer from the user and generates the Collatz sequence for that number.
"""

import matplotlib.pyplot as plt

def collatz_sequence(n):
    """
    Generates the Collatz sequence for a given positive integer.

    Parameters:
        n (int): The positive integer for which to generate the Collatz sequence.

    Returns:
        list: A list containing the Collatz sequence for the given integer.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(sequence):
    """
    Plots the Collatz sequence.

    Parameters:
        sequence (list): A list containing the Collatz sequence.

    Returns:
        None
    """
    x_values = list(range(len(sequence)))
    plt.plot(x_values, sequence, '-o', color='blue')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.title('Collatz Conjecture')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    try:
        # Get user input for a positive integer
        num = int(input("Enter a positive integer: "))

        # Check if the input is a positive integer
        if num <= 0:
            raise ValueError("The number must be positive")

        # Generate the Collatz sequence for the input number
        collatz_seq = collatz_sequence(num)

        # Print the Collatz sequence
        print("Collatz sequence:", collatz_seq)

        # Plot the Collatz sequence
        plot_collatz_sequence(collatz_seq)
    except ValueError as e:
        print("Error:", e)
