def calculate_expression(N):
    result = 0.0
    sign = 1.0  # начальный знак

    for i in range(1, N + 1):
        result += sign * (1.0 * i / 10)
        sign = -sign  # меняем знак перед следующим слагаемым

    return result


N = int(input("Введите целое число N (>0): "))
result = calculate_expression(N)
print(f"Значение выражения для N = {N}: {result}")
