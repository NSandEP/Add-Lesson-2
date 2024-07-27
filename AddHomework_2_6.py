def generating_pass(n):                    # описание функции
    pass_ = ''                             # присвоение пустого строкового значения подобранному паролю (результату)
    for i in range(1, n):                  # создание цикла нахождения первого числа для пароля
        for j in range(i + 1, n):          # создание цикла нахождения второго числа для пароля
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
for n in range(1, 20 + 1):
    pass_ = generating_pass(n)
    print(f'{n} - {pass_}')
