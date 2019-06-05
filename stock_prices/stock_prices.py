#!/usr/bin/python
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




Look Back
--------------



"""

import argparse

def find_max_profit(prices):
  pass








find_max_profit([1050, 270, 1540, 3800, 2])




















if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))