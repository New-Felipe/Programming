def eh_primo(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

for numero in range(2, 101):
    if eh_primo(numero):
        print(numero, end=' ')
