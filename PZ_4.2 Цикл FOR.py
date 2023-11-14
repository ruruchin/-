N = int(input("Введите целое число N: "))

sum_of_numbers = 0
K = 0

for i in range(N):
    sum_of_numbers += i
    if sum_of_numbers <= N:
        K += 1
    else:
        break

print("Наибольшее K:", K)
print("Сумма чисел от 1 до K:", sum_of_numbers)