import random

# Функция для генерации случайного математического примера с скобками
def generate_complex_example(operators, depth=3):
    if depth == 0:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(operators)
        
        if operator == '/' and num2 == 0:
            num2 = random.randint(1, 100)
        
        return f"{num1} {operator} {num2}"
    else:
        inner_expression = generate_complex_example(operators, depth - 1)
        return f"({inner_expression}) {random.choice(operators)} ({inner_expression})"

# Список операторов, ограниченный до +, -, * и /
operators = ['+', '-', '*', '/']

# Генерация и решение 500 более сложных примеров
for _ in range(500):
    example = generate_complex_example(operators, depth=3)
    solution = str(eval(example))
    print(f"Пример: {example} = {solution}")
