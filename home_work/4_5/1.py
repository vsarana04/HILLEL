n = int(input('Введите число: '))
cnt = 0
kub_sum = 0
for cnt in range(1, n+1):
    if cnt % 3 == 0:
        continue
    print(f'Куб числа {cnt} равен = {int(cnt) ** 3}')
    kub_sum =+ int(cnt) ** 3
print('Сумма кубов: ', kub_sum)

