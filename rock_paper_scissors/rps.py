#!/usr/bin/python

import sys

rps = [['rock'], ['paper'], ['scissors']]
def rock_paper_scissors(n):
  if n == 0:
    return []
  if n == 1:
    return [['rock'], ['paper'], ['scissors']]

    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')