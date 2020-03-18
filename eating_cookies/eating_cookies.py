#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
ways = 0
def eating_cookies(n, cache=None):
  print(n, ways)
  if n == 0:
    return (ways + 1)
  elif n == 1:
    return (ways + 1)
  elif n == 2:
    return (ways + 2)
  elif n == 3:
    return (ways + 4)
  
  eating_cookies(n-1)
  eating_cookies(n-2)
  eating_cookies(n-3)




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


    # (0), 1)
    # (1), 1)
    # (2), 2)
    # (5), 13)
    # (10), 274)

    # (50, [0 for i in range(51)]), 10562230626642)
    # (100, [0 for i in range(101)]), 180396380815100901214157639)
    # (500, [0 for i in range(501)]), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)
