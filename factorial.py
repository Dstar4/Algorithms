"""
Factorial

Understand the problem
----------------------------
n!, n must be a non-negative integer
n < 1000



0! == 1
7! == 7 * 6 * 5 * 4 * 3 * 2 * 1

n! == n*(n-1)!

4! == 4 * (4-1)!
4! == 4 * 3!
		  3 * 2 * 1

Plan
---------

Recursive definition:

0! == 1
n! == n * (n-1)!

Add range checking 0..1000
Make sure it's an integer
"""


# First Pass
def factorial(n):

	#TODO add range checking
	#TODO make sure it's an integer

	if n is 0:
		return 1
	return n * factorial(n-1)

# print(factorial(998))



#Second Pass
def factorial2(n):
	a = 1
	for i in range(n, 0, -1):
		a *=i
	return a

print(factorial2(2000))

