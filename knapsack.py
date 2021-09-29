#! /usr/bin/python
from random import random, randint

if __name__ == "__main__":
  #simpleKnapsack.py given in class
  n = 7
  k = 100

  def knapsackBool(i, size):
      if size == 0:
          return True
      if size < 0:
          return False
      if i == 0:
          return False
      return knapsackBool(i - 1, size) or knapsackBool(i - 1, size - S[i])

  for _ in range(0, 100):
      S = [randint(1, k / 2) for _ in range(0, n + 1)]
      if knapsackBool(n, k):
          print('solution exists')
      else:
          print("solution does not exist")

  n = 5
  k = 10
  S = [None, 11,12,23,435,44,4,20]
  print(knapsackBool(n,k))
