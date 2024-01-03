aux = number = int(input('Entre com um número inteiro: '))
sum = 0

while number != 0:
    value = number % 10
    number //= 10
    sum += value

print(f'A soma dos dígitos do número {aux} é {sum}')
