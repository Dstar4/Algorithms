"""

PPST
------
Understand
Plan
Carry out Plan
Look Back

-------------------
Power, exponents

Understand
-----------------------
Write algorithm to compute a^b

What is the range of input?
	a can range from 0 to inf
	b can range from 0 to inf

What about fractional or complex numbers
	Integer only

What about negative numbers?
	non-negative only

What about raising to the power of 0?
	n^0 == 1

How much memory do we have?
	Enough

2^0 == 1
2^4 == 2 * 2 * 2 * 2
       |----2^4----|
	   2 * |--2^3--|

a^0 == 1
a^b == a * a^(b-1)

Plan
-------

Analyze
----------
Iterative approach:
	O(n) time complexity
	O(1) space complexity

Recursive approach:
	O(n) time complexity
	O(n) space complexity

"""

def power_recursive(a,b):
	if b == 0:
		return 1
	return a * power_recursive(a, b - 1)

print(power_recursive(2,4))


def power_iter(a,b):
	if b==0:
		return 1

	x = 1

	for i in range(b):	# O(b)
		x *= a
	return x

# print(power_iter(2,4))