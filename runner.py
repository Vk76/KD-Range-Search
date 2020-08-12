"""
Author : Vishal Kriplani
Subject : ADS Assignment
Topic : 2-D Range Search
class : 6th sem shift 2
Roll no : 69
"""

from KDRangeSearch import TwoDimensionRangeSearch
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

if __name__ == "__main__":
    canvas = TwoDimensionRangeSearch()
    while True:
        inp = input()
        if inp[0] == '=':
            break
        canvas.add(tuple(map(int, inp.split())))

    while True:
        try:
            print(
                '=======================================================================')
            x, y = map(int, input().split())
            canvas.drawPoints()
            iterations, found = canvas.query((x, y))
            if found:
                print('Point ({},{}) found with {} iterations'.format(
                    x, y, iterations))
            else:
                print('Point ({},{}) not found with {} iterations'.format(
                    x, y, iterations))
        except Exception:
            break
