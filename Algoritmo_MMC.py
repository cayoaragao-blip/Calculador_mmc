# Atribuição de valores
n1 = 18
n2 = 20


# Função para descobrir o MDC (maior divisor comum) e logo depois retornar o MMC (menor múltiplo comum) entre dois números
def mmc(n1, n2):
    n3 = n1*n2
    while n1%n2 != 0:
        n1, n2 = n2, n1%n2
    return n3 // n2


# Armazenamento e exibição do resultado
resultado = mmc(n1, n2)
print(f"O MMC destes números é {resultado}")

# Próximo passo: possibilitar a descoberta do MMC de 3 números ou mais;