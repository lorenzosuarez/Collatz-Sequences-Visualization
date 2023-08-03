## Collatz Conjecture Visualization

This Python program is designed to generate and visualize the Collatz sequence for a given positive integer. The Collatz sequence, also known as the 3n+1 sequence or hailstone sequence, is a sequence of numbers obtained by repeatedly applying the Collatz rule to a starting positive integer, until the sequence reaches the number 1.

### The Collatz conjecture states that for any positive integer n:

- If n is even, divide it by 2 to get n/2.
- If n is odd, multiply it by 3 and add 1 to get 3n+1.

By repeatedly applying these rules, the sequence eventually reaches the number 1.

## Usage

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/lorenzosuarez/Collatz-Sequences-Visualization.git
```
Navigate to the project directory:

```bash
cd collatz-conjecture
```
Run the program by executing the Python script:

Copy code
python collatz_conjecture.py
Enter a positive integer when prompted. The program will generate the Collatz sequence for that number and display it in a plot.

### Example
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

## Collatz Conjecture Example

![result graph](https://github.com/lorenzosuarez/Collatz-Sequences-Visualization/assets/55887438/27f74c72-0577-4a81-8ecb-6429c8355790)

Description: This is an example of how the Collatz Conjecture program works. The user entered the number 165, and the program generated the Collatz sequence [165, 496, 248, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1] for that number.


