import random


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

