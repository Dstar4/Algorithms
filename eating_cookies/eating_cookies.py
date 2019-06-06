#!/usr/bin/python
"""
Understand
-------------
- can eat 1,2,3 cookies at a time.
- n cookies in a jar
-count the number of possible ways to eat all the cookies in the jar

Plan
-------------
- use recursion
- base case
  - if n = 0 return 1
- can only eat 1, 2, or 3 cookies at a time.
- call recursive function that moves closer to base case (n = 0)
-

- make a cache for performance?

Carry Out Plan
--------------

Look Back
--------------

"""

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # set our count to increment
    count = 0

    # base case
    if n == 0:
        count += 1

    # loop between number of cookies we can eat at a time
    for i in range(1, 4):

        # subtract cookies eaten at a time from the number of cookies we have
        # if zero cookies remain, increment.
        if n - i == 0:
            count += 1

        # if more than 0 cookes remain go through the function again with the remaining cookies
        elif n - i > 0:
            count += eating_cookies(n-i)

    # print("answer", count)
    return count


# eating_cookies(3)  # 13
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
