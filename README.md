# Collatz-Sequences-Visualization
A Python program to visualize the Collatz sequence for a given positive integer using matplotlib

Collatz Conjecture Visualization
This Python program is designed to generate and visualize the Collatz sequence for a given positive integer. The Collatz sequence, also known as the 3n+1 sequence or hailstone sequence, is a sequence of numbers obtained by repeatedly applying the Collatz rule to a starting positive integer, until the sequence reaches the number 1.

### The Collatz conjecture states that for any positive integer n:

If n is even, divide it by 2 to get n/2.
If n is odd, multiply it by 3 and add 1 to get 3n+1.
By repeatedly applying these rules, the sequence eventually reaches the number 1.

Usage
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/lorenzosuarez/Collatz-Sequences-Visualization.git
Navigate to the project directory:

bash
Copy code
cd collatz-conjecture
Run the program by executing the Python script:

Copy code
python collatz_conjecture.py
Enter a positive integer when prompted. The program will generate the Collatz sequence for that number and display it in a plot.

Example
Let's consider an example where the user enters the number 6. The Collatz sequence for 6 is as follows:

less
Copy code
Collatz sequence: [6, 3, 10, 5, 16, 8, 4, 2, 1]
The program will then display a plot showing the variation of values in the Collatz sequence over the steps taken.

Technical Details
Functions
collatz_sequence(n): This function generates the Collatz sequence for a given positive integer n.

Parameters:
n (int): The positive integer for which to generate the Collatz sequence.
Returns:
list: A list containing the Collatz sequence for the given integer.
plot_collatz_sequence(sequence): This function plots the Collatz sequence.

Parameters:
sequence (list): A list containing the Collatz sequence.
Returns:
None
Dependencies
This program uses the matplotlib library to create plots of the Collatz sequence. Ensure you have the library installed by running the following command:

Copy code
pip install matplotlib
Execution
When the program is run, it first prompts the user to enter a positive integer. If the user provides a non-positive value, an error message will be displayed. Otherwise, the program calculates the Collatz sequence for the input number using the collatz_sequence function and plots it using the plot_collatz_sequence function. The plot displays the variation of values in the Collatz sequence against the number of steps taken.

