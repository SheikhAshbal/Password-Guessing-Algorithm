# Password Guessing Algorithm

This Python script serves as a simple password guessing algorithm utilizing a brute-force approach to match a user-input password.

<h2>Instructions:</h2><br><br>

<h4>Requirements:</h4><br>

Python 3.x
random and string modules (both are part of Python's standard library)
Time module(The time module in Python provides functions for handling time-related tasks)

<h4>Usage:</h4><br>

Clone or download the repository containing the Python script.
Run the script using a Python interpreter.
Input the desired password when prompted.

<h4>Script Functionality:</h4><br>

Upon inputting a password, the script uses a brute-force method to guess the password by generating random combinations of ASCII letters and digits.
It keeps generating passwords until the generated password matches the user-provided password.
The number of attempts made to guess the password and the time taken for the process are displayed as output.

<h4>Code Explanation:</h4><br>

The script utilizes Python's random module to randomly select characters from the set of ASCII letters and digits (totaling 62 characters).
It initiates a loop that continues until the generated password matches the user-provided password.
For each attempt, it counts the number of attempts made to find the password.

<h4>Important Notes:</h4><br>

This script is primarily for educational purposes and should not be used for any unauthorized access.
It demonstrates a simple brute-force approach and may not be efficient for longer or complex passwords.
