numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # список для простых числе, которые делятся на 1 и на себя
not_primes = [] # список остальных числе
for number in numbers: #для numbers сделаем number раз цикл
    if number == 1: # если numbers=1
        continue #идем в начало цикла
    is_prime = True # Простое число = Истина
    for i in range(2, number):# берем числа от 2 и далее по списку, но больше 2
        if number % i == 0:# остаток от деления umber/ i=0, целое число
            is_prime = False # Фальш
            break# конец
    if is_prime:# для is_prime
        primes.append(number) # в Пример добавляем число из списка
    else:# еще
        not_primes.append(number)#
print("Primes:", primes) #выводим список Простые числа
print("Not Primes:", not_primes) # ввыводим список Не простые числа
