# is_polindrome_recursion
This repository contains a Python code file, is_polindrome_recursion.py, which is a simple implementation of a palindrome checker using recursion. The code determines whether a given string is a palindrome

# How it works
The code uses a recursive approach to check whether a string is a palindrome. Here's a brief explanation of the algorithm:

The main function, is_palindrome, takes a string as input and removes any non-alphanumeric characters and converts the string to lowercase.
The base case for the recursion is when the length of the string is 0 or 1, in which case it is considered a palindrome.
If the string has more than one character, the function checks if the first and last characters are equal. If they are not, the string is not a palindrome.
If the first and last characters are equal, the function calls itself recursively with the substring excluding the first and last characters.
The recursion continues until the base case is reached, and the final result is returned.

To use this code, you need to have Python installed on your system. Follow these steps to run the code:

Clone the repository or download the is_polindrome_recursion.py file.

Open a terminal or command prompt and navigate to the directory where the file is located.

Run the following command:

# bash
Copy code
python is_polindrome_recursion.py
You will be prompted to enter a string. Type the string and press Enter.

The code will determine whether the input string is a palindrome or not and display the result.

# Example
Here's an example run of the code:

Enter a string: racecar
The string is a palindrome.

Enter a string: hello
The string is not a palindrome.



Enter a string: hello
The string is not a palindrome.
Limitations
It's important to note that the code only considers alphanumeric characters for determining palindromes. Any non-alphanumeric characters are ignored during the comparison. Additionally, the code assumes the input string is in English and does not handle special characters or diacritics.

# Contributing
Contributions to this code are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This code is licensed under the MIT License. Feel free to use and modify it as per the terms of the license.

# Acknowledgments
This code was created by Eddy Kubwimana
