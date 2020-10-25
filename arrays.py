#!/bin/python3
#Program to reverse the integer list and print it in one line
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    revarr = arr[::-1]
    for i in range(n):
        print(revarr[i], end=" ")
