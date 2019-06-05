#!/usr/bin/python
import argparse
"""
Understand
-------------
- function recieves a list of stock prices as an input

- returns max profit that can be made from a single buy and sell

- You must buy first, before selling


Plan
-------------
- Find max difference between the smallest and largest prices in a list of prices
- Make sure the max profit is computed by substracting a price by a price that comes before it.

- Keep track of current_min_price and max_profit_so_far


Carry Out Plan
--------------

- Take in list of prices
- Ennumerate the list, return value and index.
- Subtract values of list and index of the values
- If index is 1 or more and value is more than max profit, set new max profit

"""


def find_max_profit(prices):   
    max_profit = None

    # loop through list of prices getting the values and index
    for item, value in enumerate(prices):

        # loop through again starting at the next index to get the next values
        for j in range(item + 1, len(prices)):


            # set current profit to the value of the j loop subtracting the value of the current index.
            current_profit = prices[j] - value

            # if the max profit has not been set or is greater than the current max_profit set it to the new profit
            if max_profit is None or current_profit > max_profit:

                max_profit = current_profit

    return max_profit


find_max_profit([1050, 270, 1540, 3800, 2])

"""
Look Back
--------------
I think this could be done recursively insted of calling another for loop, you could call find_max_profit again..
We are looping through all the data 2x here, this could get expensive with large data sets.

"""


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
