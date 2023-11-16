#!/usr/bin/python3 

import random
import sys

class Expression:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    
    def __str__(self):
        return "(" + str(self.left) + " " + str(self.op) + " " + str(self.right) + ")"
    

class Number:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    

class Operator:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)


def generate_expression(depth):
    if depth == 0:
        return Number(random.randint(1, 9))
    else:
        left = generate_expression(depth - 1)
        right = generate_expression(depth - 1)
        op = Operator(random.choice(["+", "-", "*", "/"]))
        return Expression(left, right, op)


def evaluate_expression(expr):
    if isinstance(expr, Number):
        return expr.value
    else:
        left = evaluate_expression(expr.left)
        right = evaluate_expression(expr.right)
        op = expr.op.value
        return eval(str(left) + op + str(right))

def main():
    for _ in range(500):
        expr = generate_expression(random.randint(1,5))
        #expr = generate_expression(1)
        print(expr)
        sys.stdout.flush()

        result = evaluate_expression(expr)
        user_awswer = sys.stdin.readline().strip()
        if user_awswer == str(result):
            continue
        else:
            print("U R NOT ROBOT")
            sys.stdout.flush()
            exit(1)
    print("U R ROBOT, here is your flag: CCC{m4th_1s_3z}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
