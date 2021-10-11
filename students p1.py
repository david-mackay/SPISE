"""Python has square root built in but you can write your own.
Here's a common technique for finding the sqaure root of some
number x........

1. Begin with initial guess 1.
2. Update your guess to be .5 * ((guess**2) + x / guess) .
3. Repeat step 2 as needed.
4. Return the value of guess as the square root

Write a program which prompts the user for the number x, performs
the above procedure and then prints out the result - which 
should be close to the actual square root."""

x = int(input("Enter a number. "))

answer = x ** 0.5 
guess = 1

while (guess > answer + 0.1) or (guess < answer - 0.1): #checks if the number is out of range. If True, the loop iterates
    guess = 0.5 * ((guess **2 + x) / guess)
   
print(format(guess, ".2f")) #formats the result to 2 decimal places
