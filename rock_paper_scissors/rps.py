# !/usr/bin/python
import sys
"""
Understand
-----------------

- generate all the possible plays that can be made in Paper Rock Scissors
- n represents the number of plays per round
- output all possible plays that can be made, each round
- Output should be a list of lists
- base case - n = 0


Plan
--------------------
-Use recursion
- Make a list of all plays in P.R.S.






Implement
--------------------

Look Back
-------------------
"""


def rock_paper_scissors(n):

    rps_arr = ['rock', "paper", "scissors"]
    new_arr = []
    if n > 0:
        print("n", n)
        for item in range(0, n):
            print("item", item)
            rock_paper_scissors(n-1)

    print(new_arr)
    return new_arr


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
